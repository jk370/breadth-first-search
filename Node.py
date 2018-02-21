# Import required modules
import numpy as np

class Node:
    def __init__(self, missionaries_wrong_side, cannibals_wrong_side, boat_wrong_side, parent):
        '''Initialises current state in the form of a tuple'''
        self.state = (missionaries_wrong_side, cannibals_wrong_side, boat_wrong_side)
        self.parent = parent
        
    def get_current_state(self):
        '''Returns the current state of the node'''
        return self.state
    
    def get_parent_node(self):
        '''Returns the parent node'''
        return self.parent
    
    def is_goal_state(self):
        '''Returns true if current state is goal state'''
        if self.state == (0, 0, 0):
            return True
        else:
            return False
     
    def is_valid_state(self):
        '''Returns false if missionaries are outnumbered on either side of bank for current state'''
        # Set appropriate variables
        missionaries_wrong_side, cannibals_wrong_side, boat = self.state
        missionaries_right_side = 3-missionaries_wrong_side
        cannibals_right_side = 3-cannibals_wrong_side
        
        # Check for outnumbered on either side
        if missionaries_wrong_side > 0 and missionaries_wrong_side < cannibals_wrong_side:
            return False
        elif missionaries_right_side > 0 and missionaries_right_side < cannibals_right_side:
            return False
        else:
            return True

    def get_child_nodes(self):
        '''Returns all possible child nodes from current states'''
        # Initialise variables
        action_list = []
        states = []
        missionaries_wrong_side, cannibals_wrong_side, boat = self.state
        missionaries_right_side = 3-missionaries_wrong_side
        cannibals_right_side = 3-cannibals_wrong_side
        
        # Return the boat - going wrong way
        if boat == 0:
            # Search for every possible action in range - check the amount of people is valid
            for people in range(1,3):
                if missionaries_right_side >= people:
                    missionary_action = (-people, 0, -1)
                    states.append(tuple(np.subtract(self.state, missionary_action)))
                
                if cannibals_right_side >= people:
                    cannibal_action = (0, -people, -1)
                    states.append(tuple(np.subtract(self.state, cannibal_action)))
                    
            # Take action for both    
            if missionaries_right_side >= 1 and cannibals_right_side >= 1:
                both_move = (-1, -1, -1)
                states.append(tuple(np.subtract(self.state, both_move)))
            
        # Else move people across - going right way
        else:
            # Search for every possible action in range - check the amount of people is valid
            for people in range(1,3):
                if missionaries_wrong_side >= people:
                    missionary_action = (people, 0, boat)
                    states.append(tuple(np.subtract(self.state, missionary_action)))
                
                if cannibals_wrong_side >= people:
                    cannibal_action = (0, people, boat)
                    states.append(tuple(np.subtract(self.state, cannibal_action)))
            
            #Take action for both
            if missionaries_wrong_side >= 1 and cannibals_wrong_side >= 1:
                both_move = (1, 1, boat)
                states.append(tuple(np.subtract(self.state, both_move)))

        # Create child nodes from states
        for state in states:
            first, second, third = state
            node = Node(first, second, third, self)
            if node.is_valid_state():
                action_list.append(node)
        
        return action_list
    
    def print_path(node):
        ''' Return the string of the path to reach a given node'''
        parent_node = node.get_parent_node()
    
        if parent_node == 0:
            return ("%s" % str(node.get_current_state()))

        else:
            return str("%s --> %s" % (str(print_path(parent_node)), str(node.get_current_state())))