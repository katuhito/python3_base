# 可変長のキーワード引数を受け取る
def print_page(content, **kwargs):
    print(content)
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_page('my content', published=2019, author='katuhito hara')
