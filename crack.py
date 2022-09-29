from multiprocessing import Process, Queue

import hash


def check_eq(password, hashlist, hash_func, code, counter_found):
    try:
        file_hashwords = open(hashlist, 'r', encoding=code)
        hash_pass = hash.count_hash(hash_func, password, code)
        hash_word = file_hashwords.readline().strip()
        while hash_word:
            if hash_pass.__eq__(hash_word):
                counter_found.put(1)
                print(password + " : " + hash_word)
                break
            hash_word = file_hashwords.readline().strip()
    finally:
        file_hashwords.close()


def cracking(passwords, code, hash_func, hashlist):
    counter_found = Queue()

    try:
        file_passwords = open(passwords, 'r', encoding=code)
        password = file_passwords.readline().strip()
        procs = []
        while password:
            proc = Process(target=check_eq, args=(password, hashlist, hash_func, code,counter_found,))
            procs.append(proc)
            proc.start()
            password = file_passwords.readline().strip()
        for proc in procs:
            proc.join()
        return counter_found
    finally:
        file_passwords.close()
