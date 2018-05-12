# Системы счисления
numb2 = int('101', 2) # 5
numb8 = int('713', 8) # 459
numb16 = int('f1a', 16) # 3866

# Перевод в двоичную
bin(459) # '0b111001011'
# Перевод в восьмеричную 
oct(459) # '0o713'
# Перевод в шестнадцатеричную 
hex(459) # '0x1cb'

bace = 8 
x = int(input()) # 459
digit = ''
while x > 0:
	digit = str(x % bace) + digit
	x //= bace
print(digit) # 713