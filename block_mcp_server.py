"""
MCP Server for Block Sequence Application

This server exposes the block manipulation functions to Claude via MCP protocol.
"""

import asyncio
import threading
from mcp.server.models import InitializationOptions
import mcp.types as types
from mcp.server import NotificationOptions, Server
import mcp.server.stdio

# Import the GUI application
from block_sequence_app import BlockSequenceApp

# Global app instance
app_instance = None

# Create MCP server
server = Server("block-sequence-server")

def start_gui_thread():
    """Start the GUI in a separate thread"""
    global app_instance
    app_instance = BlockSequenceApp()
    app_instance.run()

# Start GUI in background thread when server starts
gui_thread = threading.Thread(target=start_gui_thread, daemon=True)
gui_thread.start()

# Wait for app to initialize
import time
time.sleep(1)

@server.list_tools()
async def handle_list_tools() -> list[types.Tool]:
    """List all available tools for block manipulation"""
    return [
        types.Tool(
            name="swap_blocks",
            description="Swap two blocks at specified positions (0-4)",
            inputSchema={
                "type": "object",
                "properties": {
                    "pos1": {
                        "type": "integer",
                        "description": "First position (0-4)",
                        "minimum": 0,
                        "maximum": 4
                    },
                    "pos2": {
                        "type": "integer",
                        "description": "Second position (0-4)",
                        "minimum": 0,
                        "maximum": 4
                    }
                },
                "required": ["pos1", "pos2"]
            }
        ),
        types.Tool(
            name="set_block_color",
            description="Change the color of a block at a specific position",
            inputSchema={
                "type": "object",
                "properties": {
                    "pos": {
                        "type": "integer",
                        "description": "Position (0-4)",
                        "minimum": 0,
                        "maximum": 4
                    },
                    "color": {
                        "type": "string",
                        "description": "Color name",
                        "enum": ["blue", "green", "red", "yellow", "purple", "gray"]
                    }
                },
                "required": ["pos", "color"]
            }
        ),
        types.Tool(
            name="rotate_left",
            description="Rotate the entire sequence one position to the left",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        types.Tool(
            name="rotate_right",
            description="Rotate the entire sequence one position to the right",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        types.Tool(
            name="reverse_sequence",
            description="Reverse the order of all blocks in the sequence",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        types.Tool(
            name="set_block_at_position",
            description="Set a specific block type (A-E) at a given position",
            inputSchema={
                "type": "object",
                "properties": {
                    "pos": {
                        "type": "integer",
                        "description": "Position (0-4)",
                        "minimum": 0,
                        "maximum": 4
                    },
                    "block_type": {
                        "type": "string",
                        "description": "Block type letter",
                        "enum": ["A", "B", "C", "D", "E"]
                    }
                },
                "required": ["pos", "block_type"]
            }
        ),
        types.Tool(
            name="get_current_sequence",
            description="Get the current state of the block sequence and validation status",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        ),
        types.Tool(
            name="set_to_pattern",
            description="Reset the sequence to the valid pattern (A->B->C->D->E)",
            inputSchema={
                "type": "object",
                "properties": {}
            }
        )
    ]

@server.call_tool()
async def handle_call_tool(
    name: str, arguments: dict | None
) -> list[types.TextContent]:
    """Handle tool execution"""
    global app_instance
    
    if app_instance is None:
        return [types.TextContent(
            type="text",
            text="Error: Application not initialized"
        )]
    
    try:
        result = ""
        
        if name == "swap_blocks":
            result = app_instance.swap_blocks(arguments["pos1"], arguments["pos2"])
        
        elif name == "set_block_color":
            result = app_instance.set_block_color(arguments["pos"], arguments["color"])
        
        elif name == "rotate_left":
            result = app_instance.rotate_left()
        
        elif name == "rotate_right":
            result = app_instance.rotate_right()
        
        elif name == "reverse_sequence":
            result = app_instance.reverse_sequence()
        
        elif name == "set_block_at_position":
            result = app_instance.set_block_at_position(arguments["pos"], arguments["block_type"])
        
        elif name == "get_current_sequence":
            result = app_instance.get_current_sequence()
        
        elif name == "set_to_pattern":
            result = app_instance.set_to_pattern()
        
        else:
            result = f"Unknown tool: {name}"
        
        return [types.TextContent(type="text", text=result)]
    
    except Exception as e:
        return [types.TextContent(
            type="text",
            text=f"Error executing {name}: {str(e)}"
        )]

async def main():
    """Main entry point for the MCP server"""
    async with mcp.server.stdio.stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            InitializationOptions(
                server_name="block-sequence",
                server_version="0.1.0",
                capabilities=server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                )
            )
        )

if __name__ == "__main__":
    asyncio.run(main())
