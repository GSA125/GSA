import tkinter 

def display_grade ():
    user_input = entry.get().upper()
    
    if user_input == "O":
        label2.config (text = "Outstanding")
    elif user_input == "A":
        label2.config (text = "Very good")
    elif user_input == "B":
        label2.config (text = "Good")   
    elif user_input == "C":
        label2.config (text = "Average") 
    elif user_input == "F":
        label2.config (text = "Fail") 
    else:
        label2.config (text = "Invalid grade")
    



root = tkinter.Tk ()
root.geometry ("400x400")
root.title ("Grade Display GUI")

label1 = tkinter.Label (root, text = "Enter grade (O, A, B, C, or F)")
label1.pack ()

entry = tkinter.Entry (root, width = 10)
entry.pack ()


button = tkinter.Button (root, text = "Submit", command = display_grade)
button.pack ()


label2 = tkinter.Label (root, text = "")
label2.pack ()


root.mainloop ()