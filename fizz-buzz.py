def isFifteenMultiple(num):
    if num % 15 == 0:
        return True
    return False

def isFiveMultiple(i):
    if i % 5 == 0:
        return True
    return False
  
def isThreeMultiple(num):
    return num % 3 == 0


for i in range(1, 101):
    answer = i
    # 1부터 100까지 100번 반복
    if isFifteenMultiple(i):
        answer = "FizzBuzz"
    elif isThreeMultiple(i):
        answer = "Fizz"
    elif isFiveMultiple(i):
        answer = "Buzz"
    print(answer)


