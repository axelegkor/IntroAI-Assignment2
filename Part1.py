from Map import Map_Obj


def h(s, goal_pos):
    return (abs(goal_pos[0] - s[0])**2 + abs(goal_pos[1] - s[1])**2)**0.5


def find_path(map_obj: Map_Obj):
    open_list = []

    closed_list = []

    open_list.append([map_obj.get_start_pos(), []])

    while open_list:
        current = open_list.pop(0)
        currentNode = current[0]
        currentHistory = current[1]
        closed_list.append(currentNode)
        if currentNode == map_obj.get_goal_pos():
            currentHistory.append(currentNode)
            for i in currentHistory[1:len(currentHistory)-1]:
                map_obj.replace_map_values(i, 4, map_obj.get_goal_pos())
            return currentHistory
        for i in map_obj.get_walkable_neighbors(currentNode):
            if i not in closed_list:
                map_obj.replace_map_values(i, 2, map_obj.get_goal_pos())
                new = [i, currentHistory + [currentNode]]
                j = 0
                while j < len(open_list) and len(open_list[j][1]) + h(open_list[j][0], map_obj.get_goal_pos()) < len(new[1]) + h(new[0], map_obj.get_goal_pos()):
                    j += 1
                if j == len(open_list):
                    open_list.append(new)
                else:
                    open_list.append(open_list[len(open_list) - 1])
                    for k in range(len(open_list) - 1, j, -1):
                        open_list[k] = open_list[k - 1]
                    open_list[j] = new

    return None


# Task 1
map_obj_task1 = Map_Obj(1)
find_path(map_obj_task1)
map_obj_task1.show_map()

# Task 2
map_obj_task2 = Map_Obj(2)
find_path(map_obj_task2)
map_obj_task2.show_map()
