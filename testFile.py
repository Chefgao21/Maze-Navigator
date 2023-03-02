from Stack import Stack
from lab04 import *

maze = [ ['+','+','+','+','G','+'],
         ['+','+','+',' ',' ','+'],
         ['+',' ',' ',' ','+','+'],
         ['+','+',' ','+',' ','+'],
         ['+','+',' ',' ','+','+'],
         ['+','+','+','+','+','+'] ]

maze1 = [ ['G','+','+','+','+','+'],
          ['+','+',' ',' ','+','+'],
          ['+',' ',' ',' ','+','+'],
          ['+','+','+','+','+','+'] ]

maze2 = [ ['+','+','+'],
          ['+',' ','+'],
          ['+','+','+'] ]

def test__lab04():
    
    assert solveMaze(maze, 4, 3) == True
    assert maze == [ ['+', '+', '+', '+', 'G', '+'],
                     ['+', '+', '+', 7, 8, '+'],
                     ['+', 5, 4, 6, '+', '+'],
                     ['+', '+', 3, '+', ' ', '+'],
                     ['+', '+', 2, 1, '+', '+'],
                     ['+', '+', '+', '+', '+', '+'] ]
    assert solveMaze(maze, 3, 4) == False


    assert solveMaze(maze1, 1, 3) == False
    assert maze1 == [ ['G','+','+','+','+','+'],
                      ['+','+', 2, 1,'+','+'],
                      ['+', 4, 3, 5,'+','+'],
                      ['+','+','+','+','+','+'] ]
    assert solveMaze(maze1, 1, 2) == False

    assert solveMaze(maze2, 1, 1) == False
    assert maze2 == [ ['+','+','+'],
                      ['+', 1,'+'],
                      ['+','+','+'] ]

