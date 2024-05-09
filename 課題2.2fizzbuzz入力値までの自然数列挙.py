
#pattern1
def fizzbuzz202():
    value = input("正の値を入力してください・・・")
    try:
        value = int(value)
    except:
        print("自然数を入力してください。")
        return fizzbuzz202()
    if value < 0:
        print("正の値を入れてください。")
        return  fizzbuzz202()
    for x in range(1,value):
        if x % 3 ==0 and value % 5 ==0:
             print("fizzbuzz")
        elif x % 3 ==0:
            print("fizz")
        elif x % 5 ==0:
            print("buzz")
        else :
            print(x)

if __name__ =="__main__":
    fizzbuzz202()

















