from time import sleep
import student_detail
class Library:
    def __init__(self,listOfBooks):
        self.books = listOfBooks
    def displayAvailableBooks(self):
        print("Books present in This Library are: ")
        for book in self.books:
            print("-> "+book)
    def borrowBook(self,bookName):
        if bookName in self.books:
            print(f"You have issued {bookName}. Keep it safe and kindly return it within 30 days.")
            self.books.remove(bookName)
            with open("books.txt") as f:
                books=f.read()
            books=books.replace(","+bookName,"")
            with open("books.txt","w") as f:
                f.write(books)
            return True
        else:
            print("Book is not avilable.")
            return False

    def returnBook(self,bookName):
        self.books.append(bookName)
        with open("books.txt","a") as f:
            f.write(f",{bookName}")
        print("Thanks for returning/Donating. Have a great day!")



class Student:
    def requestBook(self):
        self.book = input("Enter The Book Name: ")
        return self.book 
    def returnBook(self):
        self.book = input("Enter The Book Name: ")
        return self.book


if __name__ =="__main__":
    print("***************Welcome to Central Library***************\n")
    for i in range(3):
        student_i=int(input("Enter User Id: ")[:4])
        student_id=f"CL-{student_i}"
        # print(type(student_id))
        # print(student_id)
        students_d=student_detail.student_details()
        # print(students_d)
        std_d_l=list(students_d.keys())
        # print(std_d_l)
        print("Logging on to Central Library Portal...\n")
        sleep(1.5)
        if student_id in std_d_l:
            student_name=students_d[student_id]
            print(f"Welcome, {student_name}")
            break
        else:
            print("StudentId is Incorrect\n")
        
    else:
        print("Try After Some Time")
        sleep(.5)
        print("Thank You!")
        sleep(1)
        exit()
    try:
        with open("books.txt","r") as f:
            l=f.read()
            lst=l.split(",")
    except:
        print("Error books.txt no found!.")
        print("Please Donate some Books.")
        print("If you want to donate some books then press 1.")
        opt=int(input())
        if opt==1:
            book_name=input("Enter Book Name: ")
            with open("books.txt","a") as f:
                f.write(f"{book_name},")
        else:
            sleep(1)
            exit()
    centraLibrary = Library(lst)
    # centraLibrary.displayAvailableBooks()
    Student=Student()
    # print(lst)
    welcomeMsg = "-_-_-_-_-_Welcome To Central Library Portal_-_-_-_-_-_"
    print(welcomeMsg)

    while True:

        options='''\nPlease choose an option:
            1. List all the books.
            2. Request a book.
            3. Donate/Return a book. 
            4. Exit the Library
            '''
        print(options)
        a = int(input("Enter a option: "))

        if a==1:
            centraLibrary.displayAvailableBooks()
        elif a==2:
            centraLibrary.borrowBook(Student.requestBook())
        elif a==3:
            centraLibrary.returnBook(Student.returnBook())
        elif a==4:
            print("''''''Thanks for Using.''''''")
            sleep(1)
            exit()
        else:
            print("Enter a Valid option.")
    