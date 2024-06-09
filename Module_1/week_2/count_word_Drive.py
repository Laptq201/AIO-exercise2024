!gdown https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko

def count_word ( file_path ) :
    counter = {} 
    with open(file_path) as file:
        for line in file:
            words = line.split()
            for word in words:
                if word in counter:
                    counter[word] += 1
                else:
                    counter[word] = 1
    return counter
file_path = '/content/P1_data.txt'
result = count_word(file_path)
assert result ['who'] == 3
print(result['man'])