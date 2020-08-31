def print_title(printer, title):
    print('@@@@@')

    # 引数printerは関数オブジェクト
    printer(title.upper())
    print('@@@@@')

# print_page関数を定義
def print_page(content):
    print(content)


# print_page関数を渡し、タイトルを印刷
print_title(print_page, 'python practice book')
