import tkinter as tk
import time

def update_time():
    current_time = time.strftime('%H:%M:%S')
    clock_label.config(text=current_time)
    root.after(1000, update_time)

# Create the main window
root = tk.Tk()
root.title("Digital Clock")
root.geometry("200x100")
root.resizable(False, False)

# Create a label to display the clock
clock_label = tk.Label(root, font=("Helvetica", 40), bg="black", fg="white")
clock_label.pack(fill="both", expand=True)

# Run the clock update function
update_time()

# Start the main event loop
root.mainloop()
