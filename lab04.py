from Stack import Stack

def solveMaze(maze, startX, startY):
    s = Stack()
    maze[startX][startY] = 1
    s.push((startX, startY))
    steps = 1
    
    while(maze[startX][startY] != 'G'):
        
        if maze[startX - 1][startY] == ' ' or maze[startX - 1][startY] == 'G':
            if maze[startX - 1][startY] == 'G':
                return True
            steps += 1
            maze[startX - 1][startY] = steps
            startX = startX - 1
            s.push((startX, startY))
            
        elif maze[startX][startY - 1] == ' ' or maze[startX][startY - 1] == 'G':
            if maze[startX][startY - 1] == 'G':
                return True
            steps += 1
            maze[startX][startY - 1] = steps
            startY = startY - 1
            s.push((startX, startY))
            
        elif maze[startX + 1][startY] == ' ' or maze[startX + 1][startY] == 'G':
            if maze[startX + 1][startY] == 'G':
                return True
            steps += 1
            maze[startX + 1][startY] = steps
            startX = startX + 1
            s.push((startX, startY))

        elif maze[startX][startY + 1] == ' ' or maze[startX][startY + 1] == 'G':
            if maze[startX][startY + 1] == 'G':
                return True
            steps += 1
            maze[startX][startY + 1] = steps
            startY = startY + 1
            s.push((startX, startY))

        else:
            if(s.isEmpty()):
                return False
            tup = s.pop()
            startX = tup[0]
            startY = tup[1]

    return True



        
            
    
        
    
   
    
