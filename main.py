from tkinter import *
from tkinter import messagebox
import PyPDF2
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfile

page_content = []


def output_text_window():
    joined_output = '[Page End]'.join(page_content)

    output_window = Tk()
    output_window.minsize(height=800, width=800)
    output_window.title("PDF Text")

    text_box = Text(output_window, height=50, width=100)
    text_box.insert(1.0, joined_output)
    text_box.grid(column=0)
    browse_text.set("Browse")

    output_window.mainloop()


# Creates GUI Windowloop

window = Tk()
window.title("Applehand's PDF Text Extraction")
window.geometry('600x350')

# Sets height of the window and creates styling grid

canvas = Canvas(window, width=600, height=350, bg="white")
canvas.grid(columnspan=3, rowspan=4)

# Opens image, resizes it, converts image to ImageTk, sets image in label

logo = Image.open('Apple.png')
logo_resized = logo.resize((175, 150))
logo = ImageTk.PhotoImage(logo_resized)
logo_label = Label(image=logo, border=0)
logo_label.image = logo
logo_label.grid(column=1, row=0)

# Directions label

directions = Label(window, text="Browse for a PDF.")
directions.grid(columnspan=3, column=0, row=1)


def open_file():
    browse_text.set("loading..?")
    file = askopenfile(parent=window, mode='rb', title="Choose a file")
    if file:
        read_pdf = PyPDF2.PdfFileReader(file)
        page_count = read_pdf.numPages
        for i in range(page_count):
            page = read_pdf.getPage(i)
            page_content.append(page.extractText())
        output_text_window()

    else:
        browse_text.set("Browse")
        messagebox.showerror("I don't think that's a PDF.")


# Create Browse Button

browse_text = StringVar()
browse_btn = Button(window, textvariable=browse_text, command=lambda: open_file(), bg="#d16666", fg="white", height=2,
                    width=15)
browse_text.set("Browse")
browse_btn.grid(column=1, row=3)

# Ends GUI Windowloop

window.mainloop()