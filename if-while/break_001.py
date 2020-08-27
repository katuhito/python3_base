def has_book(items):
    for item in items:
        if 'book' in item:
            print('Found')
            break
        else:
            print('Not found')

has_book(['note'])
has_book(['note', 'notebook'])

# 上と同じ処理をwhile文で書く
def has_book(items):
    # pop()はリストの内容を変更するのでコピーを作る
    copied = items.copy()
    # 空になるまでループを続ける
    while copied:
        # 最後の要素を取り出す
        item = copied.pop()
        if 'book' in item:
            print('Found')
            break #ループを抜ける
        else:
            print('Not found')

has_book(['note'])
has_book(['note', 'notebook'])
