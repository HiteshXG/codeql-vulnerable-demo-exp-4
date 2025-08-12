# ❌ VULNERABLE: hardcoded secret
DB_PASSWORD = "SuperSecret123"

def main():
    print("Connecting with password:", DB_PASSWORD)

if __name__ == "__main__":
    main()
