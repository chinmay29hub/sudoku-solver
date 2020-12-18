import numpy as np


import pyfiglet


import pyautogui



grid =[
       [0,0,0, 0,0,0, 0,2,0],
       [7,0,0, 0,0,2, 6,0,0],
       [0,4,6, 0,8,3, 1,0,0],
       
       [0,7,5, 0,1,0, 0,0,0],
       [0,0,1, 9,7,8, 2,0,0],
       [0,0,0, 0,3,0, 4,1,0],
       
       [0,0,7, 4,2,0, 8,3,0],
       [0,0,4, 8,0,0, 0,0,5],
       [0,6,0, 0,0,0, 0,0,0]
      ]



data = pyfiglet.figlet_format("Sudoku   Solver")   
#print(data)
pyautogui.typewrite(data, interval = 0.005)


#print("Before Solving :::\n")
pyautogui.typewrite('Before Solving :::\n', interval = 0.05)
print("\n\n")
print(np.array(grid))
print("\n\n")









def possible(x,y,n):
    
    
    val = grid[y][x]
    rx = x - x%3
    ry = y - y%3
    
    
    
    if val!=0:
	
       return False
    if n in grid[y]:

       return False
    for row in grid:
    	if n==row[x]:
    	   return False
    
    
    	   
    for x_ in range(rx,rx+3):
        for y_ in range(ry,ry+3):
            
            if n==grid[y_][x_]:
               return False
    return True 



def presolve(x,y):
    
    poss = []
    
    for i in range(1,10):
        if possible(x,y,i):
           poss.append(i)              
        	   
    
    return poss
    	   


def lookup(y):
    
    ltable = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0}
    
    
    for x in range(9):
        p = presolve(x,y)
        for i in p:
            ltable[i] = ltable[i] + 1 
            
    
    
    for i in range(1,10):
    
        if ltable[i] == 1:
           for x in range(9):
               if possible(x,y,i):
                 #print(x,y,i)
                  grid[y][x] = i
                  return True
                  
    return False 




def solve():
    for y in range(9):
        if lookup(y):
           solve()
solve()



#print("\n\nAfter Solving:::\n")
pyautogui.typewrite('After Solving :::\n', interval = 0.05)
print("\n\n")
g = np.array(grid)

print(g) 
print("\n\n")                      




#print("\nPuzzled Solved : Check on https://www.sudoku-solutions.com/\n\n")  

pyautogui.typewrite('Puzzled Solved : Check on https://www.sudoku-solutions.com/\n\n\n', interval = 0.05)     
    	   


