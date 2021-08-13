'''
문제 - for문
백준 10950 A + B - 3
https://www.acmicpc.net/problem/10950
'''


n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    print(a + b)


'''
알고 가자
for _ in range(n)
    : for문을 실행하면서 변수 값이 필요 없을 때 _(언더바) 사용
    : range(n)은 n회 반복한다는 의미
'''
