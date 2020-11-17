def caesarCipher(s, k):
    e = ""
    for i in s:
        if i.islower():
            e+= chr((ord(i)-97+k)%26+97)
        elif i.isupper():
            e+= chr((ord(i)-65+k)%26+65)
        else:
            e+= i
    return e
input()
s,k = input(), int(input())
print(caesarCipher(s, k))