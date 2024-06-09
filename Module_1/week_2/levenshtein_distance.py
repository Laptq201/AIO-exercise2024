def levenshtein_distance(token1, token2):
    """
    This function calculates the Levenshtein distance between two strings
    """
    # Create a matrix of zeros with dimensions (len(token1)+1) x (len(token2)+1)
    matrix = [[0 for _ in range(len(token2) + 1)] for _ in range(len(token1) + 1)]
    # Fill in the first row of the matrix
    for i in range(len(token1) + 1):
        matrix[i][0] = i
    # Fill in the first column of the matrix
    for j in range(len(token2) + 1):
        matrix[0][j] = j
    # Iterate over the rest of the matrix
    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            # If the characters at the current positions are the same
            if token1[i - 1] == token2[j - 1]:
                # The cost is 0
                cost = 0
            else:
                # The cost is 1
                cost = 1
            # Calculate the minimum of the three possible values
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost)
    # The Levenshtein distance is the value in the bottom right corner of the matrix
    distance = matrix[len(token1)][len(token2)]

    return distance 


if __name__ == '__main__':
    assert levenshtein_distance("hi", "hello") == 4.0
    print(levenshtein_distance("hola", "hello"))