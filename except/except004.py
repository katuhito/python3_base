def get_book(index):
    items = ['note', 'notebook', 'sketchbook']
    try:
        return items[index]
    except TypeError:
        print(f'TypeErrorが発生しました')
        return print('範囲外です')

def get_book_wrapper(index):
    try:
        return get_book(index)
    except IndexError:
        print(f'IndexErrorが発生しました')
        return print('範囲外です')

get_book_wrapper(3)
