import tkinter as tk
from tkinter import font

class ModernCalculator:
    """A modern, stylish calculator application using Tkinter."""

    # Color Palette
    BG_COLOR = "#1C1C1C"
    DISPLAY_BG_COLOR = "#1C1C1C"
    BUTTON_BG_COLOR = "#333333"
    OPERATOR_BG_COLOR = "#FF9500" # Orange for operators
    SPECIAL_BG_COLOR = "#A5A5A5" # Light gray for C, +/-, %
    TEXT_COLOR = "#FFFFFF"
    SPECIAL_TEXT_COLOR = "#000000"
    TOTAL_TEXT_COLOR = "#FFFFFF"
    ENTRY_TEXT_COLOR = "#B2B2B2"

    def __init__(self, master):
        self.master = master
        master.title("Modern Calculator")
        master.geometry("340x540")
        master.resizable(False, False)
        master.configure(bg=self.BG_COLOR)

        # --- State Variables ---
        self.expression = ""
        self.total = "0"

        # --- Fonts ---
        self.total_font = font.Font(family="Helvetica", size=48, weight="bold")
        self.entry_font = font.Font(family="Helvetica", size=20)
        self.button_font = font.Font(family="Helvetica", size=18, weight="bold")

        # --- Display Widgets ---
        self.total_text = tk.StringVar(value=self.total)
        self.entry_text = tk.StringVar(value="")
        self.create_display()

        # --- Button Widgets ---
        self.create_buttons()

    def create_display(self):
        """Creates the two-line display area."""
        display_frame = tk.Frame(self.master, bg=self.DISPLAY_BG_COLOR)
        display_frame.pack(expand=True, fill="both", padx=20, pady=(20, 0))

        # Label for the current expression/input
        entry_label = tk.Label(display_frame, textvariable=self.entry_text, font=self.entry_font,
                               bg=self.DISPLAY_BG_COLOR, fg=self.ENTRY_TEXT_COLOR, anchor="e")
        entry_label.pack(expand=True, fill="both")

        # Label for the total/result
        total_label = tk.Label(display_frame, textvariable=self.total_text, font=self.total_font,
                               bg=self.DISPLAY_BG_COLOR, fg=self.TOTAL_TEXT_COLOR, anchor="e")
        total_label.pack(expand=True, fill="both")

    def create_buttons(self):
        """Creates and lays out the calculator buttons in a grid."""
        button_frame = tk.Frame(self.master, bg=self.BG_COLOR)
        button_frame.pack(expand=True, fill="both", padx=10, pady=10)

        # Configure grid columns to have equal weight
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)

        # Button layout and properties
        buttons = [
            {'text': 'C', 'row': 0, 'col': 0, 'bg': self.SPECIAL_BG_COLOR, 'fg': self.SPECIAL_TEXT_COLOR, 'cmd': self.clear},
            {'text': '±', 'row': 0, 'col': 1, 'bg': self.SPECIAL_BG_COLOR, 'fg': self.SPECIAL_TEXT_COLOR, 'cmd': self.toggle_sign},
            {'text': '%', 'row': 0, 'col': 2, 'bg': self.SPECIAL_BG_COLOR, 'fg': self.SPECIAL_TEXT_COLOR, 'cmd': lambda: self.press('%')},
            {'text': '/', 'row': 0, 'col': 3, 'bg': self.OPERATOR_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('/')},
            {'text': '7', 'row': 1, 'col': 0, 'bg': self.BUTTON_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('7')},
            {'text': '8', 'row': 1, 'col': 1, 'bg': self.BUTTON_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('8')},
            {'text': '9', 'row': 1, 'col': 2, 'bg': self.BUTTON_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('9')},
            {'text': '×', 'row': 1, 'col': 3, 'bg': self.OPERATOR_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('*')},
            {'text': '4', 'row': 2, 'col': 0, 'bg': self.BUTTON_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('4')},
            {'text': '5', 'row': 2, 'col': 1, 'bg': self.BUTTON_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('5')},
            {'text': '6', 'row': 2, 'col': 2, 'bg': self.BUTTON_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('6')},
            {'text': '−', 'row': 2, 'col': 3, 'bg': self.OPERATOR_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('-')},
            {'text': '1', 'row': 3, 'col': 0, 'bg': self.BUTTON_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('1')},
            {'text': '2', 'row': 3, 'col': 1, 'bg': self.BUTTON_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('2')},
            {'text': '3', 'row': 3, 'col': 2, 'bg': self.BUTTON_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('3')},
            {'text': '+', 'row': 3, 'col': 3, 'bg': self.OPERATOR_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('+')},
            {'text': '0', 'row': 4, 'col': 0, 'bg': self.BUTTON_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('0'), 'span': 2},
            {'text': '.', 'row': 4, 'col': 2, 'bg': self.BUTTON_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': lambda: self.press('.')},
            {'text': '=', 'row': 4, 'col': 3, 'bg': self.OPERATOR_BG_COLOR, 'fg': self.TEXT_COLOR, 'cmd': self.evaluate}
        ]

        for btn in buttons:
            button = tk.Button(button_frame, text=btn['text'], font=self.button_font,
                               bg=btn['bg'], fg=btn['fg'], relief='flat', bd=0,
                               command=btn['cmd'])
            button.grid(row=btn['row'], column=btn['col'], columnspan=btn.get('span', 1),
                        sticky="nsew", padx=5, pady=5)

    # --- Button Logic Methods ---

    def press(self, key):
        """Appends the pressed key to the expression."""
        self.expression += str(key)
        self.entry_text.set(self.expression)

    def clear(self):
        """Clears the expression and resets the display."""
        self.expression = ""
        self.total = "0"
        self.entry_text.set("")
        self.total_text.set(self.total)

    def toggle_sign(self):
        """Toggles the sign of the current expression."""
        if self.expression and self.expression[0] == '-':
            self.expression = self.expression[1:]
        else:
            self.expression = '-' + self.expression
        self.entry_text.set(self.expression)

    def evaluate(self):
        """Evaluates the expression and shows the result."""
        try:
            # Replace display symbols with Python operators if needed
            expression_to_eval = self.expression.replace('%', '/100')
            result = str(eval(expression_to_eval))
            self.total = result
            self.expression = ""
        except (SyntaxError, ZeroDivisionError, TypeError):
            self.total = "Error"
            self.expression = ""
        finally:
            self.total_text.set(self.total)
            self.entry_text.set("")

# --- Main execution block ---
if __name__ == "__main__":
    root = tk.Tk()
    app = ModernCalculator(root)
    root.mainloop()