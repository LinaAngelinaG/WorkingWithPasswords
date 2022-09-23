import random
import string
import hash


def generate(passwords, code, hash_func, words_val, hashlist):
    file_strings = sum(1 for line in open(passwords, 'r', encoding=code))
    try:
        hashfile = open(hashlist, 'w', encoding=code)
        passwordsfile = open(passwords, 'r', encoding=code)
    
        if file_strings > words_val:
            raise IOError("Length of hashlist is less than amount of passwords. Try again.")
    
        max_step = words_val // file_strings
        cur = 0
        next_el = random.randint(0, max_step+1)
    
        while words_val > 0:
            while cur < next_el:
                letters = string.ascii_lowercase
                rand_string = ''.join(random.choice(letters) for i in range(random.randint(10, 21)))
                hashfile.write(hash.count_hash(hash_func, rand_string, code)+'\n')
                cur += 1
                words_val -= 1
    
            if file_strings > 0:
                hashfile.write(hash.count_hash(hash_func, passwordsfile.readline().strip(), code)+'\n')
                file_strings -= 1
                words_val -= 1

                if file_strings > 0 and words_val / file_strings > 1.0:
                    next_el = random.randint(next_el + 1, next_el + words_val // file_strings + 1)
            else:
                next_el = cur + words_val


    finally:
        hashfile.close()
        passwordsfile.close()