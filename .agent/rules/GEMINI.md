# Global Agent Rules

## Activation
type: always-on

## Core Principles

1. **Hierarchy**: All agents operate under PM (Project Manager) orchestration
2. **Version Control**: Main branch is READ-ONLY except for Merge Agent
3. **Quality Gates**: All artifacts must pass validation before proceeding
4. **Context Passing**: PM manages context saturation between agents

## Agent Hierarchy

```
User (Human) → PM → [PO, RE, AN, AR, DS, FD, BD, DO, TW, QA, SA, CR, MA]
```

## Communication Rules

1. Agents report status to PM, not directly to User
2. PM aggregates status and presents to User at decision points
3. Only PM may request User input during active iterations

## Code Standards

1. All code must be fully typed (TypeScript, Python typing module)
2. Every function requires docstrings/JSDoc comments
3. Error handling must be explicit - no bare try/except
4. Logs must be structured and informative

## Security Rules

1. Never commit secrets, API keys, or credentials
2. Security Advisor must approve code before merge
3. Risk level HIGH or MEDIUM blocks merge

