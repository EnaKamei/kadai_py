# This is a sample Python script
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def python_name(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def hello(name1):
    print("Helo,World！"+name1)

def ex_input():
    str=input("入力してください")
    print(str)

def ex_input1():
    numbers=int(input("２　整数を入力して"))
    print(numbers)

#3-1
def ex_input31():
    num1 = int(input("３−１　３を加えて表示"))
    print(num1+3)

#3-2
def ex_input32():
    num2 = int(input("入力３−２　３倍にして表示"))
    print(num2 * 3)

#4-1
def ex_condition():
    num41=int(input("整数を入力してください"))
    if num41 > 0:
        print("positive")

#4-2
def ex_condition2():
    num42=int(input("整数を入力してください"))
    if num42 > 0 :
        print("positive")
    elif num42 < 0:
        print("negative")
    elif num42 == 0:
        print("zero")

#No.1 fizzbuzz 1-1
def ex_fizzbuzz():
    value=int(input("整数を入力fizzbuzz"))
    if value % 3 == 0 and value % 5 == 0:
        print("fizzbuzz")
    elif value % 5 == 0:
        print("buzz")
    elif value % 3 == 0:
        print("fizz")

#No.1 fizzbuzz 1-2
def ex_fizzbuzz2():
    value=int(input("fizzbuzz2の整数を入力"))
    if value > 0:
        for x in range(1,value):
            if x % 3 == 0 and x % 5 == 0:
                print("fizzbuzz")
            elif x % 3 == 0:
                print("fizz")
            elif x % 5 == 0:
                print("buzz")
            else :
                print(x)
    else :
        print("正の整数を入力してください。")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    python_name('PyCharm')
    hello(name1="kamei")
    ex_input()
    ex_input1()
    ex_input31()
    ex_input32()
    ex_condition()
    ex_condition2()
    ex_fizzbuzz()
    ex_fizzbuzz2()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# Press the green button in the gutter to run the script.