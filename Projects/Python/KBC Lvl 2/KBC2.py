'''
Lets Play Kon Banega Crorepati - advance modifications
'''

import pandas as pd
import numpy as np
import random as rd

price_map = {
    '1' : 1000, '2' : 2000, '3' : 3000, '4' : 5000,
    '5' : 10000, '6' : 20000, '7' : 40000, '8' : 80000,
    '9' : 160000, '10' : 320000, '11' : 640000, '12' : 1250000,
    '13' : 2500000, '14' : 5000000, '15' : 7500000, '16' : 10000000
}

kbc_QNA = pd.read_csv(r"C:\New folder\KBC - py Project\KBC2 - QnA.csv").sample(n=16).reset_index(drop=True)
kbc_QNA.index = kbc_QNA.index + 1
print(kbc_QNA.head())

win_amount = 0
locked_amount = 0
for q in kbc_QNA.index:
    row = kbc_QNA.loc[q]
    print(f'{q}.', row['Question'])
    print('A.', row['A'], '     ', 'B.', row['B'])
    print('C.', row['C'], '     ', 'D.', row['D'])
    print('For:', price_map[str(q)])

    ans = input('Please choose the correct option: ')
    if ans.upper() == row['Correct']:
        win_amount = price_map[str(q)] 
        print('Thats the right answer')
        if q in [4,8,12,14,16]:
            locked_amount = win_amount 
        print(f'You just won {win_amount}')
        print('------------------------------------')
    else:
        print(f'{row['Correct']} Unfortunatly! This is the wrong answer')
        break
    
print("Congratulations, you answered all questions!")
print(f'Your final amount: {locked_amount}')
