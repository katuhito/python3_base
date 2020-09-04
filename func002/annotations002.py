# 変数への型情報の付与
from typing import Optional

def decrement(page_num: int) -> int:
    prev_page: int  #型情報を付けて変数を宣言
    prev_page = page_num -1
    return prev_page

print(decrement(2.0))
