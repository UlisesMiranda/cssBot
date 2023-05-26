
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"D:\Documentos\a\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1138x720")
window.configure(bg = "#F5FDF8")


canvas = Canvas(
    window,
    bg = "#F5FDF8",
    height = 720,
    width = 1138,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    821.6666259765625,
    296.0,
    image=image_image_1
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    316.7642364501953,
    357.955322265625,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=165.756103515625,
    y=27.0,
    width=302.0162658691406,
    height=659.91064453125
)

canvas.create_text(
    164.60975646972656,
    70.25201416015625,
    anchor="nw",
    text="Tu mensaje aparecera aqui...\n",
    fill="#858383",
    font=("Inter", 16 * -1)
)

canvas.create_rectangle(
    566.0,
    608.0,
    1080.0,
    692.0,
    fill="#B80090",
    outline="")

canvas.create_text(
    583.0,
    633.0,
    anchor="nw",
    text="Palabra detectada: ",
    fill="#FFFFFF",
    font=("OpenSansRoman CondensedBold", 32 * -1)
)

canvas.create_text(
    952.0,
    626.0,
    anchor="nw",
    text="A",
    fill="#FFFFFF",
    font=("OpenSansRoman CondensedBold", 36 * -1)
)

canvas.create_rectangle(
    14.0,
    27.0,
    95.86991882324219,
    688.91064453125,
    fill="#FFFFFF",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=25.0,
    y=41.0,
    width=62.0,
    height=104.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=32.536590576171875,
    y=264.11376953125,
    width=48.658538818359375,
    height=54.83740234375
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=30.219512939453125,
    y=343.6666259765625,
    width=48.658538818359375,
    height=54.83740234375
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=30.99188232421875,
    y=410.86181640625,
    width=48.658538818359375,
    height=54.83740234375
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=30.99188232421875,
    y=626.349609375,
    width=48.658538818359375,
    height=54.83740234375
)
window.resizable(False, False)
window.mainloop()
