import random
import sys
# enhance security
import improve_by_Ascii as iba
# large prime generation
import large_prime_generation_module as lpgm


class RSA:

    # 判断是否为素数
    def is_prime_num(self, n):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    return False
            else:
                return True

    # 判断是否为素数
    def is_prime(self, n):
        if n <= 3:
            return n > 1
        elif (n % 2 == 0) or (n % 3 == 0):
            return False
        i = 5
        while i * i <= n:
            if (n % i == 0) or (n % (i + 2) == 0):
                return False
            i += 6
        return True

    # 最大公因数
    def gcd(self, a, b):
        return a if b == 0 else self.gcd(b, a % b)

    # 最小公倍数
    def lcm(self, a, b):
        return a // self.gcd(a, b) * b

    # 基础方法寻找d
    def find_d(self, e, phi):
        while True:
            d = random.randint(2, 100000)
            if ((d * e) % phi) == 1:
                return d

    # 扩展欧几里得方法
    def ex_gcd(self, a, b, d, x, y):
        if b == 0:
            d[0], x[0], y[0] = a, 1, 0
        else:
            self.ex_gcd(b, a % b, d, y, x)
            y[0] -= a // b * x[0]


    # 基础加密与解密方法
    def transform(self, info, key, n):
        info = (info ** key) % n
        return info

    # quick power加密解密
    def quick_power(self, a, b, mod):
        res = 1
        while b != 0:
            if (b & 1) == 1:
                res = (res * a) % mod
            a = a * a % mod
            b >>= 1
        return res

    # # 中国余数定理
    # def crt(self, info, e, d, n, p, q, status):
    #     dp = [0]
    #     self.ex_gcd(e, p - 1, [0], dp, [0])
    #     dp = dp[0] % (p - 1)
    #     dq = [0]
    #     self.ex_gcd(e, q - 1, [0], dq, [0])
    #     dq = dq[0] % (q - 1)
    #     qinv = [0]
    #     self.ex_gcd(q, p, [0], qinv, [0])
    #     qinv = qinv[0] % p
    #     if status == "en":
    #         return (info ** e) % n
    #     elif status == "de":
    #         m1 = (info ** dp) % p
    #         m2 = (info ** dq) % q
    #         h = (qinv * ((m1 - m2) % p)) % p
    #         m = m2 + h * q
    #         return m

    # 中国余数定理
    def crt(self, info, p, q, dp, dq, qinv):
        m1 = self.quick_power(info, dp, p)
        m2 = self.quick_power(info, dq, q)
        h = (qinv * ((m1 - m2) % p)) % p
        m = m2 + h * q
        return m
    
        #获取p,q,m分量通过crt

    # # 中国余数定理2
    # def crt2(self, e, d, p, q, c):
    #     dp = [0]
    #     self.ex_gcd(e, p - 1, [0], dp, [0])
    #     dp = dp[0] % (p - 1)
    #     dq = [0]
    #     self.ex_gcd(e, q - 1, [0], dq, [0])
    #     dq = dq[0] % (q - 1)
    #
    #     cp = c % p
    #     cq = c % q
    #     mp = (c ** dp) % p
    #     mq = (c ** dq) % q
    #     return dp, dq, cp, cq, mp, mq
        
    #     #产生一个随机数A用于解密
    # def generate_A(self, p,q):
    #
    #     while True:
    #         if p < q:
    #             a = random.randint(0, q - 1)
    #             if a * p == 1 % q:
    #                 break
    #     return a
    #
    #     #解密
    # def dencypt2(self, mq, q, mp, p):
    #     a = self.generate_A(p,q)
    #     m = (((mq + q - mp) * a) % q) * p + mp
    #     return m

    # 基础方法生成key
    def generate(self):
        p, q = int(input("请输入素数p的值：")),  int(input("请输入素数q的值："))
        lambdan = self.lcm(p - 1, q - 1)
        e = 0
        while not self.is_prime(e):
            e = random.randint(2, lambdan - 1)
        d = [0]
        # get private key d which satisfies (de) mod lambdan = 1
        d = self.find_d(e, (p - 1) * (q - 1))
        # self.ex_gcd(e, lambdan, [0], d, [0])
        # d = d[0] % lambdan
        print("公钥PU=[e={},n={}]".format(e, p*q))
        print("私钥PR=[d={},n={}]".format(d, p*q))
        return {
            'n': p * q,  # public key PartI
            'e': e,  # public key PartII
            'd': d,  # private key
            'p': p,
            'q': q
        }

    # 升级版生成key
    def generate_update(self):
        p = lpgm.generate_prime(keysize=512)
        q = lpgm.generate_prime(keysize=512)
        print("素数p的值为：{}".format(p))
        print("素数q的值为：{}".format(q))
        lambdan = self.lcm(p - 1, q - 1)
        e = lpgm.generate_prime(keysize=512)
        d = [0]
        # get private key d which satisfies (d * e) mod lambdan = 1
        self.ex_gcd(e, lambdan, [0], d, [0])
        d = d[0] % lambdan
        print("公钥PU=[e={},n={}]".format(e, p * q))
        print("私钥PR=[d={},n={}]".format(d, p * q))

        dp = [0]
        self.ex_gcd(e, p - 1, [0], dp, [0])
        dp = dp[0] % (p - 1)
        dq = [0]
        self.ex_gcd(e, q - 1, [0], dq, [0])
        dq = dq[0] % (q - 1)
        qinv = [0]
        self.ex_gcd(q, p, [0], qinv, [0])
        qinv = qinv[0] % p

        return {
            'n': p * q,  # public key PartI
            'e': e,  # public key PartII
            'd': d,  # private key
            'p': p,
            'q': q,
            'dp': dp,
            'dq': dq,
            'qinv': qinv
        }

    # 基础方法加密
    def encrypt(self, m, e, n):
        c = self.transform(m, e, n)
        # c = self.quick_power(m, e, n)
        return c

    # 基础方法解密
    def decrypt(self, c, d, n):
        m = self.transform(c, d, n)
        # m = self.quick_power(c, d, n)
        return m

    # 基础方法加密
    def encrypt_update(self, m, e, n):
        # c = self.transform(m, e, n)
        c = self.quick_power(m, e, n)
        return c

    # 基础方法解密
    def decrypt_update(self, c, d, n):
        # m = self.transform(c, d, n)
        m = self.quick_power(c, d, n)
        return m





def choose_rsa():
    print("请选择合适的RSA类型")
    print(" " * 5 + "1--基础RSA")
    print(" " * 5 + "2--高效率RSA")
    print(" " * 5 + "3--新版RSA")
    print(" " * 5 + "4--新版高效率RSA")
    choose = int(input("请输入要选择的RSA类型: "))
    return choose

def show():
    print("=" * 25)
    print(" " * 5 + "{}".format("欢迎进入RSA算法"))
    print(" " * 5 + "1--加密")
    print(" " * 5 + "2--解密")
    print(" " * 5 + "3--重新选择RSA类型")
    print(" " * 5 + "4--退出")
    print("=" * 25)
    choose = int(input("请输入要选择的功能号："))
    return choose


# if __name__ == "__main__":
#     msg = input("请输入初始明文：")
#     rsa1 = RSA()
#     rsa2 = RSA()
#     c, m = [], []
#     rsa_type = choose_rsa()
#     while True:
#         if rsa_type == 1:
#             keys = rsa1.generate()
#             choose = show()
#             c, m = [], []
#             while choose != 4:
#                 if choose == 1:
#                     for i in range(len(msg)):
#                         # ord()函数: 返回对应字符的ASCII值
#                         # c.append(rsa2.crt(info=ord(msg[i]), e=keys['e'], d=keys['d'], n=keys['n'], p=keys['p'], q=keys['q'], status="en"))
#                         c.append(rsa2.encrypt(m=ord(msg[i]), e=keys['e'], n=keys['n']))
#                     cc = "".join(str(c))
#                     print("密文是：{}".format(cc))
#                 elif choose == 2:
#                     for i in range(len(msg)):
#                         # m.append(chr(rsa2.crt(info=c[i], e=keys['e'], d=keys['d'], n=keys['n'], p=keys['p'], q=keys['q'], status="de")))
#                         m.append(chr(rsa1.decrypt(c[i], d=keys['d'], n=keys['n'])))
#                     ming = "".join(m)
#                     print("明文：{}".format(ming))
#                     c, m = [], []
#                 elif (choose == 3) or (choose == 4):
#                     break
#                 choose = show()
#
#
#
#         elif rsa_type == 2:
#             keys = rsa1.generate()
#             choose = show()
#             c, m = [], []
#             while choose != 4:
#                 if choose == 1:
#                     for i in range(len(msg)):
#                         # ord()函数: 返回对应字符的ASCII值
#                         # c.append(rsa2.crt(info=ord(msg[i]), e=keys['e'], d=keys['d'], n=keys['n'], p=keys['p'], q=keys['q'], status="en"))
#                         c.append(rsa2.encrypt_update(m=ord(msg[i]), e=keys['e'], n=keys['n']))
#                     cc = "".join(str(c))
#                     print("密文是：{}".format(cc))
#                 elif choose == 2:
#                     for i in range(len(msg)):
#                         # m.append(chr(rsa2.crt(info=c[i], e=keys['e'], d=keys['d'], n=keys['n'], p=keys['p'], q=keys['q'], status="de")))
#                         m.append(chr(rsa1.decrypt_update(c[i], d=keys['d'], n=keys['n'])))
#                     ming = "".join(m)
#                     print("明文：{}".format(ming))
#                     c, m = [], []
#                 elif (choose == 3) or (choose == 4):
#                     break
#                 choose = show()
#
#         elif rsa_type == 3:
#             msg = str(iba.improve_encryption(msg))
#             # keys = rsa1.generate()
#             keys = rsa1.generate_update()
#             choose = show()
#             c, m = [], []
#             while choose != 4:
#                 if choose == 1:
#                     for i in range(len(msg)):
#                         # ord()函数: 返回对应字符的ASCII值
#                         # c.append(rsa2.crt(info=ord(msg[i]), e=keys['e'], d=keys['d'], n=keys['n'], p=keys['p'], q=keys['q'], status="en"))
#                         c.append(rsa2.encrypt(m=ord(msg[i]), e=keys['e'], n=keys['n']))
#                     cc = "".join(str(c))
#                     print("密文是：{}".format(cc))
#                 elif choose == 2:
#                     for i in range(len(msg)):
#                         # m.append(chr(rsa2.crt(info=c[i], e=keys['e'], d=keys['d'], n=keys['n'], p=keys['p'], q=keys['q'], status="de")))
#                         m.append(chr(rsa1.decrypt(c[i], d=keys['d'], n=keys['n'])))
#                     ming = "".join(m)
#                     print("获得加密明文：{}".format(ming))
#                     ming = iba.improve_decryption(ming)
#                     print("最后获得明文：{}".format(ming))
#                     c, m = [], []
#                 elif (choose == 3) or (choose == 4):
#                     break
#                 choose = show()
#
#         elif rsa_type == 4:
#             msg = str(iba.improve_encryption(msg))
#             # keys = rsa1.generate()
#             keys = rsa1.generate_update()
#             choose = show()
#             c, m = [], []
#             while choose != 4:
#                 if choose == 1:
#                     for i in range(len(msg)):
#                         # ord()函数: 返回对应字符的ASCII值
#                         # c.append(rsa2.crt(info=ord(msg[i]), e=keys['e'], d=keys['d'], n=keys['n'], p=keys['p'], q=keys['q'], status="en"))
#                         c.append(rsa1.encrypt_update(m=ord(msg[i]), e=keys['e'], n=keys['n']))
#                     cc = "".join(str(c))
#                     print("密文是：{}".format(cc))
#                 elif choose == 2:
#                     for i in range(len(msg)):
#                         m.append(chr(rsa1.crt(info=c[i], p=keys['p'], q=keys['q'], dp=keys['dp'], dq=keys['dq'], qinv=keys['qinv'])))
#                         # m.append(chr(rsa1.decrypt_update(c[i], d=keys['d'], n=keys['n'])))
#                     ming = "".join(m)
#                     print("获得加密明文：{}".format(ming))
#                     ming = iba.improve_decryption(ming)
#                     print("最后获得明文：{}".format(ming))
#                     c, m = [], []
#                 elif (choose == 3) or (choose == 4):
#                     break
#                 choose = show()
#
#         if choose == 4:
#             break
#         rsa_type = choose_rsa()
    # keys = rsa1.generate()
    # choose = show()
    # while choose != 4:
    #
    #     while choose != 3:
    #
    #         if choose == 1:
    #             for i in range(len(msg)):
    #                 # ord()函数: 返回对应字符的ASCII值
    #                 # c.append(rsa2.crt(info=ord(msg[i]), e=keys['e'], d=keys['d'], n=keys['n'], p=keys['p'], q=keys['q'], status="en"))
    #                 c.append(rsa2.encrypt(m=ord(msg[i]), e=keys['e'], n=keys['n']))
    #             cc = "".join(str(c))
    #             print("密文是：{}".format(cc))
    #         elif choose == 2:
    #             for i in range(len(msg)):
    #                 # m.append(chr(rsa2.crt(info=c[i], e=keys['e'], d=keys['d'], n=keys['n'], p=keys['p'], q=keys['q'], status="de")))
    #                 m.append(chr(rsa1.dencypt(c[i], d=keys['d'], n=keys['n'])))
    #             ming = "".join(m)
    #             print("明文：{}".format(ming))
    #             c, m = [], []
    #         choose = show()
    #
    #     rsa_type = choose_rsa()
    #     choose = show()
