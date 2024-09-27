import numpy as np
import matplotlib.pyplot as plt

def plot_epicycloid(R, r, steps=1000):
    """
    Plots the epicycloid based on the radii of the fixed and rolling circles.

    Parameters:
    R (float): Radius of the fixed circle.
    r (float): Radius of the rolling circle.
    steps (int): Number of points used to plot the curve. Higher values result in smoother curves.

    Returns:
    None
    """
    # The range of t is extended to cover multiple full rotations
    t = np.linspace(0, 2 * np.pi * (R / r), steps)
    x = (R + r) * np.cos(t) - r * np.cos((R + r) / r * t)
    y = (R + r) * np.sin(t) - r * np.sin((R + r) / r * t)
    
    # Plot the curve
    plt.plot(x, y, label=f'Epicycloid (R={R}, r={r})')
    plt.gca().set_aspect('equal')
    plt.legend()
    plt.title(f'Epicycloid with R={R}, r={r}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

def plot_hypocycloid(R, r, steps=1000):
    """
    Plots the hypocycloid based on the radii of the fixed and rolling circles.

    Parameters:
    R (float): Radius of the fixed circle.
    r (float): Radius of the rolling circle.
    steps (int): Number of points used to plot the curve. Higher values result in smoother curves.

    Returns:
    None
    """
    # The range of t is extended to cover multiple full rotations
    t = np.linspace(0, 2 * np.pi * (R / r), steps)
    x = (R - r) * np.cos(t) + r * np.cos((R - r) / r * t)
    y = (R - r) * np.sin(t) - r * np.sin((R - r) / r * t)
    
    # Plot the curve
    plt.plot(x, y, label=f'Hypocycloid (R={R}, r={r})')
    plt.gca().set_aspect('equal')
    plt.legend()
    plt.title(f'Hypocycloid with R={R}, r={r}')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    # Get user input for the radii
    print("Epicycloid and Hypocycloid Plotting Program")
    
    try:
        # Input for the epicycloid
        R_epicycloid = float(input("Enter the radius of the fixed circle for the epicycloid (R): "))
        r_epicycloid = float(input("Enter the radius of the rolling circle for the epicycloid (r): "))
        plot_epicycloid(R_epicycloid, r_epicycloid)
        
        # Input for the hypocycloid
        R_hypocycloid = float(input("Enter the radius of the fixed circle for the hypocycloid (R): "))
        r_hypocycloid = float(input("Enter the radius of the rolling circle for the hypocycloid (r): "))
        plot_hypocycloid(R_hypocycloid, r_hypocycloid)
    
    except ValueError:
        print("Please enter valid numerical values for the radii.")
