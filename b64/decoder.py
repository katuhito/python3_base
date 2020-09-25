import base64

def base64_to_str(x):
    """base64表現を文字列に変換するb64decode()の戻り値はbytes型であるためdecode()で文字列にしてから返す"""
    return base64.b64decode(x).decode('utf-8')

__all__ = ['base64_to_str']
