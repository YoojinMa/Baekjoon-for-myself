'''
문제 - 입출력과 사칙연산
백준 1000
https://www.acmicpc.net/problem/1000
'''

a, b = map(int, input().split())
print(a + b)

'''
알고 가자
a, b = int(input().split())은 불가능 - 이유 : int는 list로 받지 못함
a, b = map(int, input().split())은 가능
'''
