
import search
import random

# Module Classes

class EightPuzzleState:


 def __init__( self, numbers ):
 
   self.cells = []
   numbers = numbers[:] # Make a copy so as not to cause side-effects.
   numbers.reverse()
   for row in range( 3 ):
     self.cells.append( [] )
     for col in range( 3 ):
       self.cells[row].append( numbers.pop() )
       if self.cells[row][col] == 0:
         self.blankLocation = row, col

 def isGoal( self ):
   
   current = 0
   for row in range( 3 ):
    for col in range( 3 ):
      if current != self.cells[row][col]:
        return False
      current += 1
   return True

 def legalMoves( self ):
  
   moves = []
   row, col = self.blankLocation
   if(row != 0):
     moves.append('up')
   if(row != 2):
     moves.append('down')
   if(col != 0):
     moves.append('left')
   if(col != 2):
     moves.append('right')
   return moves

 def result(self, move):
   
   row, col = self.blankLocation
   if(move == 'up'):
     newrow = row - 1
     newcol = col
   elif(move == 'down'):
     newrow = row + 1
     newcol = col
   elif(move == 'left'):
     newrow = row
     newcol = col - 1
   elif(move == 'right'):
     newrow = row
     newcol = col + 1
   else:
     raise Exception("Illegal Move")

   # Create a copy of the current eightPuzzle
   newPuzzle = EightPuzzleState([0, 0, 0, 0, 0, 0, 0, 0, 0])
   newPuzzle.cells = [values[:] for values in self.cells]
   # And update it to reflect the move
   newPuzzle.cells[row][col] = self.cells[newrow][newcol]
   newPuzzle.cells[newrow][newcol] = self.cells[row][col]
   newPuzzle.blankLocation = newrow, newcol

   return newPuzzle

 # Utilities for comparison and display
 def __eq__(self, other):
  
   for row in range( 3 ):
      if self.cells[row] != other.cells[row]:
        return False
   return True

 def __hash__(self):
   return hash(str(self.cells))

 def __getAsciiString(self):
  
   lines = []
   horizontalLine = ('-' * (13))
   lines.append(horizontalLine)
   for row in self.cells:
     rowLine = '|'
     for col in row:
       if col == 0:
         col = ' '
       rowLine = rowLine + ' ' + col.__str__() + ' |'
     lines.append(rowLine)
     lines.append(horizontalLine)
   return '\n'.join(lines)

 def __str__(self):
   return self.__getAsciiString()

# TODO: Implement The methods in this class

class EightPuzzleSearchProblem(search.SearchProblem):
  
  def __init__(self,puzzle):
    "Creates a new EightPuzzleSearchProblem which stores search information."
    self.puzzle = puzzle

  def getStartState(self):
    return puzzle
      
  def isGoalState(self,state):
    return state.isGoal()
   
  def getSuccessors(self,state):
   
    succ = []
    for a in state.legalMoves():
      succ.append((state.result(a), a, 1))
    return succ

  def getCostOfActions(self, actions):
     
     return len(actions)

EIGHT_PUZZLE_DATA = [[1, 0, 2, 3, 4, 5, 6, 7, 8], 
                     [1, 7, 8, 2, 3, 4, 5, 6, 0], 
                     [4, 3, 2, 7, 0, 5, 1, 6, 8], 
                     [5, 1, 3, 4, 0, 2, 6, 7, 8], 
                     [1, 2, 5, 7, 6, 8, 0, 4, 3], 
                     [0, 3, 1, 6, 8, 2, 7, 5, 4]]

def loadEightPuzzle(puzzleNumber):
  
  return EightPuzzleState(EIGHT_PUZZLE_DATA[puzzleNumber])

def createRandomEightPuzzle(moves=100):
 
 puzzle = EightPuzzleState([0,1,2,3,4,5,6,7,8])
 for i in range(moves):
   # Execute a random legal move
   puzzle = puzzle.result(random.sample(puzzle.legalMoves(), 1)[0])
 return puzzle

if __name__ == '__main__':
  puzzle = createRandomEightPuzzle(25)
  print('A random puzzle:')
  print(puzzle)
  
  problem = EightPuzzleSearchProblem(puzzle)
  path = search.breadthFirstSearch(problem)
  print(('BFS found a path of %d moves: %s' % (len(path), str(path))))
  curr = puzzle
  i = 1
  for a in path:
    curr = curr.result(a)
    print(('After %d move%s: %s' % (i, ("", "s")[i>1], a)))
    print(curr)
    
    eval(input("Press return for the next state..."))   # wait for key stroke
    i += 1
