class NotSpecifiedFormatString(BaseException):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

def sumForText(string: str):
    _ = 0
    
    for s in string:
        _ += ord(s)

    return _

def encrypt(text: str, key: str) -> str:
    text_ = ''

    for s in text:
        text_ += str((ord(s) + sumForText(key)) * sumForText(key)) + '_'
    
    return text_

def decrypt(text: str, key: str) -> str:
    text_ = ''

    for i in text.split('_'):
        if i.isdigit():
            text_ += chr(int(int(i) / sumForText(key)) - sumForText(key))
        else:
            if i == '' and text.split('_').index(i) == len(text.split('_')) - 1:
                pass
            else:
                raise NotSpecifiedFormatString(f'Not Specified Format String ({text})')

    return text_

if __name__ == '__main__':
    text = 'SXXYRRY-是星星与然然呀-23XR-星然'
    print(f'原文本：{text}')
    key = 'sxxyrry-23XR'
    print(f'秘钥：{key}')
    en_text = encrypt(text, key)
    print(f'加密后的文本：{en_text}')
    de_text = decrypt(en_text, key)
    print(f'解密后的文本：{de_text}')
    eq_1 = text == de_text
    eq_2 = {'True' : '是', 'False' : '否'}[str(text == de_text)]
    print(f'原文本与解密后的文本是否相等：{eq_1} （{eq_2}）')
