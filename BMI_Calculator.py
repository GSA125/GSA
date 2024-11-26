import tkinter

root = tkinter.Tk ()
root.title ("BMI Calculator")
root.geometry ("400x400")

def bmi_call ():
    kg_user = entry2.get ()
    hg_user = entry1.get ()
    bmi = float(kg_user)/(float(hg_user)*float(hg_user))
    if bmi <18.4:
        status.config (text = "Underweight")
    elif 24.9 > bmi > 18.5 :
        status.config (text = "Normal")
    elif 39.9 > bmi > 25.0 :
        status.config (text = "Overweight")
    elif 40.0 < bmi:
        status.config (text = "Obeses")
    result.config (text = f"BMI = {bmi}")
    

label1 = tkinter.Label (root, text="Enter your height in meters:")
label1.pack (pady = 10)

entry1 = tkinter.Entry (root, width = 10)
entry1.pack (pady = 10)

label2 = tkinter.Label (root, text = "Enter your weight in kilograms:")
label2.pack (pady = 10)

entry2 = tkinter.Entry (root, width = 10)
entry2.pack (pady = 10)


button = tkinter.Button (root, text = "Calculate BMI", command = bmi_call)
button.pack (pady = 10)

result = tkinter.Label (root, text = "")
result.pack (pady = 10)

status = tkinter.Label (root, text = "")
status.pack (pady = 10)

root.mainloop ()