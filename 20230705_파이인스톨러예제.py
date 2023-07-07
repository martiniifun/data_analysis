"""
홀짝 판별기
"""


def holjjak(n):
    n = int(n)
    if n % 2 == 1:
        print("홀수입니다.")
    elif n % 2 == 0:
        print("짝수입니다.")
    else:
        print("무슨 숫자인지 모르겠네요ㅜ")


if __name__ == '__main__':
    입력숫자 = input("정수를 입력해주세요 : ")
    holjjak(입력숫자)
    input()