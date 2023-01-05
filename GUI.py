# Import Required Module
from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog
import os
import FTPUploader
import FTPDownloader
import receiver.decryption
import receiver.keyDecryption
import sender.encryption
import sender.keyEncryption



def UploadAction(event=None):
    chosenUploadFile = filedialog.askopenfilename()
    head, tail = os.path.split(chosenUploadFile)
    labelText3.set("")
    labelText4.set("")
    labelText5.set("")
    # encrypt chosenFile 
    sender.encryption.encryption(tail)
    # upload encrypted chosenFile
    FTPUploader.fileUpload('ciphertext.txt')
    # create a Label widget
    labelText.set("File Encrypted and Uploaded...")
    # encrypt keys
    sender.keyEncryption.keyEncryption()
    # upload keys 
    FTPUploader.fileUpload('encryptedKey.txt') 
    labelText1.set("Keys File Encrypted and Uploaded...")
    # upload masterkey
    FTPUploader.fileUpload('encryptedMasterKey.txt')
    labelText2.set("Master Key File Encrypted and Uploaded...")
    
def DownloadAction(event=None):
    chosenDownloadFile = 'ciphertext.txt'
    labelText.set("")
    labelText1.set("")
    labelText2.set("")
    # download masterkey
    FTPDownloader.fileDownload('encryptedMasterKey.txt')
    labelText3.set("Master Key File Decrypted and Downloaded...")
    # download keys 
    FTPDownloader.fileDownload('encryptedKey.txt') 
    labelText4.set("Key File Decrypted and Downloaded...")
    # decrypt keys
    receiver.keyDecryption.keyDecryption()
    # download encrypted chosenFile
    FTPDownloader.fileDownload(chosenDownloadFile)
    labelText5.set("Text File Decrypted and Downloaded...")
    # decrypt chosenFile 
    receiver.decryption.decryption(chosenDownloadFile)
    print('Selected:', chosenDownloadFile)





# Create Root Object
root = Tk()

# Set Geometry(widthxheight)
root.geometry('650x200')

# Create style Object
style = Style()


# Will add style to every available button
# even though we are not passing style
# to every button widget.
style.configure('TButton', font =
			('calibri', 10, 'bold'),
				foreground = 'black',
                background = 'black')
# button 1
btn1 = Button(root, text = 'UPLOAD',
				style = 'TButton',
			command = UploadAction)

btn1.grid(row = 0, column = 3, padx = 100)

# button 2
btn2 = Button(root, text = 'DOWNLOAD', command = DownloadAction)
btn2.grid(row = 4, column = 3, pady = 10, padx = 100)

labelText = StringVar()
label = Label(root,  textvariable=labelText).grid(row = 0, column = 4, padx = 100)
labelText1 = StringVar()
label1 = Label(root, textvariable=labelText1).grid(row = 1, column = 4, padx = 100)
labelText2 = StringVar()
label2 = Label(root, textvariable=labelText2).grid(row = 2, column = 4, padx = 100)

labelText3 = StringVar()
label3 = Label(root,  textvariable=labelText3).grid(row = 4, column = 4, padx = 100)
labelText4 = StringVar()
label4 = Label(root, textvariable=labelText4).grid(row = 5, column = 4, padx = 100)
labelText5 = StringVar()
label5 = Label(root, textvariable=labelText5).grid(row = 6, column = 4, padx = 100)


# Execute Tkinter
root.mainloop()
