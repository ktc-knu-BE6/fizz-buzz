for i in range(1, 101):
    answer = i
    # 1부터 100까지 100번 반복
    if isThreeMultiple(i):
        answer = "Fizz"
    elif isFiveMultiple(i):
        answer = "Buzz"
    elif isFifteenMultiple(i):
        answer = "FizzBuzz"
    print(answer)


