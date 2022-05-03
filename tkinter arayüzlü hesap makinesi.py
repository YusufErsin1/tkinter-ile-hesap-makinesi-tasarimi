from tkinter import *
def num(x):
    length=len(entered.get())
    entered.insert(str(length),str(x))
    #print(x)
calcul=5
s1=0
def calculate(x):
    global calcul
    calcul=x
    global s1
    s1=float(entered.get())
    print(calcul)
    print(s1)
    
    entered.delete(0,"end")
s2=0
def last_calculate():
    global s2
    s2=float(entered.get())
    print(s2)
    global calcul
    result=0
    if calcul==0:
        result=s1+s2
    elif calcul == 1 :
        result = abs(s1 - s2)
    elif calcul == 2 :
        result = s1 * s2
    elif calcul == 3 :
        result = float(s1 / s2)
    entered.delete ( 0, "end" )
    entered.insert(0,str(result))

window= Tk()
window.geometry("450x450")

entered= Entry(font=("Vedana",25,"bold"),width=22,justify="right")
entered.place(x=20,y=20)
button=[]
number=0
for i in range(1,10):
    button.append(Button(text=str(i),font=("Vedana",35,"bold"),command=lambda x=i:num(x)))
for i in range(0,3):
    for j  in range (0,3):
        button[number].place(x=40+j*80,y=80+i*80)
        number+=1
cal=[]
for l in range(0,4):
    cal.append(Button(font=("Vedana",40,"bold"),width=2,command=lambda x=l:calculate(x)))
cal[0]["text"]="+"
cal[1]["text"]="-"
cal[2]["text"]="x"
cal[3]["text"]="/"
for l in range(0,4):
    cal[l].place ( x=300, y=80 + l * 82)
zero=Button(text="0", font="Verdana 30 bold",command=lambda x=0:num(x))
zero.place(x=40,y=350)
equal=Button(text="=", fg="RED",font="Verdana 31 bold",command=last_calculate)
equal.place(x=120,y=350)
point=Button(text=".", font="Verdana 31 bold",width=2,wraplength=2,command=lambda x=".":num(x))
point.place(x=200,y=350)
window.mainloop()

