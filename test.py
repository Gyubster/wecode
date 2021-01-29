def test():
    numbers = [i for i in range(50)]
    answer =[]
    for number in numbers:
        if number%2 == 0:
            answer.append(number)
    return answer
