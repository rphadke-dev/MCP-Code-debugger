# Simulation Code Debugger (MCP)

A stateful **Model Context Protocol (MCP)** server written in Python that simulates code execution step-by-step and analyzes execution history to detect logical and runtime issues (e.g. division by zero, deep call stacks).

This project is designed as an **AI-assisted debugging backend** that Claude Desktop can interact with via MCP tools.

---

## 🚀 Features

- ✅ Stateful simulation engine (persists across tool calls)
- ✅ Step-by-step execution of operations
- ✅ Execution history tracking
- ✅ Automated issue detection (e.g. division by zero)
- ✅ MCP tool interface compatible with Claude Desktop
- ✅ Fully written in Python

---

## 🧠 Architecture Overview

flowchart TD
    Claude[Claude / MCP Client]

    Claude -->|MCP Tools| Server[server.py]

    Server --> Engine[simulation/engine.py]
    Engine --> History[simulation/history.py]
    History --> State[simulation/state.py]

    History --> Trace[debugger/trace.py]
    Trace --> Heuristics[debugger/heuristics.py]
    Heuristics --> Analyzer[debugger/analyzer.py]
    Analyzer --> Report[debugger/report.py]

    Report --> Types[common/types.py]

### Key Design Principle

> **The `SimulationEngine` is instantiated once at server startup and persists across all MCP tool calls**, enabling multi-step simulation and history-based analysis.

This is critical for correct MCP behavior.

---

## 🛠 MCP Tools

### `ping`
Health check to verify server connectivity.

---

### `run_simulation_step`

Simulates one execution step.

**Parameters**
```json
{
  "variables": { "a": 10, "b": 2 },
  "operation": "a / b"
}