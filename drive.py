age = int(input('請輸入您的年齡：'))
country = input('請輸入您的國家：')
if country == '台灣':
    if age >= 18 :
        print('可以考駕照！')
    else :
        print('你還不可以考駕照！')
elif country == '美國':
    if age >= 16 :
    	print('可以考駕照！')
    else :
    	print('你還不可以考駕照！')
else :
	print('你所輸入的國家尚無法判斷！')
