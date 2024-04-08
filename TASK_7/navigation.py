import cv2
import matplotlib.image as plt
import matplotlib.pyplot as pllt
import numpy as np
import heapq
from collections import deque
def a_star(grid, start, goal):
    def heuristic(a, b):
        return abs(a[0] - b[0]) + abs(a[1] - b[1])
    def reconstruct_path(came_from, current):
        path = deque()
        while current in came_from:
            path.appendleft(current)
            current = came_from[current]
        return path
    open_set = []
    heapq.heappush(open_set, (0, start))
    came_from = {}
    g_score = {start: 0}
    f_score = {start: heuristic(start, goal)}
    while open_set:
        current = heapq.heappop(open_set)[1]
        if current == goal:
            return reconstruct_path(came_from, current)
        for neighbor in [(current[0]+1, current[1]), (current[0]-1, current[1]), (current[0], current[1]+1), (current[0], current[1]-1)]:
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and not grid[neighbor[0]][neighbor[1]]:
                tentative_g_score = g_score[current] + 1
                if tentative_g_score < g_score.get(neighbor, float("inf")):
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
    return None



imagepath=r"C:\\Users\\shiva\\OneDrive\\Pictures\\navigationtask.jpg"
image=cv2.imread(imagepath)
img=plt.imread(imagepath)


image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
se = cv2.getStructuringElement(cv2.MORPH_RECT, (8, 8))


bg = cv2.morphologyEx(image, cv2.MORPH_DILATE, se)
out_gray = cv2.divide(image, bg, scale=255)


out_binary = cv2.threshold(out_gray, 0, 255, cv2.THRESH_OTSU)[1]

bwimg=np.array(out_binary)

c=[]
for i in range (5):
    d=[]
    for j in range(5):
        print(sum(sum(bwimg[172*i:172*(i+1),172*j:172*(j+1)])))
        if (sum(sum(bwimg[172*i:172*(i+1),172*j:172*(j+1)])))>17000:
            d.append(1)
        else:
            d.append(0)
    c.append(d)
    print(c)
grid = c
start = (0, 0)
goal = (4, 4)
path = a_star(grid, start, goal)
u=[(start[0]+1,start[1]+1)]
# print(list(path))
for i in range(len(path)):
    (o,p)=path[i]
    u.append((o+1,p+1))
print(u)
# for i in range (5):
#     for j in range (5):
#          if b[i][j]==1:
#              print("(",i+1,",",j+1,")")
#          else:
#              print("No path found")
