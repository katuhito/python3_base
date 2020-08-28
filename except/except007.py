from io import UnsupportedOperation

# ファイルを読み取りモードでオープン
f = open('some.txt', 'r')
try:
    f.read()
# except UnsupportedOperation as e:
#     print(f'例外が発生しました: {e}')
finally:
    print('ファイルをクローズします')
    f.close()
    
