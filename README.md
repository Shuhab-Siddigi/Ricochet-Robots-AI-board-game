# Ricochet-Robots-AI-board-game

Ricochet Robots board game played by AI agent
### Requirements
To be able to run the program pygame==2.1.2 is required
## To run the program run __main__.py

### To change the values of the board with specific prefixes.

     __main__.py file 
    
    23 positions = [(0, 6), (15, 0), (0, 15), (13, 6)]
    24 token = "GC"
    25 board = Board(levels.Level0,positions=positions,token=token)

### To test AI (Prefix has to be set) or just press button

    33 goal = board.tokens[token]
    34 board.commands = ai.solve("BFS", board.graph, board.players, token, goal)
    34 board.commands = ai.solve("a_star", board.graph, board.players, token, goal)