def levenshtein_distance(token1, token2):
    matrix = [[0 for _ in range(len(token2) + 1)] for _ in range(len(token1) + 1)]
    for i in range(len(token1) + 1):
        matrix[i][0] = i
    for j in range(len(token2) + 1):
        matrix[0][j] = j
    for i in range(1, len(token1) + 1):
        for j in range(1, len(token2) + 1):
            if token1[i - 1] == token2[j - 1]:
                cost = 0
            else:
                cost = 1
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost)
    
    distance = matrix[len(token1)][len(token2)]

    return distance 


if __name__ == '__main__':
    assert levenshtein_distance("hi", "hello") == 4.0
    print(levenshtein_distance("hola", "hello"))