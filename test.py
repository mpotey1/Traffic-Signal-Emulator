from Tkinter import *
import time
from time import sleep

#Creating a tkinter object
window = Tk()
#Creating Canvas of the entire GUI
canvas = Canvas(window, width=280, height=275)
canvas.pack()

#Creating global variables for interactivity between functions
str1 = StringVar()
str2 = StringVar()
str3 = StringVar()
running = True

#Signal looping function
def signal_loop(val1,val2,val3):
    global running
    T.configure(state='normal')
    T.delete(1.0,END)
    T.configure(state='disabled')
    #Signal loop
    while running == True:
        #For loop for red light. Will run for n times and will sleep for one second in every interation
        for i in range(val1):
            #If condition in the loop to check if the running value was set to False
            if running == False:
                break
            canvas.create_oval(5,5,50,50, fill="red")
            window.update()
            time.sleep(1)
        #Setting the color back to white
        canvas.create_oval(5,5,50,50, fill="white")
        window.update()
        time.sleep(0.05)

        #For loop for orange light. Will run for n times and will sleep for one second in every interation
        for i in range(val2):
            #If condition in the loop to check if the running value was set to False
            if running == False:
                break
            canvas.create_oval(5,55,50,100, fill="orange")
            window.update()
            time.sleep(1)
        #Setting the color back to white
        canvas.create_oval(5,55,50,100, fill="white")
        window.update()
        time.sleep(0.05)

        #For loop for green light. Will run for n times and will sleep for one second in every interation
        for i in range(val3):
            #If condition in the loop to check if the running value was set to False
            if running == False:
                break
            canvas.create_oval(5,105,50,150, fill="green")
            window.update()
            time.sleep(1)
        #Setting the color back to white
        canvas.create_oval(5,105,50,150, fill="white")
        window.update()
        time.sleep(0.05)



def start_traffic():
    global str1,str2,str3,running
    running = True

    #Checking if any input field is empty
    if str1.get()=='' or str2.get()=='' or str3.get()=='':
        T.configure(state='normal')
        T.delete(1.0,END)
        T.insert(END,'Input ')
        if str1.get()=='':
            T.insert(END,'Red ')
        if str2.get()=='':
            T.insert(END,'Orange ')
        if str3.get()=='':
            T.insert(END,'Green ')
        T.insert(END,'empty.\nPlease enter integer value.')
        T.configure(state='disabled')
        running=False
        return

    #Checking for all characters except number by typecasting the string input to integer
    try:
        val1 = int(str1.get())
    except ValueError:
        T.configure(state='normal')
        T.delete(1.0,END)
        T.insert(END,'Please enter an integer value\nfor Red')
        T.configure(state='disabled')
        running=False
        return
    try:
        val2 = int(str2.get())
    except ValueError:
        T.configure(state='normal')
        T.delete(1.0,END)
        T.insert(END,'Please enter an integer value\nfor Orange')
        T.configure(state='disabled')
        running=False
        return
    try:
        val3 = int(str3.get())
    except ValueError:
        T.configure(state='normal')
        T.delete(1.0,END)
        T.insert(END,'Please enter an integer value\nfor Green')
        T.configure(state='disabled')
        running=False
        return

    #Checking if the values in the input boxes are > 0
    if val1<=0 or val2<=0 or val3<=0:
        T.configure(state='normal')
        T.delete(1.0,END)
        T.insert(END,'Please enter value greater\nthan 0 for ')
        if val1<=0:
            T.insert(END,'Red ')
        if val2<=0:
            T.insert(END,'Orange ')
        if val3<=0:
            T.insert(END,'Green ')
        T.configure(state='disabled')
        running=False
        return
    #Calling the signal_loop function to start the simulator
    signal_loop(val1,val2,val3)


def stop_traffic():
    #Setting the global variable false so that the signal_loop terminates on checking the running = False condition
    global running
    running = False


def quit_traffic():
    #Turning running variable false to stop the lights loop
    global running
    running = False
    #explicitly setting the color canvas to white so that it doesn't have wait for the signal_loop to terminate
    canvas.create_oval(5,5,50,50, fill="white")
    canvas.create_oval(5,55,50,100, fill="white")
    canvas.create_oval(5,105,50,150, fill="white")
    #Putting in the exiting message to the log box and sleeping for 1.5 seconds
    T.configure(state='normal')
    T.delete(1.0,END)
    T.insert(END,'Exiting Traffic Light\nSimulator')
    window.update()
    time.sleep(1.5)
    T.configure(state='disabled')
    #exiting the GUI
    window.quit()


#Creating Start,Stop,Quit buttons
button1 = Button(window, text="Start", command=start_traffic)
button1.place(x=5, y=255)
button2 = Button(window, text="Stop", command=stop_traffic)
button2.place(x=50, y=255)
button3 = Button(window, text="Quit", command=quit_traffic)
button3.place(x=95, y=255)

#Creating initial canvas ovals and filling them with white marking the initialization of the signal
canvas.create_rectangle(2,2,52,152,fill="black")
canvas.create_oval(5,5,50,50, fill="white")
canvas.create_oval(5,55,50,100, fill ="white")
canvas.create_oval(5,105,50,150, fill="white")

#Creating all the text fields and input boxes
#Creating tips and usage manual text box
textu=Text(window,height=9,width=26)
textu.place(x=60,y=5)
textu.insert(END,'Usage:\n1)Put in value in seconds next to color name.\nE.g. : Red: 1\n2)Only integer values\nacceptable.\n3)Start button starts sim.\n4)Stop button stops sim.\n5)Quit button quits sim.')
textu.configure(state='disabled')

#Creating logs text
textl=Text(window,height=0.5,width=4)
textl.place(x=1,y=215)
textl.insert(END,'Log:')
textl.configure(state='disabled')

#Creating a text box for all the logs
T = Text(window, height=2, width=30,state='disabled')
T.place(x=35,y=215)


#Creating input box1 for accepting red light's timing
text1=Text(window,height=0.5,width=5)
text1.place(x=1,y=185)
text1.insert(END,'Red:')
text1.configure(state='disabled')
entry1 = Entry(window, textvariable = str1, width=5)
entry1.place(x=40,y=185)

#Creating input box2 for accepting orange light's timing
text2=Text(window,height=0.5,width=7)
text2.place(x=80,y=185)
text2.insert(END,'Orange:')
text2.configure(state='disabled')
entry2 = Entry(window, textvariable = str2, width=5)
entry2.place(x=140,y=185)

#Creating input box3 for accepting green light's timing
text3=Text(window,height=0.5,width=6)
text3.place(x=180,y=185)
text3.insert(END,'Green:')
text3.configure(state='disabled')
entry3 = Entry(window, textvariable = str3, width=5)
entry3.place(x=230,y=185)

#Starting the GUI window loop
window.mainloop()
