if __name__ == "__main__":

    with open ("min_max_data.txt") as file:
        text = file.readlines()
        #print(text)
        numbers = []
        for line in text:
            numbers.append(int(line[:-1]))
        #print(numbers)

        #numbers = [6, 1, 2, 5, 7, 8, 9, 4, 5]
        max = numbers[0]
        min = numbers[0]

        for number in numbers:
            if number < min:
                min = number
            if number > max:
                max = number

        print(f"Liczba min to: {min}")
        print(f"Liczba max to: {max}")