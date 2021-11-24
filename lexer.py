

def file_to_token(filename):
    # Fungsi yang menerima file python yang ingin diperiksa syntaxnya dan mengembalikan
    # sebuah list of string
    input_file = open(filename, 'r')
    input_file_lines = input_file.readlines()
    input_file.close()

    seperated_input_list = seperate_special_character(input_file_lines)

    token_list = []
    for strings in seperated_input_list:
        for element in strings:
            token_list.append(element)

    return token_list


def seperate_special_character(input_file):
    # Fungsi yang akan mengembalikan special char menjadi sebuah string terpisah
    # dari string awal
    input_list = []
    for line in input_file:
        line = line.replace('(', ' ( ')
        line = line.replace(')', ' ) ')
        line = line.replace('+', ' + ')
        line = line.replace('-', ' - ')
        line = line.replace('*', ' * ')
        line = line.replace('/', ' / ')
        line = line.replace('%', ' % ')
        line = line.replace(',', ' , ')
        line = line.replace('.', ' . ')
        line = line.replace('>', ' > ')
        line = line.replace('<', ' < ')
        line = line.replace('[', ' [ ')
        line = line.replace(']', ' ] ')
        line = line.replace('"', ' " ')
        line = line.replace("'", " ' ")
        line = line.replace('=', ' = ')
        line = line.replace(':', ' : ')
        line = line.split()
        # line.append('EOL')
        input_list.append(line)
    return input_list


#print(file_to_token('test.py'))
