# Block Sequence Application - Setup Guide

## Installation

### 1. Install Python Dependencies

```bash
pip install customtkinter mcp
```

### 2. File Structure

```
block-sequence/
├── block_sequence_app.py    # GUI Application
├── mcp_server.py            # MCP Server
├── mcp_config.json          # MCP Configuration (see below)
└── README.md
```

### 3. Create MCP Configuration

Create `mcp_config.json` in your Claude Desktop config directory:

**macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`  
**Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "block-sequence": {
      "command": "python",
      "args": ["/path/to/your/mcp_server.py"]
    }
  }
}
```

Replace `/path/to/your/` with the actual path to your `mcp_server.py` file.

## Usage

### Running Standalone (GUI only)

```bash
python block_sequence_app.py
```

This opens the GUI where you can manually manipulate blocks using buttons.

### Running with MCP (Claude Integration)

1. Configure MCP as shown above
2. Restart Claude Desktop
3. The GUI will launch automatically when Claude uses any tool
4. Claude can now control the blocks via natural language

## Available Functions (MCP Tools)

1. **swap_blocks(pos1, pos2)** - Swap two blocks
2. **set_block_color(pos, color)** - Change block color (blue, green, red, yellow, purple, gray)
3. **rotate_left()** - Rotate sequence left
4. **rotate_right()** - Rotate sequence right
5. **reverse_sequence()** - Reverse the order
6. **set_block_at_position(pos, block_type)** - Set specific block (A-E) at position
7. **get_current_sequence()** - Get current state and validation status
8. **set_to_pattern()** - Reset to valid pattern (A→B→C→D→E)

## Example Claude Commands

Once MCP is configured, you can ask Claude:

- "Show me the current block sequence"
- "Swap blocks at positions 0 and 2"
- "Rotate the sequence left twice"
- "Set position 3 to green"
- "Reverse the entire sequence"
- "Can you arrange the blocks to spell EDCBA?"
- "Try different combinations until you find the valid pattern"

## Valid Pattern

The application validates when blocks are in order: **A → B → C → D → E**

When this pattern is achieved, the status shows "✓ Valid Combination!" in green.

## Troubleshooting

**GUI doesn't appear**: Make sure `customtkinter` is installed
**MCP not working**: Check the path in `claude_desktop_config.json` is absolute
**Import errors**: Ensure both files are in the same directory
**Permission issues**: Make sure Python has permission to run on your system

## Extending the Application

To add more manipulation functions:

1. Add method to `BlockSequenceApp` class
2. Add corresponding tool definition in `handle_list_tools()`
3. Add handler case in `handle_call_tool()`

The pattern checking logic can be customized in the `valid_pattern` attribute and `check_pattern()` method.
