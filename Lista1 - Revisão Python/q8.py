# tentativa falha
s = input()
for x in range(len(s)):
    s = s[1:] + s[0]
    print(s)