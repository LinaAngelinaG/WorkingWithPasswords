import os.path
import pathlib
import crack
import gen
import argparse as args


def work_args():
    parser = args.ArgumentParser()

    parser.add_argument("--func", default='gen', type=str)
    parser.add_argument("--passwords", type=str)
    parser.add_argument("--hashlist", type=str)
    parser.add_argument("--code", default='UTF-8', type=str)
    parser.add_argument("--words_val", default=None, type=int)
    parser.add_argument("--hash_func", default='MD4', type=str)

    all_args = parser.parse_args()


    func = all_args.func
    passwords = all_args.passwords
    hashlist = all_args.hashlist
    code = all_args.code
    hash_func = all_args.hash_func
    words_val = all_args.words_val

    if func.__eq__('gen'):
        if words_val is not None and words_val > 0:
            gen.generate(passwords, code, hash_func, words_val, hashlist)
        else:
            raise IOError("Invalid value of words in output file.")
    else:
        crack.cracking(passwords, code, hash_func, hashlist)
