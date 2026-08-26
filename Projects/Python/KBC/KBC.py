'''
Lets Play Kon Banega Crorepati
'''

import pandas as pd
import numpy as np
import random as rd

kbc_QNA = pd.read_csv(r'C:\New folder\KBC - py Project\KBC - QnA.csv', index_col= 'S no')
print(kbc_QNA.head())

win_amount = 0
locked_amount = 0
for q in kbc_QNA.index:
    row = kbc_QNA.loc[q]
    print(f'{q}.', row['Question'])
    print('A.', row['A'], '     ', 'B.', row['B'])
    print('C.', row['C'], '     ', 'D.', row['D'])
    print('For:', row['Price'])

    ans = input('Please choose the correct option: ')
    if ans.upper() == row['Correct']:
        win_amount = int(row['Price']) 
        print('Thats the right answer')
        if q in [4,8,12,14,16]:
            locked_amount = win_amount 
        print(f'You just won {win_amount}')
        print('------------------------------------')
    else:
        print(f'{row['Correct']} Unfortunatly! This is the wrong answer')
        break
else:
    print("Congratulations, you answered all questions!")
    locked_amount = win_amount
    print(f'Your final amount: {locked_amount}')

print(f'Your final amount: {locked_amount}')