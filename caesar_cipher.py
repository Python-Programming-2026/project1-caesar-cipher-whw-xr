def caesar_encrypt(text, shift):
    """
    凯撒密码加密函数
    :param text: 待加密的明文（字符串）
    :param shift: 偏移量（整数，正数右移，负数左移）
    :return: 加密后的密文
    """
    result = ""
    # 遍历每个字符进行加密
    for char in text:
        # 处理大写字母
        if char.isupper():
            # 计算加密后的ASCII码，取模26保证在字母范围内
            result += chr((ord(char) - 65 + shift) % 26 + 65)
        # 处理小写字母
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        # 非字母字符（数字、符号、空格）保持不变
        else:
            result += char
    return result


def caesar_decrypt(cipher_text, shift):
    """
    凯撒密码解密函数（本质是加密的逆过程，偏移量取反）
    :param cipher_text: 待解密的密文（字符串）
    :param shift: 加密时使用的偏移量（整数）
    :return: 解密后的明文
    """
    return caesar_encrypt(cipher_text, -shift)


def brute_force_decrypt(cipher_text):
    """
    暴力破解凯撒密码（遍历所有可能的偏移量）
    :param cipher_text: 待破解的密文（字符串）
    :return: 所有偏移量对应的解密结果（字典）
    """
    results = {}
    for shift in range(26):
        results[shift] = caesar_decrypt(cipher_text, shift)
    return results


def main():
    """
    主函数：提供交互式界面，让用户选择功能并执行
    """
    print("===== 凯撒密码工具 =====")
    print("1. 加密")
    print("2. 解密")
    print("3. 暴力破解")

    # 输入校验：确保用户选择合法的功能
    while True:
        try:
            choice = int(input("\n请选择功能（1/2/3）："))
            if choice not in [1, 2, 3]:
                print("请输入1、2、3中的一个数字！")
                continue
            break
        except ValueError:
            print("输入无效！请输入数字1、2或3。")

    # 加密功能
    if choice == 1:
        text = input("请输入要加密的文本：")
        while True:
            try:
                shift = int(input("请输入偏移量（整数）："))
                break
            except ValueError:
                print("偏移量必须是整数！请重新输入。")
        encrypted = caesar_encrypt(text, shift)
        print(f"加密后的结果：{encrypted}")

    # 解密功能
    elif choice == 2:
        text = input("请输入要解密的文本：")
        while True:
            try:
                shift = int(input("请输入加密时的偏移量："))
                break
            except ValueError:
                print("偏移量必须是整数！请重新输入。")
        decrypted = caesar_decrypt(text, shift)
        print(f"解密后的结果：{decrypted}")

    # 暴力破解功能
    else:
        text = input("请输入要暴力破解的文本：")
        results = brute_force_decrypt(text)
        print("\n暴力破解结果（偏移量: 明文）：")
        for shift, res in results.items():
            print(f"偏移量 {shift}: {res}")


if __name__ == "__main__":
    main()