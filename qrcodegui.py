import qrcode
from tkinter import *
from PIL import Image, ImageTk

def c_qrcode(text):
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black',back_color='white')
    return img

def demo():
    
    def on_click(e):
        iput_text = txt.get('0.0','end-1c')
        p_img = c_qrcode(iput_text).resize((250,250))
        img_tk = ImageTk.PhotoImage(p_img)
        qr.configure(image=img_tk)
        qr.image = img_tk
   
    screen = Tk()
    screen.title('Qrcode Generate')
    screen.minsize(width=600,height=250)
    screen.option_add('*Font','consolas 18')
    
    Label(screen,text='Enter Text',fg='blue').grid(row=0,column=0)
    txt = Text(screen,height=4,width=30,fg='green')
    txt.grid(row=1,column=0)
    btn = Button(screen,text='Create Qrcode',bg='green',fg='white')
    btn.grid(row=2,column=0)
    btn.bind('<Button-1>',on_click)
    
    qr = Label(screen)
    qr.grid(row=0,column=1,rowspan=3)
    screen.mainloop()

demo()   
    

  
  
  


