# 可変長の位置引数を受け取る
def print_pages(content, *args):
    print(content)
    for more in args:
        print('more:', more)

# argsは空のタプル
print_pages('my content')

# argsを('content2', 'content3')とする
print_pages('my content', 'content2', 'content3')
