import mysql.connector
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="Gopireddy@4512",
                               database="college_databse")
cur = mydb.cursor(buffered=True)


def student_session(username):
    while 1:
        print("\n***welcome to student session***\n")
        print("\t1.view register")
        print("\t2.download register")
        print("\t3.logout\n")
        option = input("option:")
        if option == "1":
            username = (str(username),)
            cur.execute("select date, username, status from attendence where username = %s", username)
            records = cur.fetchall()
            for record in records:
                print(record)
        elif option == "2":
            username = (str(username),)
            cur.execute("select date, username, status from attendence where username = %s", username)
            records = cur.fetchall()
            for record in records:
                with open("C:/Users/gopir/Desktop/register.txt", 'w') as f:
                    f.write(str(records)+"\n")
                f.close()
            print("all records saved")
        elif option == "3":
            break
        else:
            print("choose correct option")


def teacher_session():
    while 1:
        print("\n***Welcome to teacher session***\n")
        print()
        print("\t1.mark student atendence")
        print("\t2.view register")
        print("\t3.logout\n")
        option = input("option:")
        if option == "1":
            print()
            print("marking the student attendence")
            print()
            cur.execute("select username from users where priviledge = 'student' ")
            records = cur.fetchall()
            date = input("enter date DD/MM/YYYY:")
            for record in records:
                record = str(record).replace("'", "")
                record = str(record).replace(",", "")
                record = str(record).replace("(", "")
                record = str(record).replace(")", "")
                # present | absent | late
                status = input("status for {} is P|A|L".format(record))
                query = (record, date, status)
                cur.execute("insert into attendence(username, date, status) values(%s,%s,%s)", query)
                mydb.commit()
                print("{} marked as {}".format(record, status))
        elif option == "2":
            print("viewing the student register")
            cur.execute("select username, date, status from attendence")
            records = cur.fetchall()
            for record in records:
                print(record)
        elif option == "3":
            break
        else:
            print("please choose correct option")


def admin_session():
    while 1:
        print("\n***Welcome to admin session***\n")
        print("\t1.register new student")
        print("\t2.register new teacher")
        print("\t3.delete existing student")
        print("\t4.delete existing teacher")
        print("\t5.logout\n")
        option = input("enter the option to proceed:")
        if option == "1":
            user_name = input("enter the student name:")
            password = input("enter the student password:")
            query = (user_name, password)
            cur.execute("insert into users(username, password, priviledge) values (%s,%s,'student')", query)
            mydb.commit()
            print(user_name, "has been registered")
        elif option == "2":
            user_name = input("enter the teacher name:")
            password = input("enter the teacher password:")
            query = (user_name, password)
            cur.execute("insert into users(username, password, priviledge) values (%s,%s,'teacher')", query)
            mydb.commit()
            print(user_name, "has been registered")
        elif option == "3":
            print("deleting existing student")
            user_name = input("enter the username to delete record in DB")
            query = (user_name, "student")
            cur.execute("DELETE FROM users WHERE username = %s AND priviledge = %s", query)
            mydb.commit()
            if cur.rowcount < 1:
                print("user not found")
            else:
                print(user_name, "deleted sucessfully")
        elif option == "4":
            print("deleting existing teacher")
            user_name = input("enter the username to delete record in DB:")
            query = (user_name, "teacher")
            cur.execute("DELETE FROM users WHERE username = %s AND priviledge = %s", query)
            mydb.commit()
            if cur.rowcount < 1:
                print("user not found")
            else:
                print(user_name, "deleted sucessfully")
        elif option == "5":
            break
        else:
            print("Choose valid option")


def auth_student():
    print("auth_student")
    username = input("enter student username:")
    password = input("enter the student password:")
    query = (username, password, 'student')
    cur.execute("select username from users where username = %s AND password = %s AND priviledge = %s", query)
    if cur.rowcount <= 0:
        print("student details not recognized")
    else:
        student_session(username)


def auth_teacher():
    print("auth_teacher")
    username = input("enter  teacher username:")
    password = input("enter the teacher password:")
    query = (username, password)
    cur.execute("SELECT * FROM  users WHERE username = %s AND password = %s AND priviledge = 'teacher'", query)
    if cur.rowcount <= 0:
        print("teacher cred's not recognized")
    else:
        teacher_session()


def auth_admin():
    print("\n##Admin_authentication...###\n")
    username = input("enter the ADMIN_username:")
    password = input("enter the ADMIN_password:")
    if username == "Admin":
        if password == "password":
            admin_session()
        else:
            print("wrong password")
    else:
        print("wrong username")


def main():
    while 1:
        print("\n***Welcome To College Management***\n")
        print("\t1.student login")
        print("\t2.Teacher Login")
        print("\t3.Admin login\n")
        user_option = input("enter the option to continue:")
        if user_option == "1":
            auth_student()
        elif user_option == "2":
            auth_teacher()
        elif user_option == "3":
            auth_admin()
        else:
            break


main()
