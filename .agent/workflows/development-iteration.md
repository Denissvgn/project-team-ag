---
description: Execute Development iteration (Iteration 2) - Coding, Security, Docs, Merge
---

# Development Iteration Workflow

## Trigger
Use after completing Planning iteration.

## Goal
Implement features according to architecture and design.

## Branch Strategy
All development work happens in feature branches:
```
feature/<iteration>-<agent>-<description>
```

## Steps

### Step 1: Development Tasks (Parallel)
PM assigns tasks to development agents based on dependencies.

#### Step 1a: Backend Development
```
Action: @skill backend-dev
Input: Architecture, API contracts, Requirements
Branch: feature/dev-[N]-bd-[task]
Output: Backend code
```

#### Step 1b: Frontend Development  
```
Action: @skill frontend-dev
Input: Design specs, API contracts, Requirements
Branch: feature/dev-[N]-fd-[task]
Output: Frontend code
```

#### Step 1c: DevOps Setup
```
Action: @skill devops
Input: Architecture, deployment requirements
Branch: feature/dev-[N]-do-[task]
Output: CI/CD, infrastructure config
```

**Parallel Execution:**
- FD, BD, DO can work simultaneously on independent tasks
- PM monitors progress and handles blockers
- Dependencies are respected (e.g., BD API needed before FD integration)

### Step 2: Security Review (Per Feature)
After each feature is coded, PM triggers security review.

```
Action: @skill security-advisor
Input: Feature branch code
Output: Security Report with Risk Level
```

**Decision Point:**
- ❌ **Risk == HIGH or MEDIUM**: Return code to developer with SA feedback
- ✅ **Risk == LOW or NONE**: Proceed to Step 3

### Step 3: Documentation
After code is security-approved, PM triggers documentation.

```
Action: @skill tech-writer
Input: Approved code, Requirements, Architecture
Output: Updated documentation
```

**TW deliverables:**
- Updated README
- API documentation
- Code comments (if needed)
- User guide updates

### Step 4: Merge to Main
PM triggers merge for approved features.

```
Action: @skill merge-agent
Input: Feature branch (approved by SA, documented by TW)
Output: Code merged to main
```

**MA Checklist:**
- [ ] SA approval confirmed
- [ ] Tests passing (if applicable at this stage)
- [ ] Documentation updated
- [ ] No merge conflicts

### Step 5: Repeat for All Tasks
PM iterates through all development tasks:
1. Assign task to developer
2. Review with SA
3. Document with TW
4. Merge with MA

### Step 6: Development Complete
When all tasks are merged:

```
Action: @mcp gantt-tools update_iteration
Input: Development iteration complete
Output: Updated timeline
```

## Outputs
- ✅ All feature branches created
- ✅ All code security-approved
- ✅ All documentation updated
- ✅ All features merged to main
- ✅ CI/CD pipeline configured

## Next Step
→ `/workflow verification-iteration`
