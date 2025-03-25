from globals import PATH_DATA
from pathfinding import a_star_search, find_nearest_node
import ShortTerm
import ap
import io
import time

class NodeTraversal:
    def __init__(self):
        pass  # No car integration for now

    def transitionState(self,state):
        ShortTerm.stateTransition=False
        ShortTerm.CURRENT_STATE=state
        ShortTerm.stateStartIteration=0
        ShortTerm.relativeIteration=0

    def executeInstruction(self,instruction):
        command, value = instruction
        state=ShortTerm.State.Wait
        if(command=="straight"):
            state=ShortTerm.State.Forward
        elif(command=="turn_right"):
            state=ShortTerm.State.TurnR
        elif(command=="turn_left"):
            state=ShortTerm.State.TurnL
        elif(command=="wait"):
            state=ShortTerm.State.Wait
        
        self.transitionState(state)
        ShortTerm.value=value

        while(ShortTerm.stateTransition==False):
            # TODO update current position
            ShortTerm.iteration()
            continue



        return

    def execute_path(self, start_node, end_node):
        """
        Finds the nearest node to (dest_x, dest_y), computes the path using A* search,
        and executes the movement instructions step by step.
        """
        # Find nearest destination node
        #destination_node = find_nearest_node(dest_x, dest_y)
        #print(f"Nearest node to ({dest_x}, {dest_y}) is: {destination_node}")

        # Get the path from start_node to destination_node
        path = a_star_search(start_node, destination_node)
        if not path or len(path) < 3:
            print("No valid path found or path too short!")
            return
        
        print(f"\n🗺️  Generated Path: {' -> '.join(path)}\n")

        # Start traversal using the first node as the current node
        current_node = path[0]
        intersection_node = path[1]
        next_node = path[2]

        index = 0
        while index < len(path) - 2:
            if intersection_node not in PATH_DATA or "paths" not in PATH_DATA[intersection_node]:
                print(f"⚠️ No path data for {intersection_node}, skipping...")
            else:
                key = (current_node, next_node)
                if key in PATH_DATA[intersection_node]["paths"]:
                    movements = PATH_DATA[intersection_node]["paths"][key]
                    print(f"🚦 Moving from '{current_node}' to '{next_node}' via '{intersection_node}'")
                    for step in movements:
                        if isinstance(step, list) and len(step) == 2:
                            command, value = step
                            self.executeInstruction(step)
                            print(f"➡️  {command.capitalize()} {value} units/degrees")
                        elif isinstance(step, str):
                            print(f"Special Instruction: {step}")
                    print("Instruction sequence completed.\n")
                else:
                    print(f"⚠️ No movement instructions for {current_node} -> {next_node} via {intersection_node}, proceeding without instructions.")
            
            # Shift indices for next iteration
            index += 1
            if index + 2 < len(path):
                current_node = path[index]
                intersection_node = path[index + 1]
                next_node = path[index + 2]
            else:
                break
        self.transitionState(ShortTerm.State.Wait)
        ShortTerm.iteration()




# Test the function
if __name__ == "__main__":
    traversal = NodeTraversal()
    ShortTerm.init()

    start_fare = 1
    start_path = 0
    while(1):
        if(start_fare):
            fareStatus,fare=ap.get_fare()
            
            # Check if the specific substring is present
            if "Claim fare" == fareStatus:
                print("Collected Fare succesfully")
            else:
                time.sleep(0.5)
                continue

            start_end_points = ap.get_locations() #starxy, endxy
            start_car_loc = ap.get_current_loc() #x, y

            car_start_node = find_nearest_node(start_car_loc[0], start_car_loc[1])
            route_start_node = find_nearest_node(start_end_points[0], start_end_points[1])
            route_end_node = find_nearest_node(start_end_points[2], start_end_points[3])

            traversal.execute_path(car_start_node, route_start_node)

            start_fare = 0
            start_path = 1
        if(start_path):
            traversal.execute_path(route_start_node, route_end_node)

            start_path = 0
            start_fare = 1
        



