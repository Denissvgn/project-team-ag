# Git-Flow Branch Protection

## Activation
type: always-on

## Main Branch Policy

**All agents except `merge-agent` have READ-ONLY access to `main` branch.**

## Feature Branch Conventions

- All development work MUST be done in feature branches
- Branch naming pattern: `feature/[iteration]-[agent]-[description]`
- Examples:
  - `feature/plan-1-ar-architecture-design`
  - `feature/dev-2-bd-auth-api`
  - `feature/dev-2-fd-login-component`

## Merge Requirements

Before merge-agent can execute `git merge` to main:

1. ✅ Security Advisor approval (risk level != HIGH)
2. ✅ All automated tests passing
3. ✅ Documentation updated by Tech Writer
4. ✅ Code review by Critic (if applicable)

## Forbidden Commands (for non-MA agents)

```bash
git push origin main     # BLOCKED
git merge main           # BLOCKED
git push --force         # BLOCKED
```

## Allowed Commands (all agents)

```bash
git status
git diff
git checkout -b feature/...
git add .
git commit -m "..."
git push origin feature/...
```

