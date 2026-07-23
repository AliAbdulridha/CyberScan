import hashlib


def file_hash_generator():
    file_path = input("Enter the file path: ")

    try:
        with open(file_path, "rb") as file:
            data = file.read()
            sha256_hash = hashlib.sha256(data).hexdigest()

        print(f"\nSHA-256 Hash:\n{sha256_hash}")

    except FileNotFoundError:
        print("File not found.")
        return