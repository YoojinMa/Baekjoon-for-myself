'''
문제 - if문
백준 14681 사분면 고르기
https://www.acmicpc.net/problem/14681
'''


a = int(input())
b = int(input())
if (a > 0 and b > 0):
    print('1')
elif (a < 0 and b > 0):
    print('2')
elif (a < 0 and b < 0):
    print('3')
else:
    print('4')


'''
알고 가자
'''