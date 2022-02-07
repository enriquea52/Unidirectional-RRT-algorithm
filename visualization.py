from matplotlib import pyplot as plt


def Draw_Tree(V, E, goal, start):

    plt.scatter(V[:,0],V[:,1],linewidths=0.1, c = "red",marker = '.')           # Draw the nodes of the tree

    for e in E.keys():                                                          # Draw the edges of the tree
        plt.plot([e[0],E[e][0]],[e[1],E[e][1]],linewidth=0.5, color = "white")
        plt.draw()

    plt.scatter(start[0],start[1],linewidths=0.1, c = "green",zorder=10,label='Start node')        # Draw the start node
    plt.scatter(goal[0],goal[1],linewidths=0.1, c = "blue",zorder=10,label='Goal node')         # Draw the goal node


def Draw_Path(path,is_smooth = False):
    if is_smooth:
        for x in range(0,len(path)-1):                                              # Draw smooth path
            plt.plot([path[x][0],path[x+1][0]],[path[x][1],path[x+1][1]], color = "lightblue", linewidth = 2)
    else:
        for x in range(0,len(path)-1):                                              # Draw the path found following the parent nodes from the goal node until the start goal
            plt.plot([path[x][0],path[x+1][0]],[path[x][1],path[x+1][1]], color = "yellow")
