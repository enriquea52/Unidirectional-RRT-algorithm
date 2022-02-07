import numpy as np


class path_planning:

    def __init__(self,map, start, goal, probability , step_q ):

        self.map = map                  # Loading grid map to be used
        self.start = start              # Setting Start Node
        self.goal = goal                # Setting Goal Node
        self.step = step_q              # Tree growing step
        self.V = np.array([start])      # Set of tree vertexes
        self.E = {}                     # Set of tree edges
        self.t = 5                      # Goal reaching Threshold
        self.Path=[]                    # Array storing the path steps
        self.probability = probability  # Probability for the goal node to appear as qrand

    def build(self, q0, n): # Function to build the tree

        for i in range(0,n):
            qrand = self.rand_conf(self.map.shape[0], self.probability, self.goal) 
            self.extend(qrand)
            if self.V[-1][0] == self.goal[0] and self.V[-1][1] == self.goal[1]:
                print("Solution found")
                return self.V, self.E,i             # Return the set of tree vertexes, edges and the number of iterations used to find the solution.
        print("No solution found, iterate again!")
        return [],[],0


    def rand_conf(self,size_map, p, goal): # Function to retrieve a random configuration, the goal configuration appears with probability p
        if np.random.random_sample() < p:
            qrand = goal
        else:
            qrand = np.random.randint(size_map, size=(1, 2)).flatten()
        return qrand




    def extend(self, qrand): # Function to add new leaves to the tree by growing towards the qrand node by a specific step size
        # This function also calls the is_collision_free function to ensure that no node falls inside an obstacle of the environment.

        distances = np.sqrt(np.power(self.V[:,0] - qrand[0],2) + np.power(self.V[:,1] - qrand[1],2))
        qnear = self.V[np.argmin(distances)]
        if  np.min(distances) == 0.:
            return
        qnew = self.step*(qrand - qnear)/ np.sqrt(np.sum(np.power(qrand - qnear,[2,2]))) 
        qnew = qnew.astype(int) + qnear
        if np.sqrt((qnew[0]-self.goal[0])**2 + (qnew[1] - self.goal[1])**2) < self.t:
            qnew = self.goal
        qnew = np.clip(qnew, 0, self.map.shape[0]-1)
        if self.is_collision_free(qnear, qnew) and self.map[qnew[1],qnew[0]] != 0.5:
            self.V = np.append(self.V, [qnew],axis = 0)
            self.E[tuple(qnew)] = tuple(qnear)
            self.map[qnew[1],qnew[0]] = 0.5



    def is_collision_free(self,qnear, qnew,divisor = 7):        
        # Function to check if there is an obstacle between two nodes ()
        # Create a set of points (7 points for this example) from qnear to qnew to check if any of those 7 points intersect an obstacle
        # If there is an intersection return False otherwise an edge can connect vertex qnear with qnew, and thus grow the tree.
        magnitude = np.sqrt(np.sum(np.power(qnew - qnear,[2,2]))) 
        direction = (qnew - qnear) / magnitude
        check =  np.array([ i*(magnitude/divisor)*direction for i in range(1,divisor+1)]) 
        check = check.astype(int) + qnear
        check = np.clip(check, 0, self.map.shape[0]-1)
        if 1. in self.map[check[:,1],check[:,0]]:
            return False
        else:
            return True


    def fill_path(self): # Function to retrieve the path from the goal to the start nodes, by going to the parent nodes each time until reaching the starting node
        self.Path = [tuple(self.goal)]
        current = self.Path[-1]
        i = 0
        while not(current[0] == self.start[0] and current[1] == self.start[1]):
            self.Path.append(self.E[current])
            current = tuple(self.E[current])
            i+=1


        return self.Path[::-1]


    def smooth_path(self): # Function to smooth the path found
        smooth = [self.start]
        while not(smooth[-1][0] == self.goal[0] and smooth[-1][1] == self.goal[1]):
            for i in range(0,len(self.Path)):
                if self.is_collision_free(np.array(smooth[-1]),self.Path[i],divisor = 200):
                    smooth.append(list(self.Path[i]))
                    break
        return smooth


    def total_distance(self, path): # Retrieve the total distance of the path found (from the starting node to the goal node)
        total = 0
        for i in range(0, len(path)-1):
            total = total + np.sqrt((path[i][0] - path[i+1][0])**2 + (path[i][1] - path[i+1][1])**2)
        return total

        

                    


    
            

    
    


