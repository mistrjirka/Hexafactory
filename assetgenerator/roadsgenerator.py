import matplotlib.pyplot as plt
import numpy as np

def create_hexagon_with_conveyor_belt_treads(file_path, line_distance, sides_to_connect, num_treads=15):
    # Define the hexagon points
    angles = np.linspace(0, 2 * np.pi, 7)  # 6 sides + closing the hexagon
    hexagon_width = 800  # Desired width of the hexagon in pixels
    radius = hexagon_width / 2  # Calculate the radius to have a flat top

    x_hexagon = radius * np.cos(angles)
    y_hexagon = radius * np.sin(angles)

    # Create the plot with a fixed size of 1024x1024 pixels
    fig = plt.figure(figsize=(1024/100, 1024/100), dpi=100)  # Size 1024x1024 pixels with dpi=100
    ax = fig.add_subplot(111)
    ax.plot(x_hexagon, y_hexagon, color='white', linewidth=2)
    ax.set_aspect('equal')
    ax.set_facecolor('black')
    ax.axis('off')

    # Store the intersection points for the specified sides
    intersection_points = []

    # Draw two lines perpendicular to the specified sides of the hexagon
    for side in sides_to_connect:  # Loop through the specified sides
        # Determine the starting and ending points of the chosen side
        x_start, x_end = x_hexagon[side], x_hexagon[side+1]
        y_start, y_end = y_hexagon[side], y_hexagon[side+1]

        # Calculate the direction vector of the side
        dx, dy = x_end - x_start, y_end - y_start
        length = np.sqrt(dx**2 + dy**2)
        dx /= length
        dy /= length

        # Determine two points along the side where lines will be drawn
        # Use fractions 1/4 and 3/4 to determine how far along the side the lines will cross
        side_points = []
        for fraction in [1/4, 3/4]:
            line_intersection_x = x_start + fraction * (x_end - x_start)
            line_intersection_y = y_start + fraction * (y_end - y_start)
            side_points.append((line_intersection_x, line_intersection_y))

            # Draw the two lines at the specified distance
            # Move in the perpendicular direction to ensure parallelism
            perp_dx, perp_dy = -dy, dx  # Perpendicular vector
            line_x1 = line_intersection_x + line_distance * perp_dx
            line_y1 = line_intersection_y + line_distance * perp_dy
            line_x2 = line_intersection_x - line_distance * perp_dx
            line_y2 = line_intersection_y - line_distance * perp_dy

            # Plot the perpendicular lines
            ax.plot([line_x1, line_x2], [line_y1, line_y2], color='white', linewidth=2)
        
        # Append the intersection points for creating the conveyor belt lines
        intersection_points.append(side_points)

    # Draw the conveyor belts (parallel lines) between specified intersection points
    if len(intersection_points) == 2:  # Ensure we have exactly two sides to connect
        # Conveyor belts: Connect the opposite fractions (1/4 to 3/4 and 3/4 to 1/4)
        belts = []
        for idx_pair in [(0, 1), (1, 0)]:
            start_point = intersection_points[0][idx_pair[0]]
            end_point = intersection_points[1][idx_pair[1]]
            
            # Draw the conveyor line
            ax.plot([start_point[0], end_point[0]], [start_point[1], end_point[1]], 
                    color='white', linewidth=2)
            
            belts.append((start_point, end_point))

        # Draw the treads on the conveyor line in the middle of the two lines
        for (start_1, end_1), (start_2, end_2) in zip(belts[::2], belts[1::2]):
            # Calculate midpoints for the treads along the conveyor lines
            for t in np.linspace(0, 1, num_treads):
                # Calculate the midpoint of the two parallel lines
                mid_x1 = start_1[0] + t * (end_1[0] - start_1[0])
                mid_y1 = start_1[1] + t * (end_1[1] - start_1[1])
                mid_x2 = start_2[0] + t * (end_2[0] - start_2[0])
                mid_y2 = start_2[1] + t * (end_2[1] - start_2[1])

                # Midpoint of the tread line
                tread_mid_x = (mid_x1 + mid_x2) / 2
                tread_mid_y = (mid_y1 + mid_y2) / 2

                # Direction vector for the tread lines
                dx = mid_x2 - mid_x1
                dy = mid_y2 - mid_y1
                tread_length = 20  # Length of each tread line

                # Draw the perpendicular tread line at the midpoint
                tread_x1 = tread_mid_x + tread_length / 2 * dy / np.sqrt(dx**2 + dy**2)
                tread_y1 = tread_mid_y - tread_length / 2 * dx / np.sqrt(dx**2 + dy**2)
                tread_x2 = tread_mid_x - tread_length / 2 * dy / np.sqrt(dx**2 + dy**2)
                tread_y2 = tread_mid_y + tread_length / 2 * dx / np.sqrt(dx**2 + dy**2)

                ax.plot([tread_x1, tread_x2], [tread_y1, tread_y2], color='white', linewidth=1)

    # Set the limits to ensure the hexagon is centered and has the correct size
    ax.set_xlim(-512, 512)
    ax.set_ylim(-512, 512)

    # Save as PNG with the correct size and resolution
    plt.savefig(file_path, dpi=100, bbox_inches='tight', pad_inches=0, facecolor='black')
    plt.close()

# Example usage
# Adjust 'line_distance' to set the distance of the lines from the point they cross the hexagon
# Specify which sides to connect, for example [0, 3] connects the top and bottom sides
create_hexagon_with_conveyor_belt_treads('hexagon_with_conveyor_belt_treads.png', line_distance=50, sides_to_connect=[0, 3])

