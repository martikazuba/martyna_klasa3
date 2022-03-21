with open("liczby.txt", "r") as file:
    lines = file.readlines()

numbers = []

for line in lines:
    numbers.append(line[:-1])

lista = ['1011', '100', '11000']

def zadanie2(numbers):
    print(numbers)
    for i in range(0, len(numbers)):
        if numbers[i][len(numbers)-1] ==0:
            print("tak")

print(zadanie1(numbers))
print(zadanie2(lista))