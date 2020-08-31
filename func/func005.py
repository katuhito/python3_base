# 呼び出し時の時刻はデフォルト値をNoneにする
from datetime import datetime

def print_page(content, timestamp=None):
    if timestamp is None:
        timestamp = datetime.now()
        print(content)
        print(timestamp)

print_page('my content')
print_page('my content2')
