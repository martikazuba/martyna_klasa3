def prime_number(number):
    if (number <= 1):
        return "nie zlozona, nie pierwsza"
    for i in range(2, number//2):
        if(number % i == 0):
            return "zlozona"
    return "pierwsza"

def perfect_number(number):
    total = 0
    for i in range(1, (number // 2) + 2):
        if (number % i == 0):
            total += i
    if (total == number and number > 0):
        return "doskonala"
    return "niedoskonala"

if _name_ == '_main_':
    f = open ('liczby.txt', 'w')
    print ("Program zapisuje informacje o zlozonosci liczb z zakresu <min,max) w plikuliczby.txt")
    min = int(input("Podaj min: "))
    max = int(input("Podaj max: "))
    for i in range (min,max):
        f.write(str(i))
        f.write("; ")
        f.write(prime_number(i))
        f.write("; ")
        f.write(perfect_number(i))
        f.write("\n")