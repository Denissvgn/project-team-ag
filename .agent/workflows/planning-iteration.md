---
description: Execute Planning iteration (Iteration 1) - Research, Analysis, Architecture, Design
---

# Planning Iteration Workflow

## Trigger
Use after project initialization or when starting a new development cycle.

## Goal
Produce detailed plans and architecture for implementation.

## Steps

### Step 1: Research Phase
PM activates `research-engineer` skill.

```
Action: @skill research-engineer
Input: Vision, scope, technology questions
Output: Research Report
```

**RE deliverables:**
- Technology recommendations
- Codebase analysis (if existing)
- Feasibility assessment
- Competitive analysis

### Step 2: Analysis Phase
PM passes RE output to `analyst` skill.

```
Action: @skill analyst
Input: Research Report + Vision
Output: Requirements, User Stories
```

**AN deliverables:**
- Functional Requirements (FR-001, FR-002, ...)
- Non-Functional Requirements (NFR-001, ...)
- User Stories with Acceptance Criteria
- Priority rankings

### Step 3: Architecture & Design (Parallel)
PM activates both skills, potentially in parallel.

#### Step 3a: Architecture
```
Action: @skill architect
Input: Requirements from AN
Output: Architecture documentation
```

**AR deliverables:**
- Architecture Decision Records (ADRs)
- System Design Document
- API Contracts
- Database Schema

#### Step 3b: Design
```
Action: @skill designer
Input: Requirements from AN, Architecture constraints
Output: Design specifications
```

**DS deliverables:**
- UI/UX Specifications
- Component designs
- Interaction flows
- Visual style guide

### Step 4: Quality Gate
PM runs validation before proceeding.

#### Step 4a: Architecture Validation
```
Action: @skill critic
Input: Architecture + Requirements
Output: Validation Report
```

#### Step 4b: Security Review
```
Action: @skill security-advisor
Input: Architecture
Output: Security Risk Assessment
```

**Decision Point:**
- ❌ **Issues Found (HIGH/MEDIUM)**: Return to Step 3 with feedback
- ✅ **Approved**: Proceed to Step 5

### Step 5: Create Development Tasks
PM generates detailed task breakdown for Development iteration.

```
Action: @mcp gantt-tools create_tasks
Input: Architecture, Requirements, Estimates
Output: Development task list with dependencies
```

### Step 6: Update Timeline
PM updates Gantt chart with actual planning completion.

```
Action: @mcp gantt-tools update_task
Input: Planning iteration status
Output: Updated timeline
```

## Outputs
- ✅ Research Report
- ✅ Requirements Document
- ✅ User Stories
- ✅ Architecture Documentation
- ✅ Design Specifications
- ✅ CR & SA Approval
- ✅ Development task breakdown

## Next Step
→ `/workflow development-iteration`
