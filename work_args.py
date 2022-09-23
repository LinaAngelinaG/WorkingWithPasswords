import os.path
import pathlib
import crack
import gen
import argparse as args


def work_args():
    func = get_functional()
    passwords = get_passwords_file_name()
    hashlist = get_hashlist_file_name()
    code = get_code()
    hash_func = get_hash_func()
    words_val = get_words_val()

    if func.__eq__('gen'):
        if words_val is not None & words_val > 0:
            gen.generate(passwords, code, hash_func, words_val, hashlist)
        else:
            raise IOError("Invalid value of words in output file.")
    else:
        path = pathlib.Path(hashlist)
        if path.exists() & path.is_file() & os.path.getsize(path) > 0:
            crack.cracking(passwords, code, hash_func, hashlist)
        else:
            raise IOError("File doesn't exists")


def get_functional():
    parser = args.ArgumentParser()
    parser.add_argument("--func", default='gen', type=str)
    func = parser.parse_args()
    if func.__eq__('gen') | func.__eq__('crack'):
        return func
    else:
        raise IOError("Incorrect functional. Use instead:\n- gen\n- crack")


def get_passwords_file_name():
    parser = args.ArgumentParser()
    parser.add_argument("--passwords", type=str)
    passwords = parser.parse_args()
    path = pathlib.Path(passwords)
    if path.exists() & path.is_file() & os.path.getsize(path) > 0:
        return passwords
    else:
        raise IOError("File doesn't exists")


def get_hashlist_file_name():
    parser = args.ArgumentParser()
    parser.add_argument("--hashlist", type=str)
    hashlist = parser.parse_args()
    return hashlist


def get_code():
    parser = args.ArgumentParser()
    parser.add_argument("--code", default='UTF-8', type=str)
    code = parser.parse_args()
    return code


def get_hash_func():
    parser = args.ArgumentParser()
    parser.add_argument("--hash_func", default='MD4', type=str)
    hash_func = parser.parse_args()
    return hash_func


def get_words_val():
    parser = args.ArgumentParser()
    parser.add_argument("--words_val", default=None, type=int)
    words_val = parser.parse_args()
    return words_val
