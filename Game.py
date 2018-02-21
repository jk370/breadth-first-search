# Import required modules
import queue

class Game:
    def __init__(self):
        '''Sets up game by creating game with 3 missionaries, 3 cannibals and 1 boat on wrong side'''
        self.initial_node = Node(missionaries_wrong_side=3, cannibals_wrong_side=3, boat_wrong_side=1, parent = 0)
    
    def breadth_first_search(self):
        '''Performs breadth-first search from current state of node when called'''
        start = self.initial_node
        # Check first node and set up initial variables
        if start.is_goal_state():
            return start
        frontier = queue.Queue()
        frontier.put(start)
        explored = set() # set to hold state of each node that has been explored
        to_explore = set() # Bad double implementation of nodes passing through frontier due issues with iteration of queue
        
        # Search loop
        while not frontier.empty():
            next = frontier.get()
            # Add to explored and remove from frontier set
            explored.add(next.get_current_state())
            to_explore.discard(next.get_current_state())
            print("Exploring node", next.get_current_state())
            
            # Loop through child nodes and check state
            for child in next.get_child_nodes():
                child_state = child.get_current_state()
                if child_state not in explored and child_state not in to_explore:
                    if child.is_goal_state():
                        return child
                    # Add to frontier
                    frontier.put(child)
                    to_explore.add(child_state)
        
        return (Node(-1, -1, -1)) # Return if no answer found or invalid node explored