from Stack import Stack

s = Stack()
def solveMaze(maze, startX, startY):
    step = 0
    s.push([startX, startY])
    while not s.isEmpty():
        #maze[startX][startY] != 'G'
        l = s.peek()
        startX = l[0]
        startY = l[1]
        if maze[startX][startY] == ' ':
            step = step + 1
            maze[startX][startY] = step
        if (maze[startX-1][startY] != "+") and (type(maze[startX-1][startY]) != int):
            print(startX, startY)
            if maze[startX-1][startY] == 'G':
                print("going up and goal is here") 
                return True
            else:
                    s.push([startX-1, startY])
                    continue
        if maze[startX][startY-1] != "+" and type(maze[startX][startY-1]) != int:
            if maze[startX][startY-1] == 'G':
                print("going left and goal is here") 
                return True
            else:
                s.push([startX, startY-1])
                continue
        if maze[startX+1][startY] != "+" and type(maze[startX+1][startY]) != int:
            if maze[startX+1][startY] == 'G':
                print("going down and goal is here") 
                return True
            else:
                s.push([startX+1, startY])
                continue
        if maze[startX][startY+1] != "+" and type(maze[startX][startY+1]) != int:
            if maze[startX][startY+1] == 'G':
                print("going right and goal is here") 
                return True
            else:
                 s.push([startX, startY+1])
                 continue
        
        else:
            s.pop()
            print("popping from the stack")
            # if s.isEmpty() == True:
            #     return False
        
    print("path not found")
    return False
        
               

def printMaze(maze):
	for row in range(len(maze)):
		for col in range(len(maze[0])):
			print("|{:<2}".format(maze[row][col]), sep='',end='')
		print("|")
	return

# maze = [
# ['+','+','+','+','G','+'],
# ['+',' ','+',' ',' ','+'],
# ['+',' ',' ',' ','+','+'],
# ['+',' ','+','+',' ','+'],
# ['+',' ',' ',' ',' ','+'],
# ['+','+','+','+','+','+'] ]

# maze2 = [
# ['+','+','+','+','+','+'],
# ['+',' ',' ',' ',' ','+'],
# ['+',' ',' ','G',' ','+'],
# ['+',' ',' ',' ',' ','+'],
# ['+',' ',' ',' ',' ','+'],
# ['+','+','+','+','+','+'] ]

'''maze3 = [
['+','+','+','+','G','+'],
['+',' ',' ',' ','+','+'],
['+',' ','+',' ',' ','+'],
['+',' ',' ',' ',' ','+'],
['+',' ',' ',' ',' ','+'],
['+','+','+','+','+','+'] ]'''



#solveMaze(maze2, 2, 4)
#printMaze(maze2)
#print(solveMaze(maze3, 4, 4))
#printMaze(maze3)



#print(1+1)