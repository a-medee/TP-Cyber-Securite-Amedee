from Crypto.Util.strxor import strxor

c = [1, 51, 42, 51, 44, 109, 107, 51, 44, 52, 56, 101, 48, 32, 61, 32, 57, 97, 62, 49, 42, 45, 34,
     54, 38, 51, 107, 41, 38, 97, 40, 45, 42, 39, 45, 55, 38, 44, 46, 43, 55, 97, 59, 36, 49, 97, 51, 42, 49, 97, 46, 43, 99, 17, 50, 49, 43, 46, 37, 101, 98]
k = "CAKE"

def list_of_number_decryption(c, k):
    c = bytes(c)
    k = k.encode('utf-8')
    n = len(k)
    message_a_decrypter = []

    for index in range(0, len(c), n):
        chunk = c[index : index + n]
        current_key = k[:len(chunk)]
        message_a_decrypter.append(strxor(chunk, current_key))

    message_a_decrypter = b"".join(message_a_decrypter).decode('utf-8')

    return message_a_decrypter

print("Message à décrypter")
print(list_of_number_decryption(c, k))
