import hashlib

def generate_checksum(data):
    return hashlib.md5(str(data).encode()).hexdigest()

def verify_integrity(source_data, target_data):
    return generate_checksum(source_data) == generate_checksum(target_data)
