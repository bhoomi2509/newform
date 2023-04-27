from tkinter import*
root=Tk()
root.geometry("500x300")

def getvals():
    print("Accepted..")

Label(root, text="Python Registration form",font="ar 15 bold").grid(row=0,column=3)

#Field name
name = Label(root, text="Name")
phone = Label(root,text="Phone")
gender = Label(root,text="Gender")
emergency = Label(root,text="Emergency")
paymentmood = Label(root,text="Payment mood")

#packing fields
name.grid(row=1, column=2)
phone.grid(row=2, column=2)
gender.grid(row=3, column=2)
emergency.grid(row=4, column=2)
paymentmood.grid(row=5, column=2)

#storing data
namevalue= StringVar
phonevalue=StringVar
gendervalue= StringVar
emergencyvalue=StringVar
paymentmoodvalue=StringVar
checkvalue=IntVar

#entry field
nameentry=Entry(root,textvariable=namevalue)
phoneentry=Entry(root,textvariable=phonevalue)
genderentry=Entry(root,textvariable=gendervalue)
paymentmoodentry=Entry(root,textvariable=paymentmoodvalue)
emergencyentry=Entry(root,textvariable=emergencyvalue)

nameentry.grid(row=1, column=3)
phoneentry.grid(row=2, column=3)
genderentry.grid(row=3, column=3)
emergencyentry.grid(row=4, column=3)
paymentmoodentry.grid(row=5, column=3)


#checkbox
checkbtn= Checkbutton(text="Remember me ?",variable=checkvalue)
checkbtn.grid(row=6, column=3)




#submit button
Button(text="Submit",command=getvals).grid(row=7, column=3)
root.mainloop()