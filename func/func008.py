# 位置引数、キーワード引数を可変長で受け取る=>どのような引数の呼び出しにも柔軟に対応ができる
def print_pages(*args, **kwargs):
    for content in args:
        print(content)

    for key,value in kwargs.items():
        print(f'{key}: {value}')

print_pages('content1', 'content2', 'content3', published=2020, author='katuhito hara')
