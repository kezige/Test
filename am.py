# 阿姆斯特朗数
# 如果一个 n 位正整数等于其各位数字的 n 次方之和,则称该数为阿姆斯特朗数。 例 如 1^3 + 5^3 + 3^3 = 153
# 输出所有的三位数中的阿姆斯特朗数
#  斐波那契数列
# 1000 以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。
sum = int(input("输入一个数"))
sumlen = len(str(sum))
sumNum = 0
for i in str(sum):
    sumNum +=int(i) ** sumlen
    if sum == sumNum:
        print("这个数的阿姆斯特郎数")
    else:
        print("不是阿姆斯特郎数")

sums = int(input("请输入要查找到多少的阿姆斯特郎数"))
sum = 0
while True:
    num = 0
    n = len(str(sum))
    for i in str(sum):
        num += int(i) ** n
        if sum == num:
            print("%d\t 这是个阿姆斯特朗数" % sum)
        if sum > sums:
           break
    sum += 1

