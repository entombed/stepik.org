import simplecrypt

with open("encrypted.bin", "rb") as efile:
    encrypted = efile.read()
with open('passwords.txt', 'r') as pfile:
    for line in pfile:
        try:
            text = simplecrypt.decrypt(line.strip(), encrypted)
            print(text.decode("utf-8"))
            break
        except simplecrypt.DecryptionException:
            pass
