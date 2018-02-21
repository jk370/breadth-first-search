# Import required modules
import Node
import Game

# Conduct the search and print terminal node and path
print("Start")
game = Game()
solution = game.breadth_first_search()
print("The goal node is", solution.get_current_state())
print("The path is: ")
print(solution.print_path())