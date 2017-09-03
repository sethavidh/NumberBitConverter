'''
   find bit representation of an input number
   by Sethavidh Gertphol
   Sep 3, 2017
   
   now works with integers only
'''

number = int(input())
if number >= 0:
    bit_all = bin(number)[2:]
    print((bit_all+':')*3, bit_all)
else:
    print('-:',end='')
    bin_bit = bin(number)[3:]
    pos_left = 7 - len(bin_bit) 
    sign_mag = '1' + '0'* pos_left + bin_bit
    print(sign_mag+':',end='')
    
    invert_bit = ''
    for b in bin_bit:
        if b == '1':
            invert_bit += '0'
        else:
            invert_bit += '1'
    one_comp = '1' + '1'* pos_left + invert_bit
    print(one_comp+':',end='')
    
    two_comp = ''
    mask = 1
    for i in range(8): 
        bit = (number & mask) >> i
        two_comp = str(bit) + two_comp
        mask = mask << 1
    print(two_comp)