# Learning-Python
#Palindrom kontröl
veri = str(input ("Kelime giriniz "))
if veri[::-1] == veri:
    print('Palindrom uygunluğu vardır.')
else:
    print('Palindrom uygunluğu yoktur')
