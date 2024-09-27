import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import colorchooser

def plot_lemniscate(a, color):
    """
    Plots the Lemniscate of Bernoulli based on the parameter 'a' and the selected color.

    Parameters:
    a (float): The parameter that controls the size of the lemniscate.
    color (str): The color of the lemniscate curve.

    Returns:
    None
    """
    theta = np.linspace(0, 2 * np.pi, 1000)
    
    # Lemniscate equation in polar coordinates r = sqrt(a^2 * cos(2 * theta))
    r = np.sqrt(a**2 * np.cos(2 * theta))
    
    # Remove complex values (where cos(2*theta) < 0)
    r = np.nan_to_num(r, nan=0.0)
    
    # Convert to Cartesian coordinates
    x = r * np.cos(theta)
    y = r * np.sin(theta)
    
    # Clear the previous plot and draw a new one
    ax.clear()
    ax.plot(x, y, color=color, label=f'Lemniscate (a={a})')
    ax.set_aspect('equal', 'box')
    ax.grid(True)
    ax.set_title(f'Lemniscate with a={a}')
    canvas.draw()

def update_plot():
    """
    Updates the plot based on the current value of 'a' and the selected color.
    """
    a = float(a_scale.get())  # Get the value of 'a' from the scale
    plot_lemniscate(a, selected_color[0])

def choose_color():
    """
    Opens a color chooser dialog and updates the color of the lemniscate.
    """
    color = colorchooser.askcolor()[1]
    if color:
        selected_color[0] = color  # Update the color
        update_plot()  # Re-plot with the new color

# Set up the main application window
root = tk.Tk()
root.title("Lemniscate Plotter")

# Create a Matplotlib figure and axis
fig, ax = plt.subplots(figsize=(5, 5))

# Create a canvas to display the Matplotlib figure inside the Tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# Default parameters
selected_color = ['blue']  # Default color is blue

# Create a frame for the controls (slider and color button)
control_frame = tk.Frame(root)
control_frame.pack(side=tk.BOTTOM, fill=tk.X)

# Add a slider to control the parameter 'a'
a_label = tk.Label(control_frame, text="Parameter a:")
a_label.pack(side=tk.LEFT, padx=10)

a_scale = tk.Scale(control_frame, from_=0.5, to=5.0, resolution=0.1, orient=tk.HORIZONTAL, command=lambda x: update_plot())
a_scale.set(1.0)  # Set default value of 'a'
a_scale.pack(side=tk.LEFT, padx=10)

# Add a button to choose the color
color_button = tk.Button(control_frame, text="Choose Color", command=choose_color)
color_button.pack(side=tk.LEFT, padx=10)

# Initialize the plot with default values
plot_lemniscate(1.0, 'blue')

# Start the Tkinter event loop
root.mainloop()
