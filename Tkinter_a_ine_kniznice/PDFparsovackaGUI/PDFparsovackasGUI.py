import tkinter as tk
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

win = tk.Tk()

canvas = tk.Canvas(win, width = 600, height = 300)
canvas.grid(columnspan=3,rowspan =3) #splits canvas into three identical invisible columns

logo = Image.open("logicko.png")
logo = ImageTk.PhotoImage(logo)
logo_label = tk.Label(image=logo)
logo_label.image = logo
logo_label.grid(column=1,row =0)

#instructions
instructions = tk.Label(win, text="Select a PDF file on your computer to extract all its text")
instructions.grid(columnspan=3,column=0,row=1)

def open_file():
    browse_text.set("loading...")
    file = askopenfile(parent=win,mode="rb",title="Choose a file",filetype=[("Pdf file","*.pdf")])
    if file:
        read_pdf = PyPDF2.PdfReader(file)
        page = read_pdf.pages[0]
        page_content = page.extract_text()
        
        #text box
        text_box = tk.Text(win, height=10, width="50", padx=15,pady=15)
        text_box.insert(1.0,page_content)
        text_box.tag_configure("center", justify= "center")
        text_box.tag_add("center",1.0, "end")
        text_box.grid(column=1, row=3)

        browse_text.set("Browse")


#browse button
browse_text = tk.StringVar()
browse_btn = tk.Button(win, textvariable=browse_text, command=lambda:open_file(), bg = "aquamarine",fg="red",height=2,width=15)
browse_text.set("Browse")
browse_btn.grid(column=1,row=2)


canvas = tk.Canvas(win, width = 600, height = 250)
canvas.grid(columnspan=3)











win.mainloop()