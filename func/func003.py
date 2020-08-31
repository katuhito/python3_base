def increment(page_num, last):
    next_page = page_num + 1
    if next_page <= last:
        return next_page
    raise ValeError('Invalid arguments')

b = increment(1, 3)
print(b)

c = increment(3, 3)
print(c)
