'''
문제 - 입출력과 사칙연산
백준 10430 나머지
https://www.acmicpc.net/problem/10430
'''

a, b, c = map(int, input().split())
print((a + b) % c)
print(((a % c) + (b % c)) % c)
print((a * b) % c)
print(((a % c) * (b % c)) % c)

'''
알고 가자
'''
