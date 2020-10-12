class ContextManager:
    # 戻り値がasキーワードに渡される
    def __enter__(self):
        return 1
    def __exit__(self, exc_type, exc_value, traceback):
        pass

with ContextManager() as f:
    print(f)

# asキーワードの省略
with ContextManager():
    pass
