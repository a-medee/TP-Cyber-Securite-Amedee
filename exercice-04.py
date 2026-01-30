from Crypto.Util.strxor import strxor
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def encrypt_image_mode(input_file, mode_name):
    with open(input_file, 'rb') as f:
        header = f.read(54)
        data = f.read()

    key = get_random_bytes(32)
    iv = get_random_bytes(16)

    if mode_name == 'ECB':
        cipher = AES.new(key, AES.MODE_ECB)
    elif mode_name == 'CBC':
        cipher = AES.new(key, AES.MODE_CBC, iv)
    elif mode_name == 'OFB':
        cipher = AES.new(key, AES.MODE_OFB, iv)

    data_padded = pad(data, AES.block_size)

    encrypted_data = cipher.encrypt(data_padded)

    output_file = f"image_{mode_name}.bmp"
    with open(output_file, 'wb') as f:
        f.write(header)
        f.write(encrypted_data)

    print(f"Saved: {output_file}")

with open('test.bmp', 'wb') as f:
    f.write(b'BM' + b'\x00'*52 + b'A'*100)

encrypt_image_mode('test.bmp', 'ECB')
encrypt_image_mode('test.bmp', 'CBC')
encrypt_image_mode('test.bmp', 'OFB')
