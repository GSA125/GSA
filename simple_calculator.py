import tkinter

root = tkinter.Tk ()
root.title ("Calculator")
root.geometry ("400x400")

def bmi_call ():
    su_user = entry1.get ()
    sb_user = entry2.get ()
    
    
    Sum = int(su_user)+int(sb_user)
    Sub = int(su_user)-int(sb_user)
    Ml = int(su_user)*int(sb_user)
    Div = int(su_user)/(int(sb_user))
    
    
    
    
    
    
    
    if   Sum_button :
        result.config (text = Sum)
    elif Sub_button:
        result.config (text = Sub)
    elif Mul_button:
        result.config (text = Ml)
    elif  Div_button:
        result.config (text = Div)
    
    
    

label1 = tkinter.Label (root, text="First number")
label1.pack (pady = 1)

entry1 = tkinter.Entry (root, width = 25)
entry1.pack (pady = 1)

label2 = tkinter.Label (root, text = "Second number")
label2.pack (pady = 1)

entry2 = tkinter.Entry (root, width = 25)
entry2.pack (pady = 1)


Sum_button = tkinter.Button (root, text = "Sum", command = bmi_call)
Sum_button.pack (pady = 1)

Sub_button = tkinter.Button (root, text = "Substract", command = bmi_call)
Sub_button.pack (pady = 1)

Mul_button = tkinter.Button (root, text = "Multiply", command = bmi_call)
Mul_button.pack (pady = 1)

Div_button = tkinter.Button (root, text = "Divide", command = bmi_call)
Div_button.pack (pady = 1)



result = tkinter.Label (root, text = "")
result.pack (pady = 1)

root.mainloop ()