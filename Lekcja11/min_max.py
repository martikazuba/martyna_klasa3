if __name__ == "__main__":
    numbers = [6, 1, 2, 5, 7, 8, 9, 4, 5]
    max = numbers[0]
    min = numbers[0]

    for number in numbers:
        if number < min:
            min = number
        if number > max:
            max = number

    print(f"Liczba min to: {min}")
    print(f"Liczba max to: {max}")