#!/usr/bin/env python3
"""
Gantt Chart MCP Server

Provides project timeline and scheduling tools.
Uses the official MCP SDK (mcp).

Install: pip install mcp
"""

import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("gantt_server")

# State file for Gantt data
STATE_FILE = Path(".context/gantt_state.json")


def load_state() -> dict[str, Any]:
    """Load Gantt state from file."""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {
        "project_name": None,
        "start_date": None,
        "tasks": [],
        "iterations": [],
    }


def save_state(state: dict[str, Any]) -> None:
    """Save Gantt state to file."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, default=str))


# Create server instance
server = Server("gantt-tools")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available Gantt tools."""
    return [
        Tool(
            name="create_project",
            description="Initialize a new project timeline with iterations.",
            inputSchema={
                "type": "object",
                "properties": {
                    "project_name": {
                        "type": "string",
                        "description": "Name of the project",
                    },
                    "start_date": {
                        "type": "string",
                        "description": "Project start date (YYYY-MM-DD)",
                    },
                },
                "required": ["project_name"],
            },
        ),
        Tool(
            name="create_task",
            description="Create a new task in the timeline.",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Task name",
                    },
                    "duration_hours": {
                        "type": "integer",
                        "description": "Estimated duration in hours",
                    },
                    "dependencies": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of task IDs this task depends on",
                    },
                    "assignee": {
                        "type": "string",
                        "description": "Agent assigned to this task",
                    },
                    "iteration": {
                        "type": "integer",
                        "description": "Iteration number (1, 2, or 3)",
                    },
                },
                "required": ["name", "duration_hours"],
            },
        ),
        Tool(
            name="update_task",
            description="Update a task's status or actual time.",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "ID of the task to update",
                    },
                    "status": {
                        "type": "string",
                        "enum": ["pending", "in_progress", "complete", "blocked"],
                        "description": "New status",
                    },
                    "actual_hours": {
                        "type": "integer",
                        "description": "Actual hours spent (if complete)",
                    },
                },
                "required": ["task_id", "status"],
            },
        ),
        Tool(
            name="shift_tasks",
            description="Shift dependent tasks when a task is delayed.",
            inputSchema={
                "type": "object",
                "properties": {
                    "from_task_id": {
                        "type": "string",
                        "description": "ID of the delayed task",
                    },
                    "delay_hours": {
                        "type": "integer",
                        "description": "Hours of delay to propagate",
                    },
                },
                "required": ["from_task_id", "delay_hours"],
            },
        ),
        Tool(
            name="get_timeline",
            description="Get the current project timeline as formatted text.",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        ),
        Tool(
            name="complete_iteration",
            description="Mark an iteration as complete.",
            inputSchema={
                "type": "object",
                "properties": {
                    "iteration": {
                        "type": "integer",
                        "description": "Iteration number to complete",
                    },
                },
                "required": ["iteration"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle tool calls."""
    state = load_state()

    if name == "create_project":
        start = arguments.get("start_date", datetime.now().strftime("%Y-%m-%d"))
        state = {
            "project_name": arguments["project_name"],
            "start_date": start,
            "tasks": [],
            "iterations": [
                {"number": 1, "name": "Planning", "status": "pending"},
                {"number": 2, "name": "Development", "status": "pending"},
                {"number": 3, "name": "Verification", "status": "pending"},
            ],
        }
        save_state(state)
        return [TextContent(
            type="text",
            text=f"Project '{arguments['project_name']}' timeline created. Start: {start}"
        )]

    elif name == "create_task":
        task_id = f"GT-{len(state['tasks']) + 1:03d}"
        task = {
            "id": task_id,
            "name": arguments["name"],
            "duration_hours": arguments["duration_hours"],
            "dependencies": arguments.get("dependencies", []),
            "assignee": arguments.get("assignee", "unassigned"),
            "iteration": arguments.get("iteration", 1),
            "status": "pending",
            "start_time": None,
            "end_time": None,
            "actual_hours": None,
        }
        state["tasks"].append(task)
        save_state(state)
        return [TextContent(
            type="text",
            text=f"Task {task_id} created: {arguments['name']} ({arguments['duration_hours']}h)"
        )]

    elif name == "update_task":
        for task in state["tasks"]:
            if task["id"] == arguments["task_id"]:
                task["status"] = arguments["status"]
                if arguments.get("actual_hours"):
                    task["actual_hours"] = arguments["actual_hours"]
                if arguments["status"] == "in_progress" and not task["start_time"]:
                    task["start_time"] = datetime.now().isoformat()
                if arguments["status"] == "complete":
                    task["end_time"] = datetime.now().isoformat()
                save_state(state)
                return [TextContent(
                    type="text",
                    text=f"Task {arguments['task_id']} updated to {arguments['status']}"
                )]
        return [TextContent(type="text", text=f"Task {arguments['task_id']} not found.")]

    elif name == "shift_tasks":
        # Find dependent tasks and shift them
        delayed_task_id = arguments["from_task_id"]
        delay = arguments["delay_hours"]
        affected = []

        for task in state["tasks"]:
            if delayed_task_id in task.get("dependencies", []):
                task["duration_hours"] += delay  # Simplified: extend duration
                affected.append(task["id"])

        save_state(state)
        return [TextContent(
            type="text",
            text=f"Shifted {len(affected)} tasks by {delay}h: {', '.join(affected)}"
        )]

    elif name == "get_timeline":
        lines = [f"# Project: {state.get('project_name', 'Unknown')}", ""]

        # Iterations overview
        lines.append("## Iterations")
        for it in state.get("iterations", []):
            status_icon = {"pending": "⏳", "in_progress": "🔄", "complete": "✅"}.get(
                it["status"], "❓"
            )
            lines.append(f"- {status_icon} Iteration {it['number']}: {it['name']} ({it['status']})")

        # Tasks by iteration
        lines.append("")
        lines.append("## Tasks")
        for it_num in [1, 2, 3]:
            it_tasks = [t for t in state.get("tasks", []) if t.get("iteration") == it_num]
            if it_tasks:
                lines.append(f"\n### Iteration {it_num}")
                for task in it_tasks:
                    status_icon = {
                        "pending": "⬜",
                        "in_progress": "🔵",
                        "complete": "✅",
                        "blocked": "🔴",
                    }.get(task["status"], "❓")
                    deps = f" (deps: {', '.join(task['dependencies'])})" if task["dependencies"] else ""
                    lines.append(
                        f"- {status_icon} [{task['id']}] {task['name']} "
                        f"({task['duration_hours']}h, {task['assignee']}){deps}"
                    )

        return [TextContent(type="text", text="\n".join(lines))]

    elif name == "complete_iteration":
        for it in state.get("iterations", []):
            if it["number"] == arguments["iteration"]:
                it["status"] = "complete"
                save_state(state)
                return [TextContent(
                    type="text",
                    text=f"Iteration {arguments['iteration']} marked complete."
                )]
        return [TextContent(type="text", text=f"Iteration {arguments['iteration']} not found.")]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
