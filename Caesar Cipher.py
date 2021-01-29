ABC = dict(zip("ABCDEFGĞHIİJKLMNOÖPQRSTUVWXYZ",range(26)))
CBA = dict(zip(range(26),"ABCDEFGĞHIİJKLMNOÖPQRSTUVWXYZ"))

key = int(input ("kaç sayı ilerletmek istiyorsunuz "))
plaintext = input ("Metin giriniz ")

ciphertext = ""
for c in plaintext.upper():
    if c.isalpha(): ciphertext += CBA[ (ABC[c] + key)%26 ]
    else: ciphertext += c
print (plaintext)
print (ciphertext)
