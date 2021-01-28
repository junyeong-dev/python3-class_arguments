# 정해지지 않은 arguments를 받고 싶을 경우
# *args    : positional arguments
# **kwargs : keyword arguments
def plus(a, b, *args, **kwargs):
    # tuple 형태로 출력
    print(args)
    # dictionary 형태로 출력
    print(kwargs)
    return a + b

plus(1, 2, 3, 4, 5, 6, hello=True, world="python")