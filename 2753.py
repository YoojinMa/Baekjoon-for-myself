'''
문제 - if문
백준 2753 윤년
https://www.acmicpc.net/problem/2753
'''


a = int(input())
if a % 4 == 0 and a % 100 != 0:
    print('1')
elif a % 400 == 0:
    print('1')
else:
    print('0')
	

'''
알고 가자
파이썬에서 '~면서'는 and 사용
'''
