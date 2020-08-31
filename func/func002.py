def increment(page_num):
    return page_num + 1

# 戻り値をnext_pageに格納する
next_page = increment(1)
print(next_page)

a = increment(increment(next_page))
print(a)
