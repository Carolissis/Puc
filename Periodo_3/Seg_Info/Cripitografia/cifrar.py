import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from os import urandom

def generate_rsa_keys(bits):
    start_time = time.time()
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=bits,
        backend=default_backend()
    )
    end_time = time.time()
    return private_key, end_time - start_time

def encrypt_rsa(public_key, message):
    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted

def generate_aes_key(key_size):
    return urandom(key_size // 8)

def encrypt_aes(key, message):
    iv = urandom(16)
    cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ct = encryptor.update(message.encode()) + encryptor.finalize()
    return iv + ct

text = "RSA: algorithm from MIT professors: Rivest, Shamir and Adleman"
rsa_key_sizes = [1024, 2048, 4096, 8192]
aes_key_sizes = [128, 256]

for bits in rsa_key_sizes:
    private_key, rsa_gen_time = generate_rsa_keys(bits)
    start_time = time.time()
    encrypted_rsa = encrypt_rsa(private_key.public_key(), text)
    rsa_time = time.time() - start_time
    print(f"RSA {bits}-bit: Key Gen Time: {rsa_gen_time:.4f}, Encryption Time: {rsa_time:.4f}")
for bits in aes_key_sizes:
    aes_key = generate_aes_key(bits)
    start_time = time.time()
    encrypted_aes = encrypt_aes(aes_key, text)
    aes_time = time.time() - start_time
    print(f"AES {bits}-bit: Encryption Time: {aes_time:.4f}")

for bits in rsa_key_sizes:
    private_key, rsa_gen_time = generate_rsa_keys(bits)
    start_time = time.time()
    encrypted_rsa = encrypt_rsa(private_key.public_key(), text)
    rsa_time = time.time() - start_time
    print(f"RSA {bits}-bit: Key Gen Time: {rsa_gen_time:.4f}, Encryption Time: {rsa_time:.4f}")
for bits in aes_key_sizes:
    aes_key = generate_aes_key(bits)
    start_time = time.time()
    encrypted_aes = encrypt_aes(aes_key, text)
    aes_time = time.time() - start_time
    print(f"AES {bits}-bit: Encryption Time: {aes_time:.4f}")

for bits in rsa_key_sizes:
    private_key, rsa_gen_time = generate_rsa_keys(bits)
    start_time = time.time()
    encrypted_rsa = encrypt_rsa(private_key.public_key(), text)
    rsa_time = time.time() - start_time
    print(f"RSA {bits}-bit: Key Gen Time: {rsa_gen_time:.4f}, Encryption Time: {rsa_time:.4f}")
for bits in aes_key_sizes:
    aes_key = generate_aes_key(bits)
    start_time = time.time()
    encrypted_aes = encrypt_aes(aes_key, text)
    aes_time = time.time() - start_time
    print(f"AES {bits}-bit: Encryption Time: {aes_time:.4f}")

for bits in rsa_key_sizes:
    private_key, rsa_gen_time = generate_rsa_keys(bits)
    start_time = time.time()
    encrypted_rsa = encrypt_rsa(private_key.public_key(), text)
    rsa_time = time.time() - start_time
    print(f"RSA {bits}-bit: Key Gen Time: {rsa_gen_time:.4f}, Encryption Time: {rsa_time:.4f}")
for bits in aes_key_sizes:
    aes_key = generate_aes_key(bits)
    start_time = time.time()
    encrypted_aes = encrypt_aes(aes_key, text)
    aes_time = time.time() - start_time
    print(f"AES {bits}-bit: Encryption Time: {aes_time:.4f}")
    
for bits in rsa_key_sizes:
    private_key, rsa_gen_time = generate_rsa_keys(bits)
    start_time = time.time()
    encrypted_rsa = encrypt_rsa(private_key.public_key(), text)
    rsa_time = time.time() - start_time
    print(f"RSA {bits}-bit: Key Gen Time: {rsa_gen_time:.4f}, Encryption Time: {rsa_time:.4f}")
for bits in aes_key_sizes:
    aes_key = generate_aes_key(bits)
    start_time = time.time()
    encrypted_aes = encrypt_aes(aes_key, text)
    aes_time = time.time() - start_time
    print(f"AES {bits}-bit: Encryption Time: {aes_time:.4f}")
