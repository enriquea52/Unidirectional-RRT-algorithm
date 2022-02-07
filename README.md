# Unidirectional RRT path planning algorithm

The present code is an implementation of the Rapidly exploring Random Tree (RRT) algorithm for path planning. A probabilistaclly complete algorithm, that although it doesn't find the shortest path it can find a feasible path from a starting pose to a goal.

The code implementation has a CLI to execute it as follows.

`python main.py map_X.png K step p qstart_x qstart_y qgoal_x qgoal_y`  where **X** is the grid_map number, **K** is the maximum number of iterations allowed for the algorithm to run,**step** is the step size used for extending the tree, **p** is a probability of appearing the goal node as **q_rand** and then the initial position **(qstart_x,qstart_y)** and the goal position **(qgoal_x,qgoal_y)**.  Some execution examples are using the following commands. The code implementation shows two images, one with the original path generated from the algorithm (yellow), the tree branches are shown in white, the tree leaves are shown as red circles and the smooth path is shown in light blue.


### Open Environment

`python main.py environments/map7.png 10000 10 0.2 270 120 274 257`

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=18wQOA7sXhFMuymc6HC69-6h3hgSWJYvO" width="300" height="300" />
<img src="https://drive.google.com/uc?export=view&id=1ojDFeFiE7tG2SwOgIYh-0y0iGNNcLEyX" width="300" height="300" />
</p>

```
Path Found in:  133  Iterations
270 120 274 257
Non-smooth path
Total Distance:  332.9026862765278
Smooth Path:  [[120, 270], [185, 176], [258, 214], [257, 274]]
Total distance:  256.5913030275865
```



### Labyrinth Environment

`python main.py environments/map6.png 10000 10 0.2 49 451 250 250`

<p align="center">
<img src="https://drive.google.com/uc?export=view&id=12u76z5IONymCgRz31dX-Ig8D2dHcGwIb" width="300" height="300" />
<img src="https://drive.google.com/uc?export=view&id=1WqAKuCISK7Qn-QgbRt7dAvwCQVlEb0Qw" width="300" height="300" />
</p>



```
Path Found in:  5068  Iterations
49 451 250 250
Non-smooth path
Total Distance:  1261.442008103167
Smooth Path:  [[49, 451], [138, 412], [145, 426], [235, 458], [286, 447], [389, 307], [399, 219], [226, 159], [175, 238], [187, 320], [260, 342], [293, 321], [273, 280], [250, 250]]
Total distance:  1081.6814813674596

```


