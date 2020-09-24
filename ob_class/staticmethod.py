class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content

    @staticmethod
    def check_blank(page):
        return bool(page.content)

page = Page(1, '')
print(page.check_blank(page))
