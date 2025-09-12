import random
def guess_number_game():
    guess_num = random.randint(1,100)

    while True:   #不知到用户几次猜对,用while直到猜对打破循环
        try:
            input_num = int(input("输入一个整数"))
            if input_num == guess_num:
                print(f"猜对了,这个数就是{guess_num}")
                break
            elif input_num < guess_num:
                print("猜小了了,再试一次")
            else:
                print("大了")
        except ValueError:
            print("请输入一个'数字'")

guess_number_game()




