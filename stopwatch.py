import tkinter 
import time
import tkinter.messagebox

screen=tkinter.Tk()
screen.geometry("300x200")
screen.title("Stopwatch")

hour=tkinter.StringVar()

minutes=tkinter.StringVar()

sec=tkinter.StringVar()

hour.set("00")
minutes.set("00")
sec.set("00")

def start():
    s=int(sec.get())
    m=int(minutes.get())
    h=int(hour.get())
    
    while not (h==0 and m==0 and s==0):
        s-=1
        if h>0 and m==0 and s==0:
            h-=1
            m=59
            s=59

        if s==0 and m>0:
            m-=1
            s+=60

        if h==0 and m==0 and s==0:
    
            tkinter.messagebox.showinfo("time is up","time is up")
            break
        sec.set(s)
        minutes.set(m)
        hour.set(h)
        screen.update()
        time.sleep(1)


    



entry1=tkinter.Entry(screen, width=5, textvariable=hour)
entry1.grid(row=1, column=1, padx=20)

entry2=tkinter.Entry(screen, width=5, textvariable=minutes)
entry2.grid(row=1, column=2, padx=20)

entry3=tkinter.Entry(screen, width=5, textvariable=sec)
entry3.grid(row=1, column=3, pady=50, padx=20)

button=tkinter.Button(screen, text="Start", command=start)
button.grid(row=2, column=2)

screen.mainloop()