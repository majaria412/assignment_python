def func(a, b):
        if (isinstance(a, int) != True and isinstance(b, int) != True)\n
        (isinstance(a, float) != True and isinstance(b, float) != True:
            raise Exception("must be integer")
        elif a > b:
            raise Exception("a<b")
        else:
            answer = 0
            for i in range(a, b+1):
                answer += i
            return answer

def stringify(num: int) -> str:
    int가 string이 될 것이다. 타이핀팅 typing
    1. 검증하는 로직 연산하는 로직 그걸 리턴

    2. 어떻게하면 더 줄일 수 있을까? simple하게
    

print(func('a', 'b'))
