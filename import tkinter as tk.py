import tkinter as tk

# Create a dictionary to keep track of the state of each square
square_states = {}

# Team "Save" starts first
current_team = "Save"

def on_click(row, col):
    global current_team  # To modify the global team variable
    
    # Get the selected letter (S or O) from the radio button selection
    selected_letter = letter_choice.get()

    # Check if the square is already full
    if square_states[(row, col)] == "full":
        status_label.config(text=f"Square ({row}, {col}) is already full")
    else:
        # Mark the square as full and update the button text
        square_states[(row, col)] = "full"
        buttons[(row, col)].config(text=selected_letter)

        # Display which team placed the letter
        status_label.config(text=f"{current_team} placed '{selected_letter}' at ({row}, {col})")

        # Switch turns between Save and Souls
        if current_team == "Save":
            current_team = "Souls"
        else:
            current_team = "Save"

        # Update the label to show the current turn
        turn_label.config(text=f"Current turn: {current_team}")

# Create the main window
root = tk.Tk()
root.title("SOS Game - Save vs Souls")

# Set the grid size
rows, cols = 10, 10

# Create a dictionary to store button references
buttons = {}

# Create a variable to hold the selected letter (S or O)
letter_choice = tk.StringVar(value="S")  # Default choice is "S"

# Create radio buttons for choosing between "S" and "O"
tk.Label(root, text="Choose letter:").grid(row=0, column=0, columnspan=2)

s_radio = tk.Radiobutton(root, text="S", variable=letter_choice, value="S")
s_radio.grid(row=1, column=0)

o_radio = tk.Radiobutton(root, text="O", variable=letter_choice, value="O")
o_radio.grid(row=1, column=1)

# Create the grid of buttons
for row in range(2, rows+2):  # Adjust row index to fit radio buttons
    for col in range(cols):
        # Initialize each square as empty
        square_states[(row-2, col)] = "empty"
        
        # Create a button for each square
        button = tk.Button(root, text="", 
                           command=lambda r=row-2, c=col: on_click(r, c),
                           width=10, height=3)
        button.grid(row=row, column=col, padx=5, pady=5)
        
        # Store the button reference in the dictionary
        buttons[(row-2, col)] = button

# Add a styled label to display messages
status_label = tk.Label(root, text="Click a square to fill it", 
                        font=("Helvetica", 14, "bold"),   # Larger, bold font
                        bg="lightblue",                   # Background color
                        fg="darkblue",                    # Text color
                        pady=10,                          # Vertical padding
                        padx=10,                          # Horizontal padding
                        borderwidth=2,                    # Border width
                        relief="groove")                  # Border style

status_label.grid(row=rows+2, column=0, columnspan=cols, pady=20)

# Add a label to show the current team's turn
turn_label = tk.Label(root, text=f"Current turn: {current_team}",
                      font=("Helvetica", 12, "bold"),
                      bg="lightgrey",
                      fg="black",
                      pady=5)
turn_label.grid(row=rows+3, column=0, columnspan=cols, pady=10)

# Start the Tkinter event loop
root.mainloop()
