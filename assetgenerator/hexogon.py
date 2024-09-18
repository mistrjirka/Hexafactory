import matplotlib.pyplot as plt
import numpy as np

def create_hexagon_with_perpendicular_lines(file_path, line_distance):
    # Define the hexagon points
    angles = np.linspace(0, 2 * np.pi, 7)  # 6 sides + closing the hexagon
    hexagon_width = 950  # Desired width of the hexagon in pixels
    radius = hexagon_width / 2  # Calculate the radius to have flat top

    x_hexagon = radius * np.cos(angles)
    y_hexagon = radius * np.sin(angles)

    # Create the plot
    fig, ax = plt.subplots(figsize=(10.24, 10.24), dpi=100)  # Size 1024x1024 pixels
    ax.plot(x_hexagon, y_hexagon, color='white', linewidth=2)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.axis('off')

    # Draw two lines perpendicular to each of the six sides of the hexagon
    for i in range(6):  # Loop through all six sides
        # Determine the starting and ending points of the chosen side
        x_start, x_end = x_hexagon[i], x_hexagon[i+1]
        y_start, y_end = y_hexagon[i], y_hexagon[i+1]

        # Calculate the slope of the side and its perpendicular slope
        dx, dy = x_end - x_start, y_end - y_start
        perp_slope = -dx / dy  # Perpendicular slope

        # Determine two points along the side where lines will be drawn
        # Use fractions to determine how far along the side the lines will cross
        for fraction in [1/4, 3/4]:
            line_intersection_x = x_start + fraction * dx
            line_intersection_y = y_start + fraction * dy

            # Draw the two lines at the specified distance
            line_x1 = line_intersection_x + line_distance * np.cos(np.arctan(perp_slope))
            line_y1 = line_intersection_y + line_distance * np.sin(np.arctan(perp_slope))
            line_x2 = line_intersection_x - line_distance * np.cos(np.arctan(perp_slope))
            line_y2 = line_intersection_y - line_distance * np.sin(np.arctan(perp_slope))

            # Plot the perpendicular lines
            ax.plot([line_x1, line_x2], [line_y1, line_y2], color='white', linewidth=2)

    # Set the limits to ensure the hexagon is centered and has the correct size
    ax.set_xlim(-512, 512)
    ax.set_ylim(-512, 512)

    # Save as PNG with the correct size
    plt.savefig(file_path, dpi=100, bbox_inches='tight', pad_inches=0, facecolor='black')
    plt.close()

# Example usage
# Adjust 'line_distance' to set the distance of the lines from the point they cross the hexagon
create_hexagon_with_perpendicular_lines('hexagon_with_perpendicular_lines.png', line_distance=5)

