from Maze import Maze
from time import sleep

class MazeworldProblem:

    ## you write the constructor, and whatever methods your astar function needs

    def __init__(self, maze, goal_locations):
        self.maze = maze
        self.goal = list(goal_locations)
        self.start_state = maze.robotloc.copy()
        self.start_state.insert(0,0)
        self.robotcount = len(maze.robotloc)//2

    def __str__(self):
        string =  "Mazeworld problem: "
        return string


    def goal_check(self,state):
        if len(state) != len(self.goal)+1:
            return False
        for i in range(1,len(state)):
            if state[i] != self.goal[i-1]:
                return False

        return True
        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)
    def update_robotloc(self,state):

        self.maze.robotloc = state[1:].copy()
    def get_successors(self, state):
        if len(state) == 1:
            return []
        state = list(state)
        toMove = state[0]
        robo_index = toMove*2+1
        currx = state[robo_index]
        curry = state[robo_index+1]

        possible_dir = [(currx+1,curry),(currx-1,curry),(currx,curry+1),(currx,curry-1)]
        next_loc = []
        for dir in possible_dir:
            if self.is_legal(dir):
                next_loc.append(list(dir))
        next_loc.append([currx,curry])
        next_to_move = (toMove+1) % self.robotcount
        successor_list = []
        firsthalf = []
        firsthalf.append(next_to_move)
        secondhalf = []
        # the robots that are not moving are kept here
        for i in range(1,robo_index):
            firsthalf.append(state[i])
        for i in range(robo_index+2,len(state)):
            secondhalf.append(state[i])

        for i in range(len(next_loc)):
            temp = firsthalf + next_loc[i] + secondhalf
            successor_list.append(temp)
        return successor_list
    def is_legal(self,state):
        # print(state)
        x = state[0]
        y = state[1]
        flag1 = self.maze.has_robot(x,y)
        flag2 = self.maze.is_floor(x,y)
        # if flag1:
        #     print("hasrobot")
        # else:
        #     print("has no robot")
        # if flag2:
        #     print("is floor")
        # else:
        #     print("not floor")
        if not flag1 and flag2:
            return True
        return False

    def manhattan_heuristic(self,state):
        total = 0
        for i in range(1,len(state)):
            total += abs(state[i]-self.goal[i-1])
        return total
    def is_sensorless(self):
        return False
    def get_cost(self, parent,child,edge_cost = 1):
        toMove = parent[0]
        robo_index = toMove * 2 + 1
        prevx = parent[robo_index]
        prevy = parent[robo_index+1]
        currx = child[robo_index]
        curry = child[robo_index + 1]
        if prevx == currx and prevy == curry:
            return 0
        return 1
    def animate_path(self, path):
        # reset the robot locations in the maze
        self.maze.robotloc = tuple(self.start_state[1:])

        for state in path:
            print(str(self))
            self.maze.robotloc = tuple(state[1:])
            sleep(1)

            print(str(self.maze))


## A bit of test code. You might want to add to it to verify that things
#  work as expected.

if __name__ == "__main__":
    test_maze4 = Maze("maze4.maz")
    test_mp = MazeworldProblem(test_maze4, (1, 4, 1, 3, 1, 2))
    print(test_maze4)
    # print(test_maze3.robotloc)
    # print(test_maze3.width,test_maze3.height)

    print(test_mp.get_successors((0, 1, 0, 1, 2, 2, 1)))
