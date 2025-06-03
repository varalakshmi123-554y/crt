from db import connection

def student_menu(roll_no):

    while True:

        print("""\nStudent Menu:

1.View Details

2.View Marks

3.View Timetable

4.Logout""")

        choice=input("Enter choice: ")



        if choice=='1':

            view_details(roll_no)

        elif choice=='2':

            view_marks(roll_no)

        elif choice=='3':

            view_timetable(roll_no)

        elif choice=='4':

            change_password(roll_no)

            print("Logging out...")

        else:

            print("Invalid choice.")



def view_details(roll_no):

    conn = connection()

    cur = conn.cursor()

    cur.execute("SELECT * FROM students WHERE roll_no=%s",(roll_no,))

    print("Student Details:")

    print(cur.fetchone())

    conn.close()



def view_marks(roll_no):

    conn = connection()

    cur = conn.cursor()

    roll_no = input("Enter roll no: ")

    cur.execute("SELECT subject, marks FROM marks WHERE roll_no=%s",(roll_no,))


    for row in cur.fetchall():

        print(row)

    conn.close()



view_marks(406)