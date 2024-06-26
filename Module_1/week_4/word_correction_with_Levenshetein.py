import streamlit as st


def levenshtein_distance(token1, token2):
    matrix = [[0 for _ in range(len(token2) + 1)]
              for _ in range(len(token1) + 1)]
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
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i]
                               [j - 1] + 1, matrix[i - 1][j - 1] + cost)

    distance = matrix[len(token1)][len(token2)]
    return distance


def load_vocab(file_path):  # lay file tu dien da co san
    with open(file_path, 'r') as f:
        lines = f.readlines()
    words = sorted(set([lines.strip().lower() for lines in lines]))
    return words


def main():
    st.title("Word Correction with Levenshtein Distance")
    word = st.text_input("Enter a word")
    vocabulary = load_vocab("./assets/vocab.txt")

    if st.button("Compute"):

        # call for levenshtein distance function
        leven_distances = dict()
        for vocab in vocabulary:
            leven_distances[vocab] = levenshtein_distance(word, vocab)
        #
        sorted_distances = dict(
            sorted(leven_distances.items(), key=lambda item: item[1]))
        correct_word = list(sorted_distances.keys())[0]
        st.write("Correct word from the existing vocabulary: ", correct_word)

        col1, col2 = st.columns(2)  # split the screen into 2 columns
        col1.write('Vocabulary:')
        col1.write(vocabulary)

        col2.write('Levenshtein Distance:')
        col2.write(sorted_distances)


if __name__ == '__main__':
    main()
