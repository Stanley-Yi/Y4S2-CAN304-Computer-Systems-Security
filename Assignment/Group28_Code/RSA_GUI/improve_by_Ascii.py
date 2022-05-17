import re


# ord()  字母转ASCii码
# chr() ASCii码转字母
# '{:0>8}'.format(str(bin(a))[2:]) 十进制转八位二进制（前面补零）

def convert_to_binary(msg1):  # msg1 是初始输入明文
    total = ''
    for ch in msg1:
        ascii_code = ord(ch)
        eight_digit_binary = '{:0>8}'.format(str(bin(ascii_code))[2:])
        total = total + str(eight_digit_binary)
    return total


# 将msg1的二进制转化为十进制
def convert_to_decimal(binary_msg):
    decimal = int(binary_msg, 2)
    return decimal


def decimal_to_binary(msg2):  # msg2 是经过rsa加密后得到的十进制数字
    binary = bin(msg2)[2:]
    print(binary)
    str_binary = str(binary)
    if len(str(binary)) % 8 != 0:
        digit = len(str(binary)) % 8
        for i in range(8 - digit):
            str_binary = '0' + str_binary
    return str_binary


def divide(binary_msg):  # binary_msg 是由rsa加密后得到的十进制数字转化得到的二进制
    div = re.findall(r'.{8}', binary_msg)
    return div


def convert_to_message(div):
    result = ""
    for i in range(len(div)):
        decimal = int(div[i], 2)
        # print(decimal)
        ch = chr(decimal)
        result = result + ch
    return result


def improve_encryption(msg):
    step1 = convert_to_binary(msg)
    print("明文转为八位二进制：" + step1)
    step2 = convert_to_decimal(step1)
    print("八位二进制转为十进制：" + str(step2))
    return step2


def improve_decryption(msg):
    step1 = decimal_to_binary(int(msg))
    print("解密后转为二进制：" + step1)
    step2 = divide(step1)
    print("将得到的二进制分割为8位一组：" + str(step2))
    step3 = convert_to_message(step2)
    # print(step3)
    return step3


# def encrypt_step456(msg):
#     step4 = decimal_to_binary(msg)
#     print("经过rsa加密后的内容转化为二进制：" + step4)
#     step5 = divide(step4)
#     print("八位切割：" + str(step5))
#     step6 = convert_to_message(step5)
#     print("转化为加密字符：" + step6)
#     return step6


# def decrypt_step12(msg):
#     step1 = convert_to_binary(msg)
#     print("密文转为八位二进制：" + step1)
#     step2 = convert_to_decimal(step1)
#     print("八位二进制转为十进制：" + str(step2))
#     return step2


# def decrypt_step456(msg):
#     step4 = decimal_to_binary(msg)
#     print("经过rsa解密后的内容转化为二进制：" + step4)
#     step5 = divide(step4)
#     print("八位切割：" + str(step5))
#     step6 = convert_to_message(step5)
#     print("转化为明文：" + step6)
#     return step6
