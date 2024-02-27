def factorial(num):
    if num == 0:
        return 1
    else:
        result = 1
        for i in range(2, num + 1):
            result *= i
        return result
