from operator import attrgetter

class Page:
    book_title = 'Python Practice Book'
    def __init__(self, num, content):
        self.num = num
        self.content = content
    def output(self):
        return f'{self.content}'

    @classmethod
    def print_pages(cls, *pages):
        print(cls.book_title)
        pages = list(pages)

        for page in sorted(pages, key=attrgetter('num')):
            print(page.output())



first = Page(1, 'first page')
second = Page(2, 'second page')
third = Page(3, 'third page')

# クラスメソッドの呼び出し
Page.print_pages(first, third, second)

# インスタンスからの呼び出し
first.print_pages(first, third, second)
