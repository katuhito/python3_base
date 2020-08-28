def get_book(index):
    items = ['note', 'notebook', 'sketchbook']
    try:
        return items[index]
    except (IndexError, TypeError) as e:
        print(f'例外が発生しました:{e}')
        return print('範囲外です')

get_book(3)
