# lambda式で関数を定義する
increment = lambda num: num + 1
print(increment(2))

# このlambda式と同等の通常の関数定義
def increment(num):
    return print(num + 1)

nums = ['one', 'two', 'three']

filtered = filter(lambda x: len(x) == 3, nums) #ラムダ式による関数定義
print(list(filtered))
