def first_item(items):
    if items:
        # 空のコンテナオブジェクトは偽になる
        return items[0]
    else:
        return None

first_item(['book'])
first_item([])
