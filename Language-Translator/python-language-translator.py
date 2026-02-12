from tkinter import *
from tkinter import ttk, messagebox
from deep_translator import GoogleTranslator

root = Tk()
root.geometry('1080x400')
root.resizable(False, False)
root.title("Language Translator")
root.config(bg='ghost white')


# ================= HEADING =================

Label(root, text="LANGUAGE TRANSLATOR",
      font="arial 20 bold", bg='white smoke').pack()

Label(root, text="Python 3.13 Compatible Version",
      font='arial 15 bold', bg='white smoke').pack(side='bottom')


# ================= TEXT AREAS =================

Label(root, text="Enter Text",
      font='arial 13 bold', bg='white smoke').place(x=200, y=60)

Input_text = Text(root, font='arial 10',
                  height=11, wrap=WORD, padx=5, pady=5, width=60)
Input_text.place(x=30, y=100)

Label(root, text="Output",
      font='arial 13 bold', bg='white smoke').place(x=780, y=60)

Output_text = Text(root, font='arial 10',
                   height=11, wrap=WORD, padx=5, pady=5, width=60)
Output_text.place(x=600, y=100)


# ================= LANGUAGES =================

languages = [
    "english", "hindi", "bengali", "french",
    "german", "spanish", "urdu", "japanese",
    "chinese", "arabic"
]

src_lang = ttk.Combobox(root, values=languages, width=22)
src_lang.place(x=20, y=60)
src_lang.set('english')

dest_lang = ttk.Combobox(root, values=languages, width=22)
dest_lang.place(x=890, y=60)
dest_lang.set('hindi')


# ================= TRANSLATE FUNCTION =================

def Translate():
    try:
        text = Input_text.get(1.0, END).strip()

        if not text:
            messagebox.showwarning("Warning", "Please enter text to translate.")
            return

        translated = GoogleTranslator(
            source=src_lang.get(),
            target=dest_lang.get()
        ).translate(text)

        Output_text.delete(1.0, END)
        Output_text.insert(END, translated)

    except Exception as e:
        messagebox.showerror("Error", f"Translation failed:\n{e}")


# ================= BUTTON =================

Button(root,
       text='Translate',
       font='arial 12 bold',
       pady=5,
       command=Translate,
       bg='royal blue1',
       activebackground='sky blue').place(x=490, y=180)


root.mainloop()
