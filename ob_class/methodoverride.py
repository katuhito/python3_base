class Page:
    def __init__(self, num, content):
        self.num = num
        self.content = content
    def output(self):
        return f'{self.content}'

# Method OverRide
class TitlePage(Page):
    def output(self):
        # 基底クラスのメソッドは自動では呼ばれないために明示的に呼び出す
        title = super().output()
        return title.upper()

title = TitlePage(0, 'Python Practice Book')
print(title.output())
