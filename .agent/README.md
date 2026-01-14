# Multi-Agent SDLC Orchestration for Antigravity

This directory contains the configuration for the multi-agent development system.

## Quick Start

1. **Initialize MCP Servers**: Ensure Python 3.10+ with `mcp` package installed
2. **Open in Antigravity**: The IDE will automatically detect `.antigravity/` config
3. **Start Project**: Use `/workflow initialization` to begin

## Agent Team

| Agent | Skill | Role |
|-------|-------|------|
| PM | `pm-orchestrator` | Central orchestrator |
| PO | `product-owner` | Vision management |
| RE | `research-engineer` | Investigation |
| AN | `analyst` | Requirements |
| AR | `architect` | System design |
| DS | `designer` | UI/UX |
| FD | `frontend-dev` | Frontend code |
| BD | `backend-dev` | Backend code |
| DO | `devops` | CI/CD |
| TW | `tech-writer` | Documentation |
| QA | `test-engineer` | Testing |
| SA | `security-advisor` | Security review |
| CR | `critic` | Validation |
| MA | `merge-agent` | Git merge (exclusive) |

## Workflows

- `initialization.md` - New project setup
- `planning-iteration.md` - Phase 1: Planning
- `development-iteration.md` - Phase 2: Development
- `verification-iteration.md` - Phase 3: Verification

## Rules

- `GEMINI.md` - Global agent behavior
- `git-flow.md` - Version control policy
