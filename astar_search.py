from SearchSolution import SearchSolution
import heapq
from heapq import heappush, heappop
from Maze import Maze
from MazeworldProblem import MazeworldProblem
class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        self.parent = parent
        self.state = state
        self.heuristic = heuristic
        self.transition_cost = transition_cost


        # you write this part


    def priority(self):
        return self.transition_cost+self.heuristic
        # you write this part

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node,searchproblem,solution):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    if searchproblem.is_sensorless():
        searchproblem.animate_path(result)
    return result


def astar_search(search_problem, heuristic_fn):
    # I'll get you started:
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heapq.heapify(pqueue)
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)
    visited_cost = {}
    visited_cost[tuple(start_node.state)] = 0
    while pqueue:
        parent = heappop(pqueue)
        parent_state = parent.state
        solution.nodes_visited += 1
        search_problem.update_robotloc(parent_state)

        #check for goal
        if search_problem.goal_check(parent_state):
            solution.path = backchain(parent,search_problem,solution)
            solution.cost = parent.transition_cost
            return solution
        # print("At state ",parent_state)
        children = search_problem.get_successors(parent_state)
        # print("children are ", children)
        for child in children:
            heuristic = heuristic_fn(child)
            trans_cost = search_problem.get_cost(parent_state,child)+ parent.transition_cost
            fn = heuristic+trans_cost

            if tuple(child) in visited_cost:
                if fn < visited_cost[tuple(child)]:
                    node = AstarNode(child,heuristic,parent,trans_cost)
                    visited_cost[tuple(child)] = fn
                    heappush(pqueue,node)
            else:
                node = AstarNode(child, heuristic, parent, trans_cost)
                visited_cost[tuple(child)] = fn
                heappush(pqueue, node)
    return solution






    # you write the rest:
if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_mp = MazeworldProblem(test_maze3, (1, 4, 1, 3, 1, 2))
    print(astar_search(test_mp,test_mp.manhattan_heuristic))
