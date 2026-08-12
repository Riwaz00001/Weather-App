from customtkinter import *
def error_message(message):
    window=CTk()
    window.title("Error!!!")
    label=CTkLabel(master=window,text=message,font=("Arial",20))
    label.pack(padx=40,pady=40)
    window.update_idletasks()
    window.mainloop()
if __name__=="__main__":
    error_message("Testing")