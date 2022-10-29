
from tkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
import base64
import os

class LoginForm:
    def __init__(self,window):
        self.window = window
        #self.window.geometry('1166x718')
        self.window.geometry('1920x1080')
        self.window.resizable(0,0)
        window.title("Encryption and Decryption Tool")

        self.frame1 = Image.open('pic\\pic3.jpg')
        photo = ImageTk.PhotoImage(self.frame1)
        self.panel1 = Label(self.window,image=photo)
        self.panel1.image = photo
        self.panel1.pack(fill='both', expand='yes')

        #frame
        self.frame2 = Frame(self.window, bg='#040405', width='1500', height='1000')
        self.frame2.place(x=200, y=50)
        #frame heading
        self.txt = 'Welcome'
        self.heading = Label(self.frame2, text=self.txt, font=('yu gothic ui', 45, 'bold'),bg='#040405',fg='white')
        self.heading.place(x=250, y=100, width=300, height=60)

        #frame text
        self.txt = 'Cryptography is used to secure and protect data during\n communication. It is helpful to prevent unauthorized \nperson or group of users from accessing any confidential\n data. Encryption and decryption are the two essential\n functionalities of cryptography. A message sent over\n the network is transformed into an unrecognizable\n encrypted message known as data encryption. At the\n receiving end, the received message is converted to \nits original form known as decryption.'
        self.info = Label(self.frame2, text=self.txt, font=('yu gothic ui', 20, 'bold'),bg='#040405',fg='white')
        self.info.place(x=50, y=180, width=700, height=600)

        self.txt = 'Give it a try !'
        self.info = Label(self.frame2, text=self.txt, font=('yu gothic ui', 22, 'bold'),bg='#040405',fg='white')
        self.info.place(x=250, y=680, width=300, height=60)


        #image
        self.image1 = Image.open('pic\\pngwing.com (1).png')
        resized_image = self.image1.resize((400, 400), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resized_image)
        self.image1_label = Label(self.frame2, image=new_image, bg = '#040405')
        self.image1_label.image = new_image
        self.image1_label.place(x=860, y=100)

        #text
        self.label1 = Label(self.frame2, text='Encryption and Decryption Tool', bg='#040405', fg='white',
                                        font=('yu gothic ui', 22, 'bold'))
        self.label1.place(x=860, y=550)

        #button
        Button(self.frame2, text="Create Secret Messages",font=('calibri', 15,'bold'), height="3", width=40, bg='#F5B041', fg="white", bd=0, cursor='hand2',activebackground='#F1C40F', command=self.openNewWindow).place(
            x=880, y=650)

    #tool window
    def openNewWindow(self):
        def decrypt():
            password = code.get()

            if password == "1234":
                screen2 = Toplevel(screen)
                screen2.title("decryption")
                screen2.geometry("400x200")
                screen2.configure(bg="#186A3B")
                message = text1.get(1.0, END)
                decode_message = message.encode("ascii")
                base64_bytes = base64.b64decode(decode_message)
                decrypt = base64_bytes.decode("ascii")

                Label(screen2, text="Decrypt", font="arial", fg="white", bg="#186A3B").place(x=10, y=0)
                text2 = Text(screen2, font="Rpbota 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
                text2.place(x=10, y=40, width=380, height=150)

                text2.insert(END, decrypt)

            elif password == "":
                messagebox.showerror("encryption", "Input Password")

            elif password != "1234":
                messagebox.showerror("encryption", "Invalid Password")

        def encrypt():
            password = code.get()

            if password == "1234":
                screen1 = Toplevel(screen)
                screen1.title("encryption")
                screen1.geometry("400x200")
                screen1.configure(bg='#A93226')
                message = text1.get(1.0, END)
                encode_message = message.encode("ascii")
                base64_bytes = base64.b64encode(encode_message)
                encrypt = base64_bytes.decode("ascii")

                Label(screen1, text="Encrypt", font="arial", fg="white", bg="#A93226").place(x=10, y=0)
                text2 = Text(screen1, font="Rpbota 10", bg="white", relief=GROOVE, wrap=WORD, bd=0)
                text2.place(x=10, y=40, width=380, height=150)

                text2.insert(END, encrypt)

            elif password == "":
                messagebox.showerror("encryption", "Input Password")

            elif password != "1234":
                messagebox.showerror("encryption", "Invalid Password")

        def main_screen():

            global screen
            global code
            global text1

            screen = Toplevel(self.window)
            screen.geometry("475x500")
            screen.configure(bg='#D7DBDD')

            #title
            screen.title("Create Secret Messages")

            def reset():
                code.set("")
                text1.delete(1.0, END)

            Label(screen,text="Enter text to encrypt and decrypt", fg="black", font=("calibri", 13)).place(x=10, y=10)
            text1 = Text(screen,font="Robota 20", bg="white", relief=GROOVE, wrap=WORD, bd=0)
            text1.place(x=10, y=70, width=455, height=100)

            Label(screen,text="Enter secret key for encryption and decryption", fg="black", font=("calibri", 13)).place(x=10,
                                                                                                                 y=190)

            code = StringVar()
            Entry(screen,textvariable=code, width=25, bd=0, font=("arial", 25), show="*").place(x=10, y=220)
            Button(screen,text="ENCRYPT", height="3", width=25, bg="#F5B041", fg="white", bd=0,cursor='hand2', command=encrypt).place(x=40, y=290)
            Button(screen,text="DECRYPT", height="3", width=25, bg="#E67E22", fg="white", bd=0,cursor='hand2', command=decrypt).place(x=250, y=290)
            Button(screen, text="RESET", height="3", width=55, bg="#34495E", fg="white", bd=0,cursor='hand2', command=reset).place(x=40, y=370) #h=2 w=23
            screen.mainloop()
        main_screen()


def page():
    window = Tk()
    LoginForm(window)
    window.mainloop()
if __name__ == '__main__':
    page()

