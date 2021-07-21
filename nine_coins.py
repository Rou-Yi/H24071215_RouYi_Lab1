#!/usr/bin/env python
# coding: utf-8

# In[27]:


class Nine_Coins:
    def __init__(self, decimal_num):
        self.decimal = decimal_num
        self.binary = '{0:09b}'.format(decimal_num) ## 使用 format 的 {b} 來轉換成 binary number
        self.coins = '{0:09b}'.format(decimal_num).replace('0', 'H').replace('1', 'T') ## 將 0, 1 轉換成 H, T
        
    def __repr__(self):
        return f'Nine_Coins: {self.coins}'
    
    def __str__(self): 
        return f'binary: {self.binary} and decimal: {self.decimal}'
    
    def toss(self): 
        import random
        self.binary = ''.join(random.sample(self.binary, len(self.binary))) ## 打亂 0, 1 的順序
        self.coins = self.binary.replace('0', 'H').replace('1', 'T') ## 將新的 self.binary 轉換成 H, T
        self.decimal = int(self.binary, 2) ## 將 binary number 轉換成 decimal number

