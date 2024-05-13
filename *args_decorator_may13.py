class input_date:
    def __init__(self):
        name = input("名前を入力してください")
        print("私の名前は" + name + "です")
    def phonenum(self, num):
        print("私の電話番号は" + num + "です")
name = input_date()
# nameというインスタンス作成
name.phonenum("8011111111")
"""
名前を入力してください kame
私の名前はkameです
私の電話番号は8011111111です
"""

class input_date:
    def __init__(self):
        name = input("名前を入力してください")
        print("私の名前は" + name + "です")
    def phonenum(self, num):
        num = input("電話番号を入力してください")
        print("私の電話番号は" + num + "です")


name = input_date()
# nameというインスタンス作成
name.phonenum()
"""
名前を入力してくださいkamei
私の名前はkameiです
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-1-96730d64850c> in <cell line: 12>()
     10 name = input_date()
     11 # nameというインスタンス作成
---> 12 name.phonenum()

TypeError: input_date.phonenum() missing 1 required positional argument: 'num'
"""

# overwrite
class Display:
    def __init__(self):
        print("文章出力できるよ")
    def display(self, sentence):
        print(sentence)
class Display_sub(Display):
    def display(self, sentence):
        print("-" + sentence + "-")
sb_dis = Display_sub()
# display_subクラス内のメソッドを使用したいので、そのクラスのインスタンスを作成
sb_dis.display("あいうえお")
# 上記で作成したインスタンスでdisplayメソッドの呼び出しを行う。
"""
文章出力できるよ
-あいうえお-
"""


def obj():
    return "object"
def free(word):
    return word
def py(func):
    def wrapper(*args, **kwargs):
        return "pythonは" + func(*args, **kwargs)
    return wrapper
pyobj = py(obj)
pyfree = py(free)
print(pyobj())
print(pyfree("楽しい"))
"""pythonはobject
pythonは楽しい"""

def py(func):
    def wrapper(*args, **kwargs):
        return "pythonは" + func(*args, **kwargs)
    return wrapper

@py
def obj():
    return "object"
@py
def free(word):
    return word


print(obj())
print(free("楽しい"))
"""pythonはobject
pythonは楽しい"""

def add_before_after_str(f):
    def before_after_str():
        print('開始')
        f()
        print('終了')
    return before_after_str


def deco1():
    print('テストです')

func = add_before_after_str(deco1)
func()
"""開始
テストです
終了"""

def add_before_after_str(f):
    def before_after_str():
        print('開始')
        f()
        print('終了')

    return before_after_str
def deco1():
    print('テストです')

f = deco1()
add_before_after_str()
"""テストです
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-54-b64affa4a9a8> in <cell line: 12>()
     10 
     11 f = deco1()
---> 12 add_before_after_str()
TypeError: add_before_after_str() missing 1 required positional argument: 'f'
"""

def before_after_str(f):
    def wrapper():
        print("start")
        f()
        print("end")
    return wrapper
@before_after_str
def f():
    print("test")

if __name__ == "__main__":
    f()
"""
start
test
end
"""

def add_before_after_str(f):
    def before_after_str(nanndeyanenn):
        print('開始')
        f(nanndeyanenn)
        print('終了')
    return before_after_str

@add_before_after_str
def deco3(text):
    print(text + '!')

deco3('あと1時間です')
"""開始
あと1時間です!
終了
"""


# デコレートつけてたら関数名違うくてもいいの？元の関数の中に２つ新しい関数がある場合は？
def add_before_after_str(f):
    def example(text):
        f(text)
    return example

    def before_after_str(nanndeyanenn):
        print('開始')
        f(nanndeyanenn)
        print('終了')
    return before_after_str
@add_before_after_str
def deco3(text):
    print(text + '!')

deco3('あと1時間です')
"""あと1時間です!"""


def concat_strings(separator, *args):
    return separator.join(args)


print(concat_strings("-", "apple", "banana", "cherry"))
# 出力: apple-banana-cherry
