'''
admin features:
1.add student
2.delete student
3.update student
4.time table
5.marks

''' 
from db import connection
def admin():
    conn=connection()
    cursor=conn.cursor()
    print("""\nadmin menu:
    1.add student
    2.update student details
    3.reset student password
    4.update marks
    5.view all students
    6.update timetable
    7.logout
    8.add marks
    9.view marks""")
    ch=int(input("Enter your choice: "))
    if ch==1:
        add_student()
    elif ch==2:
        update_student()
    elif ch==3:
        reset_student_password()
    elif ch==4:
        update_marks()
    elif ch==5:
        view_all_students()
    elif ch==6:
        update_timetable()
    elif ch==7:
        logout()
    elif ch==8:
        add_marks()
    elif ch==9:
        view_marks()
    else:
        print("invalid choice.please try again.")
def add_student():
    conn=connection()
    cursor=conn.cursor()
    roll_no=input("Enter roll no: ")
    name=input("Enter name: ")
    class_name=input("Enter class: ")
    section=input("Enter section: ")
    password="student123"
    email=input("Enter email: ")
    query="insert into students(roll_no,name,class,section,password,email) values(%s,%s,%s,%s,%s,%s)"
    values=(roll_no,name,class_name,section,password,email)
    cursor.execute(query,values)
    conn.commit()
    print("student added successfully.")
def update_student():
    conn=connection()
    cursor=conn.cursor()
    roll_no=input("Enter roll no of student to update: ")
    name=input("Enter new name: ")
    class_name=input("Enter new class: ")
    section=input("Enter new section: ")
    email=input("Enter new email: ")
    query="update students set name=%s,class=%s,section=%s,email=%s where roll_no=%s"
    values=(name,class_name,section,email,roll_no)
    cursor.execute(query,values)
    conn.commit()
    print("student updated successfully")
def 
def reset_student_password():
    pass
def update_marks():
    conn=connection()
    cursor=conn.cursor()
    roll_no=input("enter roll no of student to update marks: ")
    subject=input("enter subject:")
    marks=input("enter marks: ")
    query="update marks set marks=%s where roll_no=%s and subject=%s"
    values=(marks,roll_no,subject)
    cursor.execute(query,values)
    conn.commit()
    print("marks updated successfully.")
def add_marks():
    conn=connection()
    cursor=conn.cursor()
    roll_no=input("enter roll no of student to added marks: ")
    subject=input("enter subject:")
    marks=input("enter marks: ")
    query="insert into marks(roll_no,subject,marks) values(%s,%s,%s)"
    values=(roll_no,subject,marks)
    cursor.execute(query,values)
    conn.commit()
    print("marks added successfully.")

def view_marks():
    conn=connection()
    cursor=conn.cursor()
    query="select * from marks"
    cursor.execute(query)
    results=cursor.fetchall()
    for row in results:
        print(row)

    
def view_all_students():
    conn=connection()
    cursor=conn.cursor()
    query="select * from students"
    cursor.execute(query)
    results=cursor.fetchall()
    for row in results:
        print(row)

def update_timetable():
    pass
def logout():
    print("logging out..")
    return

if __name__ =="__main__":
    admin()

