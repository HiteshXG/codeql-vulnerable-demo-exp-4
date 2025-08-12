import os

def main():
    filename = input("Enter filename to list: ")  # untrusted
    # ❌ VULNERABLE: concatenation passed to os.system
    os.system("ls " + filename)

if __name__ == "__main__":
    main()
