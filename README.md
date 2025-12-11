# DevMAT
Devs Manufacturing Automation Technology / Devs FertigungsAutomatisierungsTechnologie

## PCB Assembly Orchestrator

A visual orchestrator for PCB assembly processes with MCP (Model Context Protocol) integration for Claude Desktop.

## Features

- Visual workflow designer for PCB assembly sequences
- 5-step process orchestration with configurable parameters
- Real-time validation against predefined patterns
- MCP server integration for Claude Desktop interaction
- Two MCP implementations: standard and FastMCP

## Prerequisites

- Python 3.8 or higher
- customtkinter
- mcp (Model Context Protocol library)
- FastMCP (for the FastMCP server variant)

## Installation

1. **Clone or navigate to the project directory:**
   ```bash
   cd path/to/DevMAT
   ```

2. **Set up Python environment:**
   ```bash
   python -m venv .conda
   .conda/Scripts/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install customtkinter mcp fastmcp
   ```

## Running the GUI

Run the orchestrator GUI standalone:

```bash
python orchestrator_gui.py
```

## MCP Server Setup

This project provides two MCP server implementations for Claude Desktop integration:

### Standard MCP Server
Located in `orchestrator_mcp_server.py`

### FastMCP Server  
Located in `orchestrator_fastmcp_server.py` (recommended)

## Claude Desktop Configuration

Add the following to your Claude Desktop config file:

**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`  
**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Linux:** `~/.config/Claude/claude_desktop_config.json`

### Configuration Example

```json
{
  "mcpServers": {
    "orchestrator": {
      "command": "/path/to/DevMAT/.conda/python.exe",
      "args": [
        "/path/to/DevMAT/orchestrator_mcp_server.py"
      ],
      "cwd": "/path/to/DevMAT"
    },
    "orchestrator-fastmcp": {
      "command": "/path/to/DevMAT/.conda/python.exe",
      "args": [
        "/path/to/DevMAT/orchestrator_fastmcp_server.py"
      ],
      "cwd": "/path/to/DevMAT"
    }
  }
}
```

**Note:** You can enable one or both servers. Replace `/path/to/DevMAT` with your actual project path.

## Available MCP Tools

Once configured, Claude can interact with the orchestrator using these tools:

- `set_block_at_position` - Set block type at a specific position
- `set_sub_param_at_position` - Configure sub-parameters
- `get_current_sequence` - View current configuration
- `execute_sequence` - Execute valid sequences
- `get_current_pattern_validity` - Check sequence validity
- `get_valid_patterns` - List all valid patterns
- `get_block_sub_params` - Query valid parameters for blocks
- `set_pattern` - Quickly set to a predefined valid pattern

## Valid Process Processes

The orchestrator supports three predefined valid processes:

**Pattern 1:** Standard Lead-Free Process
- Solder Paste Application (lead-free)
- Component Placement (high-speed)
- Soldering (235C)
- Optical Inspection (2D)
- Functional Testing (in-circuit)

**Pattern 2:** High-Precision Leaded Process
- Solder Paste Application (leaded)
- Component Placement (high-precision)
- Soldering (245C)
- Optical Inspection (3D)
- Functional Testing (functional)

**Pattern 3:** Low-Temperature Flexible Process
- Solder Paste Application (low-temp)
- Component Placement (flexible)
- Soldering (260C)
- Optical Inspection (Automated)
- Functional Testing (boundary-scan)

## Usage with Claude

After setup, restart Claude Desktop. You can ask Claude to:
- "Show me the current orchestrator sequence"
- "Set the orchestrator to pattern 2"
- "Change step 3 to use 260C soldering"
- "Execute the current sequence"
- "What are the valid patterns?"


## Project Structure

```
DevMAT/
─ orchestrator_gui.py              # Main GUI application
─ orchestrator_mcp_server.py       # Standard MCP server
─ orchestrator_fastmcp_server.py   # FastMCP server implementation
─ README.md                        # README
─ .conda/                          # Python virtual environment (make your own)
```

## Troubleshooting

- Ensure Python paths in config are correct and use forward slashes or escaped backslashes
- Verify all dependencies are installed in the correct Python environment
- Check that the working directory (`cwd`) points to the DevMAT folder
- Restart Claude Desktop after configuration changes

## Feel free to contribute to the project
- Create an issue 
- Just open a pull request