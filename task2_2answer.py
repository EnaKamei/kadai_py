def fizzbuzz_sub(x):
    """fizzbuzzの結果を計算する
    :return: 計算結果
    """
    result = ""
    # 3の倍数だったらfizzを追加
    if x % 3 == 0:
        result += "fizz"

    # 5の倍数だったらbuzzを追加
    if x % 5 == 0:
        result += "buzz"

    # どちらにも該当しなかった場合は数値
    if result == "":
        result = str(x)

    return result


def input_data():
    value = -1

    while not value > 0:
        try:
            value = int(input("正の値を入力してください・・・"))
        except ValueError as e:
            continue

    return value


# pattern1
def fizzbuzz202():
    input_value = input_data()

    for x in range(1, input_value + 1):
        result = fizzbuzz_sub(x)
        print(result)


def fizzbuzz201():
    input_value = input_data()

    print(fizzbuzz_sub(input_value))


if __name__ == "__main__":
    # fizzbuzz202()
    fizzbuzz201()

# comand + option + L で最後フォーマット整えること。
