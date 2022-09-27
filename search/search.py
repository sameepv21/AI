# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

from re import L
import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"

    # Define required imports
    from util import Stack

    # Define required variables
    visited = []
    stack = Stack()
    actions = []

    """
        getStartState() --> No parameters, Returns the initial coordinate of pacman
        isGoalState() --> Takes the state i.e coordinates as parameter, Returns boolean
        getSuccessors() --> Takes the state as parameter, Returns list of next (child) states, direction and action costs

        Here, instead of passing actions, we pass the whole array/list of actions required for reaching a particular goal.
    """

    # Initial state
    stack.push((problem.getStartState(), [])) # passing empty actions

    # DFS (Complete version)
    while(not stack.isEmpty()):
        currentState, actions = stack.pop()

        visited.append(currentState)

        # return list of actions that reach goal state
        if(problem.isGoalState(currentState)):
            # search is completed
            break

        # DFS
        for child in problem.getSuccessors(currentState):
            # child[0] is the state and child[1] is the action
            if child[0] not in visited:
                if(len(actions) == 0):
                    actionsForParticularState = [child[1]]
                else:
                    actionsForParticularState = actions + [child[1]]
                stack.push((child[0], actionsForParticularState))
    return actions

def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    # Import Required Libraries
    from util import Queue

    # Define required variables
    visited = []
    queue = Queue()
    actions = []

    # Intitial State
    queue.push((problem.getStartState(), [])) # passing empty list of actions

    # BFS
    while not queue.isEmpty():
        currentState, actions = queue.pop()
        
        # Append to visited nodes
        visited.append(currentState)

        # Check whether currentState is the goal state or not
        if problem.isGoalState(currentState):
            # search is completed
            break

        for child in problem.getSuccessors(currentState):
            if child[0] not in visited:
                if len(actions) == 0:
                    actionsForParticularState = [child[1]]
                else:
                    actionsForParticularState = actions + [child[1]]
                queue.push((child[0], actionsForParticularState))         
    return actions

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"

    # Import required libraries
    from util import PriorityQueue

    # Declare required variables
    actions = []
    visited = []
    priorityQueue = PriorityQueue()

    # Initial State
    """
        There are 2 parameters to priority queue viz data and priority where data represents the data for which
        priority needs to be decided and priority is self explanatory

        For data, list is passed containing current state (initially only starting state), list of actions to
        reach that state and its cost
    """
    priorityQueue.push((problem.getStartState(), [], 0), 1)

    # UCS
    while not priorityQueue.isEmpty():
        currentState, actions, prevCost = priorityQueue.pop()

        visited.append(currentState)

        if(problem.isGoalState(currentState)):
            # search is completed
            break

        for child in problem.getSuccessors(currentState):
            if child[0] not in visited:
                if(len(actions) == 0):
                    actionsForParticularState = [child[1]]
                else:
                    actionsForParticularState = actions + [child[1]]
                cost = prevCost + child[2]
                priorityQueue.push((child[0], actionsForParticularState, cost), cost)
    return actions

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
