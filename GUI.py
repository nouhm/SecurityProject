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
    # encrypt chosenFile 
    sender.encryption.encryption(tail)
    # upload encrypted chosenFile
    FTPUploader.fileUpload('ciphertext.txt')
    # encrypt keys
    sender.keyEncryption.keyEncryption()
    # upload keys 
    FTPUploader.fileUpload('encryptedKey.txt') 
    # upload masterkey
    FTPUploader.fileUpload('encryptedMasterKey.txt')
    print('Selected:', chosenUploadFile)
    print(tail)
    
def DownloadAction(event=None):
    chosenDownloadFile = 'ciphertext.txt'
    # head2, tail2 = os.path.split(chosenDownloadFile)
    # download masterkey
    FTPDownloader.fileDownload('encryptedMasterKey.txt')
    # download keys 
    FTPDownloader.fileDownload('encryptedKey.txt') 
    # decrypt keys
    receiver.keyDecryption.keyDecryption()
    # download encrypted chosenFile
    FTPDownloader.fileDownload(chosenDownloadFile)
    # decrypt chosenFile 
    receiver.decryption.decryption(chosenDownloadFile)





# Create Root Object
root = Tk()

# Set Geometry(widthxheight)
root.geometry('500x500')

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
btn2.grid(row = 1, column = 3, pady = 10, padx = 100)

# Execute Tkinter
root.mainloop()
