def generate_hash(input_data):
    import hashlib
    md5_hash = hashlib.md5(input_data.encode()).hexdigest()
    sha1_hash = hashlib.sha1(input_data.encode()).hexdigest()
    sha256_hash = hashlib.sha256(input_data.encode()).hexdigest()

    print("MD5 Hash:", md5_hash)
    print("SHA1 Hash:", sha1_hash)
    print("SHA256 Hash:", sha256_hash)

input_data = input("Enter a string: ")
generate_hash(input_data)