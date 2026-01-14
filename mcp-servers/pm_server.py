#!/usr/bin/env python3
"""
Project Manager MCP Server

Provides orchestration tools for the PM agent to manage multi-agent workflows.
Uses the official MCP SDK (mcp).

Install: pip install mcp
"""

import json
import logging
from datetime import datetime
from pathlib import Path
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("pm_server")

# State file for project data
STATE_FILE = Path(".context/pm_state.json")


def load_state() -> dict[str, Any]:
    """Load project state from file."""
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {
        "project_name": None,
        "current_iteration": None,
        "current_phase": None,
        "tasks": [],
        "context_transfers": [],
        "created_at": None,
    }


def save_state(state: dict[str, Any]) -> None:
    """Save project state to file."""
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, default=str))


# Create server instance
server = Server("project-manager")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available PM orchestration tools."""
    return [
        Tool(
            name="get_project_status",
            description="Get the current project status including iteration, phase, and active tasks.",
            inputSchema={
                "type": "object",
                "properties": {},
                "required": [],
            },
        ),
        Tool(
            name="initialize_project",
            description="Initialize a new project with the given name.",
            inputSchema={
                "type": "object",
                "properties": {
                    "project_name": {
                        "type": "string",
                        "description": "Name of the project to initialize",
                    }
                },
                "required": ["project_name"],
            },
        ),
        Tool(
            name="assign_task",
            description="Assign a task to a specific agent.",
            inputSchema={
                "type": "object",
                "properties": {
                    "agent": {
                        "type": "string",
                        "description": "Agent identifier (e.g., 'RE', 'AN', 'AR', 'BD')",
                    },
                    "task_description": {
                        "type": "string",
                        "description": "Description of the task to assign",
                    },
                    "priority": {
                        "type": "string",
                        "enum": ["HIGH", "MEDIUM", "LOW"],
                        "description": "Task priority",
                    },
                },
                "required": ["agent", "task_description"],
            },
        ),
        Tool(
            name="pass_context",
            description="Transfer context/output from one agent to another.",
            inputSchema={
                "type": "object",
                "properties": {
                    "from_agent": {
                        "type": "string",
                        "description": "Source agent identifier",
                    },
                    "to_agent": {
                        "type": "string",
                        "description": "Target agent identifier",
                    },
                    "context_summary": {
                        "type": "string",
                        "description": "Summary of the context being transferred",
                    },
                    "artifact_path": {
                        "type": "string",
                        "description": "Optional path to artifact file",
                    },
                },
                "required": ["from_agent", "to_agent", "context_summary"],
            },
        ),
        Tool(
            name="update_iteration",
            description="Update the current iteration and phase.",
            inputSchema={
                "type": "object",
                "properties": {
                    "iteration": {
                        "type": "integer",
                        "description": "Iteration number (1=Planning, 2=Development, 3=Verification)",
                    },
                    "phase": {
                        "type": "string",
                        "description": "Current phase within iteration",
                    },
                },
                "required": ["iteration", "phase"],
            },
        ),
        Tool(
            name="complete_task",
            description="Mark a task as complete.",
            inputSchema={
                "type": "object",
                "properties": {
                    "task_id": {
                        "type": "string",
                        "description": "ID of the task to complete",
                    },
                    "output_summary": {
                        "type": "string",
                        "description": "Summary of task output/deliverables",
                    },
                },
                "required": ["task_id", "output_summary"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> list[TextContent]:
    """Handle tool calls."""
    state = load_state()

    if name == "get_project_status":
        return [TextContent(type="text", text=json.dumps(state, indent=2, default=str))]

    elif name == "initialize_project":
        state = {
            "project_name": arguments["project_name"],
            "current_iteration": 0,
            "current_phase": "initialization",
            "tasks": [],
            "context_transfers": [],
            "created_at": datetime.now().isoformat(),
        }
        save_state(state)
        return [TextContent(
            type="text",
            text=f"Project '{arguments['project_name']}' initialized successfully."
        )]

    elif name == "assign_task":
        task_id = f"TASK-{len(state['tasks']) + 1:03d}"
        task = {
            "id": task_id,
            "agent": arguments["agent"],
            "description": arguments["task_description"],
            "priority": arguments.get("priority", "MEDIUM"),
            "status": "assigned",
            "assigned_at": datetime.now().isoformat(),
        }
        state["tasks"].append(task)
        save_state(state)
        return [TextContent(
            type="text",
            text=f"Task {task_id} assigned to {arguments['agent']}: {arguments['task_description']}"
        )]

    elif name == "pass_context":
        transfer = {
            "from": arguments["from_agent"],
            "to": arguments["to_agent"],
            "summary": arguments["context_summary"],
            "artifact": arguments.get("artifact_path"),
            "transferred_at": datetime.now().isoformat(),
        }
        state["context_transfers"].append(transfer)
        save_state(state)
        return [TextContent(
            type="text",
            text=f"Context passed from {arguments['from_agent']} to {arguments['to_agent']}"
        )]

    elif name == "update_iteration":
        iteration_names = {1: "Planning", 2: "Development", 3: "Verification"}
        state["current_iteration"] = arguments["iteration"]
        state["current_phase"] = arguments["phase"]
        save_state(state)
        iter_name = iteration_names.get(arguments["iteration"], f"Iteration {arguments['iteration']}")
        return [TextContent(
            type="text",
            text=f"Updated to {iter_name} - Phase: {arguments['phase']}"
        )]

    elif name == "complete_task":
        for task in state["tasks"]:
            if task["id"] == arguments["task_id"]:
                task["status"] = "complete"
                task["output"] = arguments["output_summary"]
                task["completed_at"] = datetime.now().isoformat()
                save_state(state)
                return [TextContent(
                    type="text",
                    text=f"Task {arguments['task_id']} marked complete."
                )]
        return [TextContent(type="text", text=f"Task {arguments['task_id']} not found.")]

    return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def main():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
