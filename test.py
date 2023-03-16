import tkinter  as tk 
from tkcalendar import DateEntry
main = tk.Tk()
main.geometry("380x220")  
#pip install tkcalendar

cal=DateEntry(main ,selectmode='day')
cal.grid(row=1,column=1,padx=15)

main.mainloop()