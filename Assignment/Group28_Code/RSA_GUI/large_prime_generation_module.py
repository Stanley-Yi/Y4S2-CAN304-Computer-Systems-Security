# !/usr/local/bin/python3
# @Time : 2022/4/24 0:22
# @Author : Tianlei.Shi
# @Site :
# @File : large_prime_generation_module.py
# @Software : PyCharm


import random


def Miller_Rabin(Num):  # 可替换为其他验证质数的方法
    CheckTimes=10
    eulerN=Num-1
    oddQ=0
    testNum2=0

    while(eulerN%2==0):

        testNum2=testNum2+1
        eulerN=eulerN//2

    oddQ=eulerN
    for trials in range(CheckTimes):
        random_a=random.randrange(2,Num-1)
        firstTest=pow(random_a,oddQ,Num)
        if(firstTest==1 or firstTest==Num-1):
            continue
        else:
            nextTest=firstTest
            for i in range(1,testNum2):
                nextTest=(nextTest**2)%Num
                if(nextTest==Num-1):
                    break
            return False
    return True




def trial_division(num):
    # small_primes = [3, 5]
    small_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    pass_test = False

    while not pass_test:
        restart = False
        index = len(small_primes)

        while index > 0 and not restart:
            index -= 1
            if num % small_primes[index] == 0:  # 求模可优化
                num += 2
                restart = True

        if not restart:
            pass_test = True

    return num




def generate_prime(keysize=1024):
    large_num = random.randrange(2 ** (keysize - 1), 2 ** keysize)  # 此处幂运算可优化
    odd_large_num = large_num * 2 + 1

    prime = trial_division(odd_large_num)

    while not Miller_Rabin(prime):  # 可替换为其他验证质数的方法
        prime += 2
        prime = trial_division(prime)

    return prime




if __name__ == '__main__':
    prime = generate_prime()
    print(prime)