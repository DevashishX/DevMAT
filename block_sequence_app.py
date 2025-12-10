import customtkinter as ctk
from typing import List

class BlockSequenceApp:
    def __init__(self):
        # Initialize application
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.root = ctk.CTk()
        self.root.title("Block Sequence Application")
        self.root.geometry("900x500")
        
        # Block data
        self.blocks = ['A', 'B', 'C', 'D', 'E'] # correspond sequentially to color_map
        self.colors = ['#3b82f6', '#3b82f6', '#3b82f6', '#3b82f6', '#3b82f6']  # blue
        self.valid_pattern = [['A', 'B', 'C', 'D', 'E']]
        
        # Color options - Map each block letter to a color
        self.color_map = {
            'A': '#3b82f6',  # blue
            'B': "#22c5c5",  # teal
            'C': '#eab308',  # yellow
            'D': '#a855f7',  # purple
            'E': '#22c55e'   # green
        }
        
        # GUI elements
        self.block_labels = []
        self.dropdowns = []
        self.status_label = None
        
        self._setup_gui()
        self.update_display()
        
    def _setup_gui(self):
        # Main container
        main_frame = ctk.CTkFrame(self.root)
        main_frame.pack(pady=20, padx=20, fill="both", expand=True)
        
        # Title
        title = ctk.CTkLabel(main_frame, text="Block Sequence Manager", 
                            font=ctk.CTkFont(size=24, weight="bold"))
        title.pack(pady=(0, 20))
        
        # Block display frame
        block_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
        block_frame.pack(pady=20)
        
        # Create 5 blocks with arrows
        for i in range(5):
            # Block
            block = ctk.CTkLabel(block_frame, text=self.blocks[i],
                               width=100, height=100,
                               font=ctk.CTkFont(size=32, weight="bold"),
                               corner_radius=10)
            block.grid(row=0, column=i*2, padx=5)
            self.block_labels.append(block)
            
            # Arrow (except after last block)
            if i < 4:
                arrow = ctk.CTkLabel(block_frame, text="→",
                                   font=ctk.CTkFont(size=32),
                                   text_color="gray")
                arrow.grid(row=0, column=i*2+1, padx=5)
        
        # Status label
        self.status_label = ctk.CTkLabel(main_frame, text="Status: Waiting for sequence...",
                                        font=ctk.CTkFont(size=16),
                                        text_color="gray")
        self.status_label.pack(pady=20)
        
        # Control frame with dropdowns
        control_frame = ctk.CTkFrame(main_frame)
        control_frame.pack(pady=10)
        
        # Create 5 dropdown combos for setting blocks
        for i in range(5):
            # Container for each control
            control_container = ctk.CTkFrame(control_frame, fg_color="transparent")
            control_container.grid(row=0, column=i, padx=10, pady=5)
            
            # Label
            label = ctk.CTkLabel(control_container, text=f"Block {i+1}:",
                               font=ctk.CTkFont(size=12))
            label.pack()
            
            # Dropdown
            dropdown = ctk.CTkComboBox(control_container, 
                                      values=['A', 'B', 'C', 'D', 'E'],
                                      width=80,
                                      command=lambda value, pos=i: self.set_block_at_position(pos, value))
            dropdown.set(self.blocks[i])
            dropdown.pack(pady=5)
            self.dropdowns.append(dropdown)
        
    def update_display(self):
        """Update the visual display of blocks"""
        for i, label in enumerate(self.block_labels):
            block_type = self.blocks[i]
            block_color = self.color_map[block_type]
            label.configure(text=block_type, fg_color=block_color)
        
        # Update dropdowns to match current blocks
        for i, dropdown in enumerate(self.dropdowns):
            dropdown.set(self.blocks[i])
        
        self.check_pattern()
        
    def check_pattern(self) -> str:
        """Check if current sequence matches the valid pattern"""
        if self.blocks in self.valid_pattern:
            self.status_label.configure(text="✓ Valid Combination!",
                                       text_color="#22c55e")
            return "Valid Combination!"
        else:
            self.status_label.configure(text="Status: Invalid sequence",
                                       text_color="gray")
            return "Invalid sequence"
    
    # Core manipulation functions (to be exposed via MCP)
    
    def set_block_at_position(self, pos: int, block_type: str) -> str:
        """Set a specific block type at a position"""
        if 0 <= pos < 5 and block_type in ['A', 'B', 'C', 'D', 'E']:
            self.blocks[pos] = block_type
            self.update_display()
            return f"Set position {pos} to {block_type}. Current: {self.blocks}"
        return "Invalid position or block type"
    
    def set_block_color(self, pos: int, color: str) -> str:
        """Set color of block at position by changing its type"""
        # Map color names to block types
        color_to_block = {
            'blue': 'A',
            'teal': 'B',
            'yellow': 'C',
            'purple': 'D',
            'green': 'E'
        }
        if 0 <= pos < 5 and color in color_to_block:
            block_type = color_to_block[color]
            self.blocks[pos] = block_type
            self.update_display()
            return f"Set position {pos} to {block_type} ({color}). Current: {self.blocks}"
        return "Invalid position or color"
    
    def get_current_sequence(self) -> str:
        """Get the current sequence state"""
        status = self.check_pattern()
        return f"Current sequence: {self.blocks}. Status: {status}"
    
    def run(self):
        """Start the GUI application"""
        self.root.mainloop()


if __name__ == "__main__":
    app = BlockSequenceApp()
    app.run()