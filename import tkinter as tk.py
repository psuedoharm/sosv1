import tkinter as tk

# Create a dictionary to keep track of the state of each square
square_states = {}

def on_click(row, col):
    # Check if the square is already full
    if square_states[(row, col)] == "full":
        status_label.config(text=f"Square ({row}, {col}) is already full")
    else:
        # Mark the square as full and update the button text
        square_states[(row, col)] = "full"
        buttons[(row, col)].config(text="Full")
        status_label.config(text=f"Square ({row}, {col}) is now full")

# Create the main window
root = tk.Tk()
root.title("10x10 Grid of Buttons")

# Set the grid size
rows, cols = 10, 10

# Create a dictionary to store button references
buttons = {}

# Create the grid of buttons
for row in range(rows):
    for col in range(cols):
        # Initialize each square as empty
        square_states[(row, col)] = "empty"
        
        # Create a button for each square
        button = tk.Button(root, text="", 
                           command=lambda r=row, c=col: on_click(r, c),
                           width=10, height=3)
        button.grid(row=row, column=col, padx=5, pady=5)
        
        # Store the button reference in the dictionary
        buttons[(row, col)] = button

# Add a styled label to display messages
status_label = tk.Label(root, text="Click a square to fill it", 
                        font=("Helvetica", 14, "bold"),   # Larger, bold font
                        bg="lightblue",                   # Background color
                        fg="darkblue",                    # Text color
                        pady=10,                          # Vertical padding
                        padx=10,                          # Horizontal padding
                        borderwidth=2,                    # Border width
                        relief="groove")                  # Border style

status_label.grid(row=rows, column=0, columnspan=cols, pady=20)

# Start the Tkinter event loop
root.mainloop()



























"""""
import tkinter as tk


# Create a dictionary to keep track of the state of each square
square_states = {}

def on_click(row, col):
    # Check if the square is already full
    if square_states[(row, col)] == "full":
        print(f"Square ({row}, {col}) is already full")
    else:
        # Mark the square as full and update the button text
        square_states[(row, col)] = "full"
        buttons[(row, col)].config(text="Full")

# Create the main window
root = tk.Tk()
root.title("10x10 Grid of Buttons")

# Set the grid size
rows, cols = 10, 10

# Create a dictionary to store button references
buttons = {}

# Create the grid of buttons
for row in range(rows):
    for col in range(cols):
        # Initialize each square as empty
        square_states[(row, col)] = "empty"
        
        # Create a button for each square
        button = tk.Button(root, text="", 
                           command=lambda r=row, c=col: on_click(r, c),
                           width=10, height=3)
        button.grid(row=row, column=col, padx=5, pady=5)
        
        # Store the button reference in the dictionary
        buttons[(row, col)] = button

# Start the Tkinter event loop
root.mainloop()
"""











"""
def on_click(row, col):
    print(f"Button at ({row}, {col}) clicked")

# Create the main window
root = tk.Tk()
root.title("10x10 Grid of Buttons")

# Set the grid size
rows, cols = 10, 10

# Create the grid of buttons
for row in range(rows):
    for col in range(cols):
        button = tk.Button(root, text=f"({row},{col})", 
                           command=lambda r=row, c=col: on_click(r, c),
                           width=10, height=3)
        button.grid(row=row, column=col, padx=5, pady=5)

# Start the Tkinter event loop
root.mainloop()
"""


"""def on_click():
    label.config(text="Hello, Tkinter!")


    

# Create the main window
root = tk.Tk()
root.title("Simple GUI")

# Set window size
root.geometry("800x800")

# Create a label
label = tk.Label(root, text="Click the button to change this text")
label.pack(pady=20)

# Create a button
button = tk.Button(root, text="Click Me!", command=on_click)
button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()"""
