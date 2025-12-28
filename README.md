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

┌──────────────────────────────────────────────┐
│                  Claude / MCP Client         │
│                                              │
│  - ping                                      │
│  - run_simulation_step                       │
│  - analyze_simulation                        │
└───────────────────────┬──────────────────────┘
                        │ MCP (stdio)
                        ▼
┌──────────────────────────────────────────────┐
│                  server.py                   │
│                                              │
│  • Registers MCP tools                       │
│  • Orchestrates simulation & debugging       │
└───────────────┬──────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│          simulation/engine.py                │
│                                              │
│  • Executes symbolic operations              │
│  • Mutates simulation state                  │
│  • Records each step                         │
└───────────────┬──────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│         simulation/history.py                │
│                                              │
│  • Append-only history of states             │
│  • Acts as execution log                     │
└───────────────┬──────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│           simulation/state.py                │
│                                              │
│  • Snapshot of a single step                 │
│  • Variables, call stack, operation          │
└───────────────┬──────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│            debugger/trace.py                 │
│                                              │
│  • Converts history → structured trace       │
│  • Provides ordered, analyzable timeline     │
└───────────────┬──────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│         debugger/heuristics.py               │
│                                              │
│  • Rule-based issue detection                │
│  • Division by zero, deep stack, etc.        │
└───────────────┬──────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│          debugger/analyzer.py                │
│                                              │
│  • Orchestrates trace + heuristics           │
│  • Coordinates debugging pass                │
└───────────────┬──────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│           debugger/report.py                 │
│                                              │
│  • Human-readable debug report               │
│  • Issues, explanations, summary             │
└───────────────┬──────────────────────────────┘
                │
                ▼
┌──────────────────────────────────────────────┐
│            common/types.py                   │
│                                              │
│  • Shared domain models                      │
│  • Issue, TraceEvent, DebugResult, etc.      │
└──────────────────────────────────────────────┘

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