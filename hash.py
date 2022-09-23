import hashlib
#import Crypto.Hash.MD4 as md4


def count_hash(hash_name, text, code):
    if hash_name.__eq__('MD5') | hash_name.__eq__('md5'):
        return md5(text, code)
    elif hash_name.__eq__('MD4') | hash_name.__eq__('md4'):
        return md4(text, code)
    elif hash_name.__eq__('SHA1') | hash_name.__eq__('sha1'):
        return sha1(text, code)
    elif hash_name.__eq__('SHA256') | hash_name.__eq__('sha256'):
        return sha256(text, code)
    elif hash_name.__eq__('SHA512') | hash_name.__eq__('sha512'):
        return sha512(text, code)
    else:
        raise IOError("Used incorrect hash-function. Use instead:\n- MD4\n- MD5\n- SHA1\n- SHA256\n- SHA512\n")


def md4(text, code):
    return hashlib.new('md4')(text.encode(code)).digest().decode(code)


def md5(text, code):
    return hashlib.md5(text.encode(code)).digest().decode(code)


def sha1(text, code):
    bytess = hashlib.sha1(text.encode(code)).hexdigest()
    return bytess


def sha256(text, code):
    return bytes.decode(hashlib.sha256(text.encode(code)).digest(), encoding=code)


def sha512(text, code):
    return bytes.decode(hashlib.sha512(text.encode(code)).digest(), encoding=code)