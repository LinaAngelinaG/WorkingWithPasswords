import string
import time
from random import random, randint, choice

import crack
import gen

if __name__=='test':
    file_results = open("results.txt", 'w')

    for i in range(20):
        file = open("input.txt", 'w')
        iter = randint(100, 500)
        file_results.write(str(iter) + ' ')
        while iter > 0:
            iter -= 1
            letters = string.ascii_lowercase
            rand_string = ''.join(choice(letters) for i in range(randint(10, 21)))
            file.write(rand_string + '\n')
        file.close()
        iter_gener = randint(1000, 2500)
        file_results.write(str(iter_gener) + ' ')
        gen.generate("input.txt", 'utf-8', 'sha1', iter_gener, "output.txt")
        start_time = time.time()
        result = crack.cracking("input.txt", 'utf-8', 'sha1', "output.txt")
        end_time = time.time()
        start_time = end_time - start_time
        summ = 0
        while not result.empty():
            summ += result.get()

        file_results.write('found ' + str(summ) + ' for ' + str(iter / start_time) + ' cand/sec \n')
    file_results.close()