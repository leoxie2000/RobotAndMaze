# You write this:
from SensorlessProblem import SensorlessProblem
from Maze import Maze
from astar_search import astar_search
def null_heuristic(state):
    return 0
test_maze1 = Maze("maze1.maz")
test_mp1 = SensorlessProblem(test_maze1)
# print(test_mp1.get_successors(test_mp1.start_state))
result1 = astar_search(test_mp1, null_heuristic)
print(result1)

result = astar_search(test_mp1, test_mp1.blind_heuristic)
print(result)


test_maze2 = Maze("maze3.maz")
test_mp2 = SensorlessProblem(test_maze2)
print(test_mp2.get_successors(test_mp2.start_state))

# UCS
result2 = astar_search(test_mp2, null_heuristic)
print(result2)
#

result = astar_search(test_mp2, test_mp2.blind_heuristic)
print(result)
