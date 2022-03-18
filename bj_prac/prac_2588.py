# 백준 2588번 문제

num_1 = int(input())
num_2 = int(input())

num_3 = num_1*(num_2%10)
num_4 = num_1*(num_2%100-num_2%10)//10
num_5 = num_1*(num_2-num_2%100)//100
num_6 = num_3+(num_4*10)+(num_5*100)

print(num_3)
print(num_4)
print(num_5)
print(num_6)