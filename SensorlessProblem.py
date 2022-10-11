from Maze import Maze
from time import sleep

class SensorlessProblem:

    ## You write the good stuff here:
    def __init__(self, maze):
        self.maze = maze
        self.start_state = self.get_start_states()
    def __str__(self):
        string =  "Blind robot problem: "
        return string

    def is_sensorless(self):
        return True
        # given a sequence of states (including robot turn), modify the maze and print it out.
        #  (Be careful, this does modify the maze!)

    def get_start_states(self):
        start_states = []
        for i in range(0, self.maze.width):
            for j in range(0, self.maze.height):
                if self.maze.is_floor(i,j):
                    start_states.append((i,j))

        return start_states
    def animate_path(self, path):
        # reset the robot locations in the maze

        self.maze.robotloc = list(self.start_state)

        for state in path:
            print(str(self))
            clean_state = list(self.delete_dir_in_state(state))
            print("clean state is",clean_state)

            loc = []
            for s in clean_state:
                loc.append(s[0])
                loc.append(s[1])
            self.update_robotloc(loc)

            sleep(1)

            print(str(self.maze))
    def get_cost(self,parent,child):
        return 1
    def update_robotloc(self,state):
        self.maze.robotloc = list(state)

    ##N = y+1, S = (y-1) W = x-1 E = x+1
    def get_successors(self,states):
        successors = []
        # print("parent state is ",states)
        clean_states = self.delete_dir_in_state(states)
        # print("Clean_states ", clean_states)
        for i in range(4):
            local = []
            for state in clean_states:
                currx,curry = state
                if i == 0:
                    next = (currx+1,curry)
                    if self.is_legal(next):
                        local.append(('E',currx+1,curry))
                elif i == 1:
                    next = (currx - 1, curry)
                    if self.is_legal(next):
                        local.append(('W', currx- 1, curry))
                elif i == 2:
                    next = (currx, curry+1)
                    if self.is_legal(next):
                        local.append(('N', currx, curry+1))
                elif i == 3:
                    next = (currx, curry - 1)
                    if self.is_legal(next):
                        local.append(('S', currx, curry-1))
            successors.append(local)
        return successors

    def goal_check(self,state):
        return len(state) == 1
    def blind_heuristic(self,state):
        #heuristic should be zero when we only have one state
        return len(state)-1


    def is_legal(self,state):
        if len(state) == 2:
            x = state[0]
            y = state[1]
        elif len(state) == 3:
            x = state[1]
            y = state[2]
        return self.maze.is_floor(x,y)

    def delete_dir_in_state(self,states):

        res = set()
        for s in states:
            # print("gettings",s)
            if len(s) == 3:
                res.add((s[1],s[2]))
            else:
                res = states
                return res
        return res
## A bit of test code

if __name__ == "__main__":
    test_maze3 = Maze("maze3.maz")
    test_problem = SensorlessProblem(test_maze3)
    print(test_problem.get_successors(test_problem.start_state))
