# 預設密碼為a123456，使用這最多可輸入3次

key = 'a123456'
print('【最多可以輸入3次密碼】')

#讓使用者輸入設密碼的迴圈

x = 0
y = 2
while x < 3:
	pswd = input('請輸入密碼: ')
	if pswd == key:
		print('登入成功!')
		break
	else:
		print('密碼錯誤!還有', y, '次機會')
		x = x + 1
		y = y - 1 

