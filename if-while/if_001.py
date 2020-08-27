import sys

def py2_or_py3():
    major = sys.version_info.major
    if major == 2:
        return print('Python2')
    elif major == 3:
        return print('Python3')
    else:
        return 'Neither'

py2_or_py3()
