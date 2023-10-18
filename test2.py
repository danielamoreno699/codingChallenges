def numPlayers(k, scores):
    # Players with equal scores have equal ranks.
    # Players with the next lower score will be ranked based on position within the list.
    # k is the minimum to level up.
    players = 0
    
    for i in range(1, len(scores) + 1):
        if (i <= k):
            players += 1

    
    print(players)

numPlayers(3, [100, 50, 50, 25])
