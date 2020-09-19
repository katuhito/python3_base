class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content

    def output(self):
        return f'{self.content}'

print('Page')
Page
