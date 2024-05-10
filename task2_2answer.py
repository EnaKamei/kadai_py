def fizzbuzz_sub(x):
    """fizzbuzzの結果を計算する
    :return: 計算結果
    """
    result = ""
    if x % 3 == 0 and x % 5 == 0:
        result = "fizzbuzz"
    elif x % 3 == 0:
        result = "fizz"
    elif x % 5 == 0:
        result = "buzz"
    else:
        result = str(x)
    
    return result

# pattern1
def fizzbuzz202():
    value = input("正の値を入力してください・・・")
    try:
        value = int(value)
    except:
        print("自然数を入力してください。")
        fizzbuzz202()
    if value < 0:
        print("正の値を入れてください。")
        fizzbuzz202()

    for x in range(1,value+1):
        print(fizzbuzz_sub(x))

if __name__ == "__main__":
    fizzbuzz202()

# comand + option + L で最後フォーマット整えること。