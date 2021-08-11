'''
문제 - if문
백준 2884 알람 시계
https://www.acmicpc.net/problem/2884
'''


a, b = map(int, input().split())
if (b < 45):
    b = 60 - 45 + b
    if (a == 0):
        a = 23
    else:
        a -= 1
else:
    b -= 45
print(a, b)


'''
알고 가자
'''
