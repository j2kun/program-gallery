def dynamicTimeWarp(seqA, seqB, d=lambda x, y: abs(x-y)):
    # create the cost matrix
    numRows, numCols = len(seqA), len(seqB)
    cost = [[0 for _ in range(numCols)] for _ in range(numRows)]

    # initialize the first row and column
    cost[0][0] = d(seqA[0], seqB[0])
    for i in range(1, numRows):
        cost[i][0] = cost[i-1][0] + d(seqA[i], seqB[0])

    for j in range(1, numCols):
        cost[0][j] = cost[0][j-1] + d(seqA[0], seqB[j])

    # fill in the rest of the matrix
    for i in range(1, numRows):
        for j in range(1, numCols):
            choices = cost[i-1][j], cost[i][j-1], cost[i-1][j-1]
            cost[i][j] = min(choices) + d(seqA[i], seqB[j])

    return cost[-1][-1]
