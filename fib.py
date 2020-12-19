# 斐波那契数列
sum = 0
num = 1
i = 0
while i < 10:
    t= sum + num
    print(t, end="  ")
    # 更新值
    sum = num
    num = t
    i += 1

# fib
# n1=0
# n2=1
# i=0
# while i<10:
#     n=n1+n2
#     print(n)
#     n1 = n2
#     n2=n
#     i +=1
