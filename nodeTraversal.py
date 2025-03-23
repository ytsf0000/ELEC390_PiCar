from globals import PATH_DATA
from pathfinding import a_star_search, find_nearest_node

class NodeTraversal:
    def __init__(self):
        pass  # No car integration for now

    def execute_path(self, start_node, dest_x, dest_y):
        """
        Finds the nearest node to (dest_x, dest_y), computes the path using A* search,
        and executes the movement instructions step by step.
        """
        # Find nearest destination node
        destination_node = find_nearest_node(dest_x, dest_y)
        print(f"🎯 Nearest node to ({dest_x}, {dest_y}) is: {destination_node}")

        # Get the path from start_node to destination_node
        path = a_star_search(start_node, destination_node)
        if not path or len(path) < 3:
            print("❌ No valid path found or path too short!")
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
                            print(f"➡️  {command.capitalize()} {value} units/degrees")
                        elif isinstance(step, str):
                            print(f"🛑 Special Instruction: {step}")
                    print("✅ Instruction sequence completed.\n")
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

# ✅ **Test the function**
if __name__ == "__main__":
    traversal = NodeTraversal()

    # Example: Start at 'PondsideAve.:QuackSt' and go to (585, 135)
    traversal.execute_path("PondsideAve.:QuackSt", 585, 135)
