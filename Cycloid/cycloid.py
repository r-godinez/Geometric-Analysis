import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Slider, RadioButtons
from matplotlib.colors import BASE_COLORS

# Parameters for the cycloid
initial_radius = 2      # Initial radius of the circle generating the cycloid
num_frames = 500        # Number of frames in the animation
interval = 20           # Interval between frames in milliseconds
point_size = 8          # Initial point size
initial_speed = 1       # Initial speed of the rolling circle
initial_start = 0       # Starting position of the rolling circle
initial_end = 8 * np.pi # Ending position of the rolling circle
initial_stop = 4 * np.pi # Default stopping position for the small circle
initial_big_circle_start = 0 # Default starting position of the big circle

# Predefined color choices
colors = list(BASE_COLORS.keys())
initial_line_color = 'b'
initial_point_color = 'r'

# Set up the figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(left=0.1, bottom=0.45)  # Adjust to make space for sliders and buttons
ax.set_aspect('equal')
ax.set_xlim(initial_start, initial_end)
ax.set_ylim(0, 5)

# Initialize the line and point objects for the animation
line, = ax.plot([], [], initial_line_color + '-', lw=2)
point, = ax.plot([], [], initial_point_color + 'o', markersize=point_size)

# Cycloid function that calculates the position
def cycloid(t, radius, x_shift=0):
    x = radius * (t - np.sin(t)) + x_shift
    y = radius * (1 - np.cos(t))
    return x, y

# Initialization function to set up the background of the animation
def init():
    line.set_data([], [])
    point.set_data([], [])
    return line, point

# Animation function that updates each frame
def update(frame):
    radius = radius_slider.val  # Get the updated radius from the slider
    speed = speed_slider.val    # Get the rolling speed
    start = start_slider.val    # Starting position of the cycloid
    end = end_slider.val        # Ending position of the cycloid
    stop = stop_slider.val      # Stopping point for the small circle
    big_circle_start = big_circle_start_slider.val  # Starting position of the big circle

    ax.set_xlim(start, end)     # Update axis limits

    t_vals = np.linspace(0, frame / 20 * speed, 500)
    x_vals, y_vals = cycloid(t_vals, radius, x_shift=big_circle_start)

    # Update the line (full cycloid trace)
    line.set_data(x_vals, y_vals)

    # Determine the time when the small circle should stop moving
    if frame / 20 * speed <= stop:
        x_point, y_point = cycloid(frame / 20 * speed, radius, x_shift=big_circle_start)
    else:
        # After the stop point, keep the small circle at its last position
        x_point, y_point = cycloid(stop, radius, x_shift=big_circle_start)
    
    point.set_data([x_point], [y_point])

    # Update the size and colors
    point.set_markersize(point_size_slider.val)
    line.set_color(line_color_dropdown.value_selected)
    point.set_color(point_color_dropdown.value_selected)

    return line, point

# Create the animation
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=interval)

# Sliders for circle radius, point size, speed, positions, and big circle start
ax_radius = plt.axes([0.2, 0.3, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_point_size = plt.axes([0.2, 0.25, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_speed = plt.axes([0.2, 0.2, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_start = plt.axes([0.2, 0.15, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_end = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_stop = plt.axes([0.2, 0.05, 0.65, 0.03], facecolor='lightgoldenrodyellow')
ax_big_circle_start = plt.axes([0.2, 0.01, 0.65, 0.03], facecolor='lightgoldenrodyellow')

radius_slider = Slider(ax_radius, 'Radius', 0.1, 5.0, valinit=initial_radius)
point_size_slider = Slider(ax_point_size, 'Point Size', 1, 20, valinit=point_size)
speed_slider = Slider(ax_speed, 'Speed', 0.1, 5.0, valinit=initial_speed)
start_slider = Slider(ax_start, 'Start Pos', 0, 10 * np.pi, valinit=initial_start)
end_slider = Slider(ax_end, 'End Pos', 0, 10 * np.pi, valinit=initial_end)
stop_slider = Slider(ax_stop, 'Stop Time', 0, 10 * np.pi, valinit=initial_stop)
big_circle_start_slider = Slider(ax_big_circle_start, 'Big Circle Start', -10 * np.pi, 10 * np.pi, valinit=initial_big_circle_start)

# Dropdowns for color selection
ax_line_color = plt.axes([0.85, 0.2, 0.1, 0.15])
ax_point_color = plt.axes([0.85, 0.05, 0.1, 0.15])

# Add radio buttons for color selection
line_color_dropdown = RadioButtons(ax_line_color, colors, active=colors.index(initial_line_color))
point_color_dropdown = RadioButtons(ax_point_color, colors, active=colors.index(initial_point_color))

# Show the plot
plt.show()
