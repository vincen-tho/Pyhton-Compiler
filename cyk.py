import lexer as lx

global terminals, input, file, cykMap
terminals = lx.file_to_token('terminal.txt')
input = lx.file_to_token('input.py')
file = open('cnf.txt').read()


cykMap = {}
def map():
    splitted = file.split('\n')
    for i in range(len(splitted)-1):
        val = splitted[i].split(' -> ')[0]
        temp = splitted[i].split(' -> ')[1]
        temp = temp.replace(" ", "")
        tempKey = temp.split('|')
        for j in tempKey:
            if (cykMap.get(j) == None):
                cykMap.update({j: [val]})
            else :
                cykMap[j].append(val)



def finiteAutomataVariable(s):
    # Mengembalikan true jika s bagian dari variable
    if len(s)<1:
        return False
    else:
        validVar = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '_']
        numberArray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        if s[0] not in validVar:
            return False
        else:
            for i in s:
                if (i not in numberArray) and (i not in validVar):
                    return False
        return True

def finiteAutomataNumber(s):
    # Mengembalikan true jika s bagian dari variable
    if len(s)<1:
        return False
    else:
        numberArray = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in s:
            if i not in numberArray:
                return False
        return True
def cyk():
    map()
    # print(input)
    cykTable = [[[] for j in range(i)] for i in range(len(input),0,-1)]

    for i in range(len(input)):
        if(input[i] in terminals):
            if(cykMap.get(input[i]) != None):
                cykTable[0][i].extend(cykMap.get(input[i]))
            else:
                continue

        else:
            if finiteAutomataVariable(input[i]):
                cykTable[0][i].extend(cykMap.get('variable'))
            if finiteAutomataNumber(input[i]):
                cykTable[0][i].extend(cykMap.get('number'))
        if input[i] != "'" and input[i] != '"':
            cykTable[0][i].extend(cykMap.get('string'))
        cykTable[0][i] = list(dict.fromkeys(cykTable[0][i]))
    
    for i in range(1,len(input)):
        for j in range(len(input)-i):
            for k in range(i):
                for l in cykTable[i-k-1][j]:
                    for m in cykTable[k][j+i-k]:
                        temp = cykMap.get(l+m)
                        if temp != None:
                            cykTable[i][j].extend(temp)
                        else:
                            continue
                cykTable[i][j] = list(dict.fromkeys(cykTable[i][j]))
    # for i in cykTable:
    #     print(i)
    return cykTable

def getVerdict(cykTable):
    if 'S' in cykTable[-1][-1] or 'S0' in cykTable[-1][-1]:
        return True
    else:
        return False


# print(finiteAutomataVariable('a31'))



