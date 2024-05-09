#No.2じゃんけん
def janken():
    import random
    num = random.randint(0, 2)

    y = int(input("最初はぐー、じゃんけん・・・ぐーなら0、ちょきなら1、パーなら2を入力してください。"))
    if y == 0:
        print("貴方・・・ぐー")
        if num == 0:
            print("相手はグーでした。あいこです。")
        elif num == 1:
            print("相手はチョキでした。あなたの勝ちです！")
        elif num == 2:
            print("相手はパーでした。あなたの負けです！")
    elif y == 1:
        print("貴方・・・ちょき")
        if num == 0:
            print("相手はグーでした。貴方の負けです！")
        elif num == 2:
            print("相手はチョキでした。あいこです。")
        elif num == 3:
            print("相手はパーでした。あなたの勝ちです！")
    elif y == 2:
        print("貴方・・・ぱー")
        if num == 0:
            print("相手はグーでした。あなたの勝ちです！")
        elif num == 2:
            print("相手はチョキでした。貴方の負けです！")
        elif num == 3:
            print("相手はパーでした。あいこです！")
    else:
        print("そんな手はありません。")




if __name__ == '__main__':
   janken()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/