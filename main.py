
from tkinter import *
import pyqrcode
import png
from pyqrcode import QRCode
# font = ImageFont.truetype("GideonRoman-Regular.ttf")


def encrypt():
    pyqrcode.create(EncryptedText.get()).png("Generated.png", scale=8)


root = Tk()
root.title("Steganography")
root.geometry("400x500+500+100")

EncryptedText = StringVar()

EncryptedTextEntry = Entry(root, textvariable=EncryptedText)

button = Button(root, text="Generate", command=encrypt)

EncryptedTextEntry.pack()
button.pack()
root.mainloop()
