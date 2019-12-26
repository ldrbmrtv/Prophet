from collections import Counter
from math import log
import numpy as np
from part import parts, k_parts
from operator import itemgetter


#Преобразование формата			
def list_to_part(X):

    return list(Counter(X).values())

def matrix_to_part(X):

    M = []
    m = len(X[0])
    for i in range(m):
        M.append([x[i] for x in X])
    
    arr = []
    for line in M:
        arr.append(len(set(line)))

    return arr

#Оценка разбиения
def entr(part):

    n = sum(part)

    inf = [log(x, n) for x in part]
    
    return np.mean(inf)

#Расчет критерия разбиения
def inf_part(y, cash):

    n = len(y)
    k = len(set(y))

    file_name = 'cash_inf_part'
    
    if cash == {}:
        f = open(file_name + '.txt', 'r')
        for line in f.readlines():
            n_str, k_str, val = line.split(' ')
            cash[(int(n_str), int(k_str))] = float(val)
        f.close()

    k_entr = cash.get((n, k))

    if k_entr == None:

        print(k)
        parts = k_parts(n, k)
        inf = []
        for part in parts:
            inf.append(entr(part))

        k_entr = np.mean(inf)
        cash[n, k] = k_entr

        f = open(file_name + '.txt', 'a+')
        f.write('{} {} {}\n'.format(n, k, k_entr))
        f.close()

    return entr(list_to_part(y)) - k_entr

def inf_k(n, k, cash):

    file_name = 'cash_inf_k'
    
    if cash == {}:
        f = open(file_name + '.txt', 'r')
        for line in f.readline():
            n_str, k_str, val = line.split()
            cash[(int(n_str), int(k_str))] = float(val)
        f.close()

    k_entr = cash.get((n, k))

    if k_entr == None:

        print(k)
        parts = k_parts(n, k)
        inf = []
        for part in parts:
            inf.append(entr(part))

        k_entr = sum(inf)
        cash[(n, k)] = k_entr
        f = open(file_name + '.txt', 'w')
        f.write('{} {} {}'.format(n, k, k_entr))
        f.close()

    return k_entr

def get_k(n, cash):

    file_name = 'cash_get_k'
    
    if cash == {}:
        f = open(file_name + '.txt', 'r')
        for line in f.readlines():
            key, val = line.split(' ')
            cash[int(key)] = int(val)
        f.close()
        
    k = cash.get(n)

    if k == None:

        arr = []
        for i in range(1, n+1):
            arr.append([i, 0])

        _parts = parts(n)
        for part in _parts:
            arr[len(part)-1][1] += entr(part)
            
        arr.sort(key=itemgetter(1), reverse = True)
        k = arr[0][0]
        cash[n]=k
        f = open(file_name + '.txt', 'a+')
        f.write('{} {}\n'.format(n, k))

    return k
