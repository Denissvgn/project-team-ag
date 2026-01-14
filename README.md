# Multi-Agent SDLC Orchestration for Antigravity

A powerful, orchestrated multi-agent development environment designed for the Google Antigravity IDE. This system automates the Software Development Life Cycle (SDLC) through a team of 14 specialized AI agents, custom MCP servers, and structured workflows.

## 🚀 Overview

This framework transforms development into a multi-agent assembly line. It handles everything from initial product visioning to final security audits and merging, ensuring high-quality, predictable, and secure code generation.

### Key Features
- **14 Specialized Agents**: Each with a distinct role (PM, PO, Architect, Security, etc.).
- **3-Phase SDLC**: Automated Planning, Development, and Verification iterations.
- **MCP-Powered Orchestration**: Custom servers manage project state and Gantt-style scheduling.
- **Git-Flow Enforcement**: Autonomous branch management and protection rules.
- **Antigravity Native**: Deeply integrated into the Antigravity workspace structure.

---

## 🏗️ The Agent Team

| Agent | Role | Expertise |
| :--- | :--- | :--- |
| **PM** | Project Manager | Central orchestrator, task distribution, and scheduling. |
| **PO** | Product Owner | Vision management, scope definition, and backlog validation. |
| **RE** | Research Engineer | Investigation, technical discovery, and feasibility studies. |
| **AN** | Analyst | Requirements engineering and user story creation. |
| **AR** | Architect | System design, ADRs, and API contracts. |
| **DS** | Designer | UI/UX design, mockups, and interaction flows. |
| **FD** | Frontend Dev | Client-side implementation (React, Vue, HTML/CSS). |
| **BD** | Backend Dev | Server-side logic, APIs, and database design. |
| **DO** | DevOps | CI/CD, infrastructure-as-code, and deployments. |
| **TW** | Tech Writer | Documentation, READMEs, and user guides. |
| **QA** | Test Engineer | Automated testing and quality assurance. |
| **SA** | Security Advisor | Vulnerability analysis and risk assessment. |
| **CR** | Critic | Artifact validation and quality review. |
| **MA** | Merge Agent | Exclusive write access to main branch. |

---

## 🔄 Workflows

The system follows a rigorous 3-iteration cycle:

### 1. Planning Iteration
- **Research**: Tech stack evaluation and feasibility study.
- **Analysis**: Requirements definition and user stories.
- **Design**: Architecture design (AR) and UI/UX design (DS).
- **Quality Gate**: Security (SA) and Architecture (CR) review.

### 2. Development Iteration
- **Implementation**: Parallel development by FD, BD, and DO agents.
- **Documentation**: Real-time documentation updates by TW.
- **Security Audit**: In-progress security review of the codebase.
- **Merge**: Automated merging of approved feature branches.

### 3. Verification Iteration
- **QA Testing**: End-to-end and unit testing.
- **Coverage Check**: Validation of test results against requirements.
- **Vision Check**: Product Owner confirms implementation matches vision.

---

## 🛠️ Usage

### Initialization
To start a new project or feature set:
```bash
/workflow initialization
```

### Planning
To begin the technical design phase:
```bash
/workflow planning-iteration
```

### Development
To kick off the coding iteration:
```bash
/workflow development-iteration
```

### Verification
To run tests and finalize the cycle:
```bash
/workflow verification-iteration
```

---

## ⚙️ Configuration

- **Agents**: Configured in `.agent/skills/`
- **MCP Servers**: Core logic in `mcp-servers/` (PM & Gantt servers)
- **Rules**: Global behavior defined in `.agent/rules/GEMINI.md`
- **IDE Settings**: Integration via `.antigravity/mcp_config.json`

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
