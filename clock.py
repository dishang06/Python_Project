import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    root.after(1000, update_time)  # Update time every second (1000 milliseconds)

# Create the main application window
root = tk.Tk()
root.title("Simple Clock")

# Create a label to display the time
label = tk.Label(root, font=("Helvetica", 50), bg="white")
label.pack(pady=20)

# Start the clock
update_time()

# Run the application
root.mainloop()
