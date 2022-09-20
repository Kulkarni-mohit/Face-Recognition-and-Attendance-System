from tkinter import *
from PIL import Image , ImageTk
import os
import cv2 as cv
import time
import Face_Detection as fd

def tab1():

    global No_of_photos
    global name_of_student
    #var.get()

    root1 = Toplevel()
    root1.geometry("800x533+300+50")
    root1.title('Face Detection Attendence system')
    #root1.iconbitmap(r'C:\Users\harsh\OneDrive\Desktop\Engineering Notes\icon.ico')
    img = ImageTk.PhotoImage(file='gjg.jpg')
    bg = Label(root1,image=img).place(x=0,y=0)

    Label(root1,text='Capture Images',font=("Ariel",20,),bg='white', fg='black').place(x=300,y=50)

    Label(root1,text='Name Of the Student:',font=("Ariel",15,)).place(x=100,y=200)
    name_of_student = Entry(root1, width=30)
    name_of_student.place(x=350,y=200)
    #Ent = Entry(root1,bg="blue")
    #Ent.place(x=50,y=50)

    Label(root1,text='Number of photos:', font=("Ariel",15,)).place(x=100,y=300)
    No_of_photos = Entry(root1,width=30)
    No_of_photos.place(x=350,y=300)

    btn=Button(root1,text='submit',bg='green', height = 3, width = 15,font=("Ariel",15,),command = name)
    btn.place(x=250,y=400)



    #img = ImageTk.PhotoImage(file=r'C:\Users\harsh\OneDrive\Desktop\Engineering Notes\ai.jpeg')
   # bg = Label(root,image=img).place(x=0,y=0)

    root1.mainloop()


def name():
    captureimages(name_of_student.get(), int(No_of_photos.get()))
    

def captureimages(name, no_of_images=60):
    """
    name --> name of directory to be made
    """
    os.chdir('Faces')
    os.mkdir(name)
    os.chdir(name)
    
    capture = cv.VideoCapture(0)

    i = no_of_images
    while True:
        istrue, frame = capture.read()

        time.sleep(1)
        filename = name+str(i)+'.jpg'
        cv.imwrite(filename, frame)
        i-=1
        if i == 0:
            break

    capture.release()
    cv.destroyAllWindows()


def mark_attendance():
    fd.Face_detection('dnn')
    

root=Tk()

root.title("Face Detection Attendence system")
root.geometry("800x533+300+50")
#root.iconbitmap(r'C:\Users\harsh\OneDrive\Desktop\Engineering Notes\icon.ico')

img = ImageTk.PhotoImage(file='gjg.jpg')
bg = Label(root,image=img).place(x=0,y=0)



label=Label(root,font=("Ariel",20,),text="Welcome To AI Based Face Detection Attendence System",bg='white', fg='black')
label.place(x=50,y=40)

btn1=Button(root,text="Mark Attendence",bg="green",fg="white" , command =mark_attendance) 
btn1.place(x=590,y=180, height=50,width=150)

btn2=Button(root,text="Add Student",bg="green",fg="white", command=tab1)
btn2.place(x=590,y=300, height=50,width=150)




root.mainloop()
