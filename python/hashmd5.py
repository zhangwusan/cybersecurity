import hashlib
import sys

def crack_md5_hash(target_hash, wordlist_file):
    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                # Remove whitespace and newline characters
                password = line.strip()
                
                # Encode and hash the password
                hashed_password = hashlib.md5(password.encode()).hexdigest()
                
                # Compare with the target hash
                if hashed_password == target_hash:
                    return password
        return None
    except FileNotFoundError:
        return "Wordlist file not found."

if __name__ == '__main__':
    # Get the target hash and wordlist file from command line arguments
    if len(sys.argv) != 3:
        print("Usage: python md5_cracker.py <hash> <wordlist_file>")
        sys.exit(1)

    target_hash = sys.argv[1]
    wordlist_file = sys.argv[2]

    cracked_password = crack_md5_hash(target_hash, wordlist_file)
    if cracked_password:
        print(f"Password found: {cracked_password}")
    else:
        print("Password not found in the wordlist.")
