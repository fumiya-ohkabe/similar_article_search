import MeCab
import neologdn
import emoji
import re

def normalize(src_text):
    return neologdn.normalize(src_text)

def remove_punct(src_text):
    p = re.compile('[^a-z\u3041-\u309F\u30A1-\u30FF\u2E80-\u2FDF\u3005-\u3007\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF\U00020000-\U0002EBEF]+')
    return p.sub('', src_text)

def remove_emoji(src_text):
    return ''.join(c for c in src_text if c not in emoji.UNICODE_EMOJI)

def analyzer(text):
    text = normalize(text)
    text = remove_punct(text)
    text = remove_emoji(text)

    # 文章から単語を抽出
    tagger = MeCab.Tagger('-Ochasen')
    tagger.parse('')
    nodes = tagger.parse(text).splitlines()[:-1]
    ret = []

    for node in nodes:
        surface, *feature = node.split('\t')
        if "名詞" in feature[2]:
            ret.append(surface)
        if "形容詞" in feature[2]:
            ret.append(surface)
        if "助動詞" in feature[2]:
            continue
        if "動詞" in feature[2]:
            ret.append(feature[1])

    return ret

if __name__ == '__main__':
    text = "眠いけど彼女はペンパイナッポーアッポーペンと恋ダンスを踊った、az09。"
    ret =analyzer(text)
    print(ret)
