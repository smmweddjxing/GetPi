from tqdm import tqdm
from sys import set_int_max_str_digits as set
set(0)
n = int(input("Enter the digits of π     "))
t = n+10
b = 10**t
x1 = b*4//5
x2 = b // -239
s = x1+x2
n *= 2
with tqdm(total=int(n/2)) as pbar:
    for i in range(3, n, 2):
        x1 //= -25
        x2 //= -57121
        x = (x1+x2) // i
        s += x
        pbar.update(1)
pai = s*4
pai //= 10**10
print(pai)
pr=str(input('Do you want to put the text into a file?\nFileName=Yes and put it into &&filename&&.txt\n0=No and Exit the procedure\n:  '))
if not pr == '0':
    with open(f'{pr}.txt', 'w') as f:
        f.write(str(pai))
    print('Progress finished')
input('------------------------------------\nPROGRESS RETURNED VALUE 0\nPress any key+Enter to continue')
