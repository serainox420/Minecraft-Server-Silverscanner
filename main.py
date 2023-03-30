import os

# Set the working directory to the directory where the Python script is located
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
os.system("clear")

while True:
    print("Please select an option:")
    print("1. Execute 'masscan.sh'")
    print("2. Execute 'silver.py'")
    print("3. Exit")
    choice = input("Enter your choice (1, 2 or 3): ")

    if choice == '1':
        os.system("bash masscan.sh")
    elif choice == '2':
        os.system("python3 silver.py")
    elif choice == '3':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
