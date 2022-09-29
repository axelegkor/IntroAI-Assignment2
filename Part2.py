from Map import Map_Obj

# Function for calculation h(s), distance from s to goal


def h(s, goal_pos):
    return (abs(goal_pos[0] - s[0])**2 + abs(goal_pos[1] - s[1])**2)**0.5

# Function for calculation g(s), distance from start to s


def find_path(map_obj: Map_Obj):

    # Initialize the open list. This will be a list of list, with each list containing a node and the path to that node
    open_list = []

    # Initialize the closed list
    closed_list = []

    # Add the start node to the open list
    open_list.append([map_obj.get_start_pos(), [], 0])

    # Loop until the open list is empty
    while open_list:

        # Get the node with the lowest cost and the path to that node
        current = open_list.pop(0)

        # Get the node with the lowest cost
        currentNode = current[0]

        # Get the path to the node with the lowest cost
        currentHistory = current[1]

        # Get the cost to the node with the lowest cost
        currentCost = current[2]

        # Add the node with the lowest cost to the closed list
        closed_list.append(currentNode)

        # If-statement to check if the current node is the goal node
        if currentNode == map_obj.get_goal_pos():

            # Add the goal node to the path
            currentHistory.append(currentNode)

            # Set the color of all nodes along the path to orange
            for i in currentHistory[1:len(currentHistory)-1]:
                map_obj.replace_map_values(i, 6, map_obj.get_goal_pos())

            # Return the path
            return currentHistory

        # Get the walkable neighbors of the current node
        for i in map_obj.get_walkable_neighbors(currentNode):
            # Ignore nodes that are already in the closed list
            if i not in closed_list:

                # Create a list with the node, the path to that node and it's cost
                new = [i, currentHistory + [currentNode],
                       currentCost + map_obj.get_cell_value(currentNode)]

                # Add the list to the right place in the open list
                j = 0
                while j < len(open_list) and open_list[j][2] + h(open_list[j][0], map_obj.get_goal_pos()) < new[2] + h(new[0], map_obj.get_goal_pos()):
                    j += 1
                if j == len(open_list):
                    open_list.append(new)
                else:
                    open_list.append(open_list[len(open_list) - 1])
                    for k in range(len(open_list) - 1, j, -1):
                        open_list[k] = open_list[k - 1]
                    open_list[j] = new

    # If the open list is empty, and the goal node is not found, return None
    return None


# Task 3
map_obj_task3 = Map_Obj(3)
print("Solution-path task 3:", find_path(map_obj_task3))
map_obj_task3.show_map()

# Task 4
map_obj_task4 = Map_Obj(4)
print("Solution-path task 4:", find_path(map_obj_task4))
map_obj_task4.show_map()
