import time
import math
from DrivingModule import CarController
from pathfinding import a_star_search, find_nearest_node, NODE_COORDS

def calculate_heading(current_node, next_node):
    
    #Calculate the heading angle (in degrees) from the current node to the next node.
    (x1, y1) = NODE_COORDS[current_node]
    (x2, y2) = NODE_COORDS[next_node]
    angle = math.degrees(math.atan2(y2 - y1, x2 - x1))
    return angle

def turn_to_heading(car, target_angle):
    """
    Turn the car towards the target angle.
    For simplicity, this demo uses the car's turn functions.
    You might need to integrate sensor feedback for precise control.
    """
    # decide whether to use turn_right or turn_left based on the sign of the angle.
    if target_angle >= 0:
        car.turn_right(speed=30, angle=target_angle)
    else:
        car.turn_left(speed=30, angle=target_angle)
    # Simulate the time needed to complete the turn.
    time.sleep(1)

def drive_to_node(car, current_node, next_node):
    """
    Drives the car from the current node to the next node.
    """
    
    # Calculate heading between nodes.
    heading = calculate_heading(current_node, next_node)
    print(f"Turning to heading {heading:.2f}° from {current_node} to {next_node}")
    
    # Turn towards the target heading.
    turn_to_heading(car, heading)
    
    # Start moving forward.
    car.move_forward(speed=30)
    
    # Estimate travel time based on the Euclidean distance between nodes.
    (x1, y1) = NODE_COORDS[current_node]
    (x2, y2) = NODE_COORDS[next_node]
    distance = math.hypot(x2 - x1, y2 - y1)
    
    # Adjust the travel time factor based on your car's speed.
    travel_time = distance / 50.0  # This factor may need tuning.
    print(f"Driving for {travel_time:.2f} seconds to reach {next_node}")
    time.sleep(travel_time)
    
    # Stop the car at the node.
    car.stop()
    time.sleep(0.5)

def traverse_path(car, path):
    """
    Traverses the full path by driving from one node to the next.
    """
    
    print("Starting node traversal...")
    for i in range(len(path) - 1):
        current_node = path[i]
        next_node = path[i + 1]
        drive_to_node(car, current_node, next_node)
    print("Traversal complete!")

"""
Possible Initialization of Function below:
"""
def main():
    # Initialize the car.
    from picarx import PicarX
    picarx = PicarX()
    car = CarController(picarx)
    
    # Define starting node and destination coordinates.
    start_node = "PondsideAve.:QuackSt"
    destination_x, destination_y = 585, 135
    
    # Determine the nearest node to the destination.
    goal_node = find_nearest_node(destination_x, destination_y)
    print(f"Destination node: {goal_node}")
    
    # Compute the optimal path using A* search.
    path = a_star_search(start_node, goal_node)
    if not path:
        print("No valid path found.")
        return
    
    print("Computed path:", " -> ".join(path))
    
    # Traverse the path.
    traverse_path(car, path)

if __name__ == "__main__":
    main()
