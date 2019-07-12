import os
import subprocess


def menu():  # Selection Menu
    print("-" * 35)
    print("=" * 10 + " Nmap Scans " + "=" * 10)
    print("-" * 35)

    print("1 - Find Host")
    print("2 - Find OS")
    print("3 - Find Port")
    print("4 - Find Port in Range")
    print("5 - Clear")
    print("6 - Exit")
    print()

    choice = int(input("Enter an Option : "))
    if choice == 1:
        findhost()
        menu()
    elif choice == 2:
        findos()
        menu()
    elif choice == 3:
        findport()
        menu()
    elif choice == 4:
        findportrng()
        menu()
    elif choice == 5:
        clear()
        menu()
    elif choice == 6:
        clear()
        exitprog()
    else:
        print("Error! Enter an Option :(")  # Make sure user inputs a number option
        menu()


def findhost():  # Find host
    host = input("Enter an Address: ")
    subprocess.check_call(['nmap', '-n','-v', '-Pn', '-sn','-sL','-PE', '-PP','-oN','hosts.txt', host])


def findos():  # Find host operating system
    sys = input("Enter an Address: ")
    subprocess.check_call(['nmap', '-n','-F','-A','-v', '-Pn','-sS','-O','-oN','findos.txt', sys])


def findport():  # Find ports from address
    port = input("Enter an Address: ")
    subprocess.check_call(['nmap', '-n','-v', '-Pn', '-sV','-oN','ports.txt', port])


def findportrng():  # Find the port range
    port = input("Enter an Address: ")
    subprocess.check_call(['nmap','-p','1-100','-oN','portrng.txt', port])


def clear():  # Clears the console
    os.system('clear||cls')


def exitprog():  # Exits
    quit()


if __name__ == '__main__':
    menu()
