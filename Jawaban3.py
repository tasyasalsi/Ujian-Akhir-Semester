main_window = tkinter.Tk()

def event_klik():
    label2 = tkinter.Label(main_window, text = "halo anjai")
    label2.pack()

    
label = tkinter.Label(main_window, text = "Natasya Salsi Anugrah \n 20210801158")
tombol = tkinter.Button(main_window, text = "klik ini", command = event_klik)

label.pack()
tombol.pack()
main_window.mainloop()
