import mysql.connector
db = mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="Gopireddy@4512",
                             database="gopipython")
cur = db.cursor(buffered=True)

def admin_session():
    print("Welcome to admin seesion")
    print()
    print("1.Register new account")
    print("2.Register new teacher")
    print("3.delete student account")
    print("4.delete teacher account")
    print("5.logout session")

    option = input("enter the option to proceed:")
    if option == "1":

def auth_admin():
    print("***Admin Login***")
    username = input("enter the username:")
    passwd = input("enter the password:")
    if username == "Gopireddy":
        if passwd == "Gopireddy@4512":
            admin_session()
        else:
            print("wrong password")
    else:
        print("enter correct details")
def main():
    while 1:
        print("Welcome To College management")
        print("")
        print("1.login as student")
        print("2.login as teacher")
        print("3.login as admin")

        user_option = input("choose option to proceed: ")
        if user_option == "1":
            print("***student login***")
        elif user_option == "2":
            print("***teacher login***")
        elif user_option == "3":
            auth_admin()
        else:
            print("choose correct option")
main()
