#백준 2753번 문제

year = int(input())
if (year%4==0 and ((year%100!=0) or (year%400 ==0))): #윤년일때
    print (1)
else:
    print(0)
