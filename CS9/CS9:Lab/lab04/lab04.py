from Stack import Stack

s = Stack()
def solveMaze(maze, startX, startY):
    step = 0
    s.push([startX, startY])
    while maze[startX][startY] != 'G':
        '''step = step + 1
        maze[startX][startY] = step

#        #for (dirX, dirY) in [(-1,0), (0, -1), (1, 0), (0, 1)]:
        for (dirX, dirY) in [(0,1), (1, 0), (0, -1), (-1, 0)]: # 
             

             curX = startX+dirX
             curY = startY+dirY

             if (maze[curX][curY] == "+") or (type(maze[curX][curY]) == int):
                  continue
             else:
                  s.push([curX, curY])
        
        if s.isEmpty() == True:
            return False
        
        l = s.pop()
        startX = l[0]
        startY = l[1]'''
            
            # check if + or int
            # # if yes continue
            # # if no add that value to the stack

             # error check curX curY in bounds
        # looking right
        l = s.peek()
        startX = l[0]
        startY = l[1]
        if maze[startX][startY] == ' ':
            step = step + 1
            maze[startX][startY] = step
        if maze[startX-1][startY] != "+" and type(maze[startX-1][startY]) != int:
            if maze[startX-1][startY] == 'G':
                 return True
            else:
                 s.push([startX-1, startY])
                 continue
        if maze[startX][startY-1] != "+" and type(maze[startX][startY-1]) != int:
            if maze[startX][startY-1] == 'G':
                 return True
            else:
                s.push([startX, startY-1])
                continue
        if maze[startX+1][startY] != "+" and type(maze[startX+1][startY]) != int:
            if maze[startX+1][startY] == 'G':
                 return True
            else:
                s.push([startX+1, startY])
                continue
        if maze[startX][startY+1] != "+" and type(maze[startX][startY+1]) != int:
            if maze[startX][startY+1] == 'G':
                 return True
            else:
                 s.push([startX, startY+1])
                 continue
        
        else:
            s.pop()
            if s.isEmpty() == True:
                return False
    return True
        
        # Non stack format

'''if maze[startX-1][startY] != "+" and type(maze[startX][startY+1]) != int:
            s.push([startX-1, startY])
        if maze[startX][startY-1] != "+" and type(maze[startX+1][startY]) != int:
            s.push([startX, startY-1])
        if maze[startX+1][startY] != "+" and type(maze[startX][startY-1]) != int:
            s.push([startX+1, startY])
        if maze[startX][startY+1] != "+" and type(maze[startX-1][startY]) != int:
            s.push([startX, startY+1])'''
    
'''if maze[startX][startY+1] == " ":
               s.push([startX, startY+1])
        if maze[startX+1][startY] == " ":
               s.push([startX+1, startY])
        if maze[startX][startY-1] == " ":
               s.push([startX, startY-1])
        if maze[startX-1][startY] == " ":
               s.push([startX-1, startY])'''
        
        #print("After Pop")
        #print(s.peek())
'''
        if maze[startX-1][startY] == "+" or type(maze[startX-1][startY])==int:
            if maze[startX][startY-1] == " ":
                step = step + 1
                s.push([startX, startY-1])
                maze[startX][startY-1] = step 
                startX = startX
                startY = startY-1
            elif maze[startX][startY-1] == "+" or type(maze[startX][startY-1]) == int: 
                if maze[startX+1][startY] == " ":
                    step = step + 1
                    s.push([startX+1, startY])
                    maze[startX+1][startY] = step 
                    startX = startX+1
                    startY = startY
                elif maze[startX+1][startY] == "+" or type(maze[startX+1][startY]) == int:
                    if maze[startX][startY+1] == " ":
                        step = step + 1
                        s.push([startX, startY+1])
                        maze[startX][startY+1] = step 
                        startX = startX
                        startY = startY+1
                    elif maze[startX][startY+1] == "+" or type(maze[startX][startY+1]) == int:
                            step = step 
                         '''
            
#        print(s.peek())
#        if (maze[s.peek()[0]-1][s.peek()[1]] == "+" or 
#            type(maze[s.peek()[0]-1][s.peek()[1]]) == int) and (maze[s.peek()[0]][s.peek()[1]-1] == "+" 
#                or type(maze[s.peek()[0]][s.peek()[1]-1]) == int) and (maze[s.peek()[0]+1][s.peek()[1]] == "+" 
#                or type(maze[s.peek()[0]+1][s.peek()[1]]) == int) and (maze[s.peek()[0]][s.peek()[1]+1] == "+" 
#                or type(maze[s.peek()[0]][s.peek()[1]+1]) == int):
               

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return

maze = [
['+','+','+','+','G','+'],
['+',' ','+',' ',' ','+'],
['+',' ',' ',' ','+','+'],
['+',' ','+','+',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]

maze2 = [
['+','+','+','+','+','+'],
['+',' ',' ',' ',' ','+'],
['+',' ',' ','G',' ','+'],
['+',' ',' ',' ',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]



#solveMaze(maze2, 2, 4)
#printMaze(maze2)
'''solveMaze(maze, 4, 4)
printMaze(maze)'''



#print(1+1)