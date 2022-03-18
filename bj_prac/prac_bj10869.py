# 백준 10869번 문제

# 문제 : 두 자연수 A와 B가 주어진다. 이 때 A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램

# 입력 : 두 자연수 A와 B가 주어진다.
# 출력 : 첫째 줄에 A+B, 둘째줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.

A,B=map(int,input().split())
print(A+B,A-B,A*B,int(A/B),A%B,sep='\n')