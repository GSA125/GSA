import tkinter

master_window = tkinter.Tk ()
#Menu
menu1 = tkinter.Menu(master_window) 
master_window.config(menu=menu1)
filemenu = tkinter.Menu(menu1, tearoff = 0)
menu1.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New Text File")
filemenu.add_command(label="New File...")
filemenu.add_separator()
filemenu.add_command (label="Open File...")
filemenu.add_separator()
filemenu.add_command (label="Exit", command = master_window.destroy)
                      
master_window.geometry("400x400")    
              
                      




master_window.mainloop ()