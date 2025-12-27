# 🧠 MCP Simulation Code Debugger

A Python-based **Model Context Protocol (MCP)** server that simulates step-by-step code execution and performs automated debugging analysis using **Claude Desktop**.

This project demonstrates how to build **stateful MCP servers in Python**, expose tools to Claude, and reason about execution behavior like a debugger.

---

## 🚀 Project Status

**Current milestone:** ✅ Day 2 Complete  
**Next milestone:** Day 3 – Variable tracking & loop detection

---

## ✨ Features (Implemented)

- ✅ Python MCP server using `FastMCP`
- 🔁 Step-based simulation engine (abstract execution model)
- 🪲 Debug analyzer for execution state
- 🤖 Claude-accessible MCP tools:
  - `ping`
  - `run_simulation_step`
  - `analyze_simulation`
- 🖥 Fully tested with Claude Desktop on Windows
- 🧪 Local testing via VS Code terminal

---

## 🧠 Conceptual Model

This project models **abstract code execution**, similar to:
- Stepping through code in a debugger
- Symbolic execution
- Execution trace analysis

Each simulation step represents:
- One logical execution tick
- One debugger-style “step forward”
