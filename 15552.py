'''
문제 - for문
백준 15552 빠른 A+B
https://www.acmicpc.net/problem/15552
'''


import sys

t = int(input())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)


'''
알고 가자
import sys
sys.stdin.readline().split() : 한 줄씩 입력받아서 공백 기준으로 나눔
'''
