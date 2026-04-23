# l=[10,20,25,30,27,40,35] 
# first=second=0
# i=0
# while i<len(l):
#         if l[i]>first and l[i]>second:
#                 second=first
#                 first=l[i]
#         elif l[i]>second and l[i]<first:
#                 second=l[i]
#         i+=1


# print('Second largest',second)                


# a=[321,'Hello',3+5j,10]
# out=[]
# for i in a:
#         if type(i)==int:
#                 for j in str(i):
#                         sum+=int(i)
#                 out+=[sum]  
#                 print(out)                      

books=[]
issued_books=[]
def add_book():
    name=input("Enter the name of :")
    books.append(name)
    print(name,'is added')
def show_books():
    if len(books)==0:
        print("no books available")
    else:
        print("Available books")
        for b in books:
            print(b)
def borrow_book():
    name=input("Enter the book you want to borrow")
    if name in books:
            issued_books.append(name)
            books.remove(name)
            print(name,'is issued')
    else:
         print(name,"Book is not available")   
def return_book():
     name=input("Enter the book you want to return")  
     if name in issued_books :
                        books.append(name) 
                        issued_books.remove(name) 
                        print(name,'is returned') 
     else:
           print("Book is not issued")
def library():                                 
         while True:                          
                print("Menu")
                print("1.Add book")
                print("2.Show book")
                print('3.Borrow book ')
                print('4.Return book')
                print('5.Exit')
                choice=int(input("Enter the choice"))
                if choice==1:
                         add_book()
                elif choice==2:
                        show_books()
                elif choice==3: 
                        borrow_book()
                elif choice==4:
                        return_book()
                elif choice==5:
                        print("Thanku visit again")
                        break
                else:
                 print("Invalid choice")
library()

                      