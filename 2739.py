'''
문제 - for문
백준 2739 구구단
https://www.acmicpc.net/problem/2739
'''


n = int(input())
for i in range(1, 10):
    print(n, '*', i, '=', n * i)


'''
알고 가자
for i in range(1, 10)
    : i는 for문 안에서 사용되는 변수
    : range(시작 숫자, 끝 숫자) 지정. 끝 숫자는 포함되지 않음
'''
