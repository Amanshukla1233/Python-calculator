from tkinter import  *
def click(event):
    global scvalue
    text=event.widget.cget("text")
    print(text)
    if text =="=":
        if scvalue.get().isdigit():
            value=int(scvalue.get())
        else:
            try:
                value=eval(screen.get())
            except Exception as e:
                print(e)
                value="error"

        scvalue.set(value)
        screen.update()
    elif text =="AC":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+text)
        screen.update()

root=Tk()
root.geometry("530x1000")
root.title("Calculator by Aman Shukla ")

scvalue=StringVar()
scvalue.set("")
screen=Entry(root,textvar=scvalue,font="lucida 35 bold")
screen.pack(fill=X,ipadx=8,padx=10,pady=10)

f=Frame(root,bg="grey")
b=Button(f, text="9",padx=28,pady=18,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
b=Button(f, text="8",padx=28,pady=18,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
b=Button(f, text="7",padx=28,pady=18,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f, text="6",padx=28,pady=18,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
b=Button(f, text="5",padx=28,pady=18,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
b=Button(f, text="4",padx=28,pady=18,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f, text="3",padx=28,pady=18,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
b=Button(f, text="2",padx=28,pady=18,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
b=Button(f, text="1",padx=28,pady=18,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f, text="0",padx=31,pady=18,font="lucida 30 bold",bg="red")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
b=Button(f, text="-",padx=31,pady=18,font="lucida 30 bold",bg="blue")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
b=Button(f, text="*",padx=31,pady=18,font="lucida 30 bold",bg="blue")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
f.pack()

f=Frame(root,bg="grey")
b=Button(f, text="/",padx=29,pady=18,font="lucida 30 bold",bg="blue")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
b=Button(f, text="+",padx=29,pady=18,font="lucida 30 bold",bg="blue")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
b=Button(f, text="%",padx=26,pady=18,font="lucida 30 bold",bg="blue")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
f.pack()
f=Frame(root,bg="grey")
b=Button(f, text="=",padx=28,pady=18,font="lucida 30 bold",bg="blue")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)
b=Button(f, text="AC",padx=28,pady=18,font="lucida 30 bold",bg="blue")
b.pack(side=LEFT,padx=18,pady=5)
b.bind("<Button->",click)

f.pack()
root.mainloop()