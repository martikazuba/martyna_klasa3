if __name__ == "__main__":
    numbers = [6, 1, 2, 5, 7, 8, 9, 4 , 5, 10]
    max = numbers[0]
    min = numbers[0]
    n = len(numbers)

    for i in range(0, n - 1, 2):
        if numbers[i] > numbers[i+1]:
            if numbers[i] > max:
                max = numbers[i]
            if numbers[i+1] < min:
                min = numbers[i+1]
        else:
            if numbers[i+1] > max:
                max = numbers[i+1]
            if numbers[i] < min:
                min = numbers[i]

    if n % 2 == 1:
        if numbers[n-1] > max:
            max = numbers[n-1]
        if numbers[n-1] < min:
            min = numbers[n-1]

    print(f"Liczba min to: {min}")
    print(f"Liczba max to: {max}")
