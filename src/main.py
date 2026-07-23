from port_scanner import run_port_scanner 
from password_checker import password_checker
from file_hash_generator import file_hash_generator 
def main():
    while True:
        print("\n=== CyberScan ===")
        print("1. Port Scanner")
        print("2. Password Strength Checker")
        print("3. File Hash Generator")
        print("4. Network Scanner")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("\nLaunching Port Scanner...")
            run_port_scanner()

        elif choice == "2":
            print("\nOpening Password Strength Checker...")
            password_checker()

        elif choice == "3":
            print("\nOpening File Hash Generator...")
            file_hash_generator()
            
        elif choice == "4":
            print("\nOpening Network Scanner...")

        elif choice == "5":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option. Please choose a number from 1 to 5.") 


if __name__ == "__main__":
    main()