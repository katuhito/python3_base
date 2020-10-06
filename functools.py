from functools import lru_cache
from time import sleep

# try:
#     from functools import lru_cache
# except ImportError:
#     from backports.functools_lru_cache import lru_cach

# 最近の呼び出し最大32回分までキャッシュ
@functools.lru_cache(maxsize=32)
def heavy_function(n):
    sleep(3) #重い処理をシミュレート
    return n + 1

# 初回は時間がかかる
print(heavy_function(2))

# キャッシュにヒットするのですぐに結果を得られる
print(heavy_function(2))


