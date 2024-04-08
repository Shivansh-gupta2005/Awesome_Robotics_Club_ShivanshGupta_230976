Path planning algorithm used by me is the A* algorithm.
I first converted the image into binary image and plotted it using matplotlib and then I sliced it using 2D array slicing.
I stored value 0 for yellow cell and 1 for blue cell and then stored these values in a 2D array.
Then I used the A* algorithm.
I started traversing the 2D array from top-left cell and the restriction was that we cannot go on blue cell.
Consider a square grid having many obstacles and we are given a starting cell and a target cell. We want to reach the target cell (if possible) from the starting cell as quickly as possible. Here A* Search Algorithm comes to the rescue.
What A* Search Algorithm does is that at each step it picks the node according to a value-‘f’ which is a parameter equal to the sum of two other parameters – ‘g’ and ‘h’. At each step it picks the node/cell having the lowest ‘f’, and process that node/cell.
We define ‘g’ and ‘h’ as simply as possible below
g = the movement cost to move from the starting point to a given square on the grid, following the path generated to get there. 
h = the estimated movement cost to move from that given square on the grid to the final destination. This is often referred to as the heuristic, which is nothing but a kind of smart guess. We really don’t know the actual distance until we find the path, because all sorts of things can be in the way (walls, water, etc.)
Using this approach, I traversed the array and printed the shortest path between top left cell and bottom right cell without moving on blue cell. I  assigned the coordinates of top left cell as (1,1) and bottom right as (5,5).
Then printed the shortest possible path.
