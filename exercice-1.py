from Crypto.Util import strxor
from Crypto.Random import get_random_bytes

m = "Je suis un ensimien en cinquième année ASTRE et j'adore la cryptographie"
k = "ENSIM"

m = m.encode('utf-8')
k = k.encode('utf-8')

def differentlengthcrypting(m, k):
    message_a_crypter = []
    n = len(k)

    for index in range(0, len(m), n):
        chunk = m[index : index + n]
        current_key = k[:len(chunk)]
        message_a_crypter.append(strxor.strxor(chunk, current_key))

    return b"".join(message_a_crypter)


def decryptingdifferentlengthcrypting(result, k):
    message_a_decrypter = []
    n = len(k)

    for index in range(0, len(result), n):
        chunk = result[index:index + n]
        current_key = k[:len(chunk)]
        message_a_decrypter.append(strxor.strxor(chunk, current_key))

    decrypted_bytes = b"".join(message_a_decrypter)
    m = decrypted_bytes.decode('utf-8')

    return m

print("Message crypte: ")
print(differentlengthcrypting(m, k))

print("Message décrypté")
print(decryptingdifferentlengthcrypting(differentlengthcrypting(m, k), k))
