# Multi-Agent SDLC System for Google Antigravity

This project implements a multi-agent development orchestration system designed for the Google Antigravity IDE platform.

## System Architecture

The system uses a hierarchical agent structure:
- **PM (Project Manager)**: Central orchestrator
- **PO (Product Owner)**: Vision and scope management
- **Planning Team**: RE, AN, AR, DS
- **Development Team**: FD, BD, DO, TW
- **Quality Control**: QA, SA, CR, MA

## Directory Structure

```
.antigravity/
├── mcp_config.json      # MCP server connections
└── settings.json        # Security policies

.agent/
├── rules/               # Global and project rules
│   ├── GEMINI.md        # Core principles
│   └── git-flow.md      # Version control rules
├── skills/              # 14 agent skills
│   ├── pm-orchestrator/
│   ├── product-owner/
│   └── ...
└── workflows/           # Iteration workflows
    ├── initialization.md
    ├── planning-iteration.md
    ├── development-iteration.md
    └── verification-iteration.md

.context/                # Knowledge and state
├── templates/           # Document templates
└── pm_state.json        # PM state (auto-managed)

mcp-servers/             # Custom MCP servers
├── pm_server.py         # PM orchestration tools
└── gantt_server.py      # Timeline management
```

## Workflow Cycle

1. **Initialization**: User request → PO creates Vision → User approves
2. **Planning (Iteration 1)**: RE → AN → AR/DS → CR/SA validation
3. **Development (Iteration 2)**: FD/BD/DO → SA → TW → MA merge
4. **Verification (Iteration 3)**: QA → CR → PO vision check → Decision

## Key Rules

- **Main branch is READ-ONLY** for all agents except Merge Agent
- **All work in feature branches**: `feature/[iteration]-[agent]-[description]`
- **Security approval required** before merge (risk != HIGH/MEDIUM)

## MCP Servers

Install dependencies:
```bash
pip install mcp
```

Servers are configured in `.antigravity/mcp_config.json`.

## Invocation

Use slash commands in Antigravity:
- `/workflow initialization` - Start new project
- `/workflow planning-iteration` - Run planning phase
- `/workflow development-iteration` - Run development phase
- `/workflow verification-iteration` - Run verification phase

Or invoke skills directly:
- `@skill pm-orchestrator` - Activate PM agent
- `@skill backend-dev` - Activate backend developer
