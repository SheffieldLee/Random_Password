import random
check_code = ''
code ="""abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNPQRSTUVWXYZ0123456789~!@#$%^&*()_+-={}[]:;<>,.?/"""
code_len = 16  # int(input('请输入密码长度：'))
code_count = 1  # int(input('请输入密码个数：'))
count = 0
while count < code_count:
    check_code = ''
    for i in range(code_len):
        j = random.randint(0, len(code)-1)
        check_code += code[j]
    print(check_code)
    count += 1