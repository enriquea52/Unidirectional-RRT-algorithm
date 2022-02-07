#!/usr/bin/env python3

import numpy as np
from matplotlib import pyplot as plt
from PIL import Image
import sys

import rrt
import visualization


if __name__ == "__main__":

    # Retrieve information from the command line ################################################## 
    if len(sys.argv) !=9:
        print("You should provide the path to the csv environment: ")
        print("Provide the correct number of arguments (8) in the following format as str: ")
        print("Path to env_X.csv (where X is the environment number), step, p, qstart_x, qstart_y, qgoal_x, qgoal_y")
        exit()
    else:
        path_env = sys.argv[1]
        K = int(sys.argv[2])
        step = int(sys.argv[3])
        p = float(sys.argv[4])
        qstart_x = int(sys.argv[5])
        qstart_y = int(sys.argv[6])
        qgoal_x = int(sys.argv[7])
        qgoal_y = int(sys.argv[8])

    print("Specified environment: ", path_env,"Step size: ", step,"Probability to choose qgoal",p,"qstart (",qstart_x,qstart_y,") qgoal (",qgoal_x,qgoal_y,") \n")
    #################################################################################################




    # Load grid map
    image = Image.open(path_env).convert('L')
    grid_map = np.array(image.getdata()).reshape(image.size[0], image.size[1])/255
    # binarize the image
    grid_map[grid_map > 0.5] = 1
    grid_map[grid_map <= 0.5] = 0
    # Invert colors to make 0 -> free and 1 -> occupied
    grid_map = (grid_map * -1) + 1
    # Show grid map
    plt.matshow(grid_map)
    plt.colorbar()

    start = [qstart_y,qstart_x] # Define start node
    goal = [qgoal_y,qgoal_x]    # Define goal node
    path_planner = rrt.path_planning(grid_map,start, goal, probability = p, step_q = step) # Define path_planning object
    V, E, iterations = path_planner.build(start, K)                                        # Built the tree using the RRT algorithm


    if len(V) != 0:

        # Retrieve the path of the tree
        
        print("Path Found in: ", iterations, " Iterations")
        visualization.Draw_Tree(V, E, goal, start)
        path = path_planner.fill_path()                                            
        print("Path: ", path, "\nTotal Distance: ",path_planner.total_distance(path))
        visualization.Draw_Path(path)
        plt.title('RRT Path Found')


        # Draw smooth path
        
        plt.matshow(grid_map)
        plt.colorbar()
        visualization.Draw_Tree(V, E, goal, start)
        smooth = path_planner.smooth_path()                                         
        print("Smooth Path: ", smooth, "\nTotal distance: ",path_planner.total_distance(smooth))
        visualization.Draw_Path(smooth, is_smooth = True)
        plt.title('RRT Smooth Path Found')



plt.show()
