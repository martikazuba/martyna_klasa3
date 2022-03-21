with open("liczby.txt", "r") as file:
    lines = file.readlines()

numbers = []

for line in lines:
    numbers.append(line[:-1])

lista = ['1011', '100', '11000']

def zadanie1(numbers):
    value =0

    for j in range(0, len(numbers)):
        ones = 0
        zeros = 0
        for i in range(len(numbers[j])):
            if numbers[j][i] == '1':
                ones +=1
            else:
                zeros +=1
        if zeros>ones:
            value +=1
    return value