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

    def fizzbuzz_sub(x):
        if x % 3 == 0 and x % 5 == 0:
            return "fizzbuzz"
        elif x % 3 == 0:
            return "fizz"
        elif x % 5 == 0:
            return "buzz"
        else:
            return (x)

    for x in range(1,value+1):
        print(fizzbuzz_sub(x))

if __name__ == "__main__":
    fizzbuzz202()

# comand + option + L で最後フォーマット整えること。