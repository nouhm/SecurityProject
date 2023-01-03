import ftplib

def fileDownload(filename):
    FTP_HOST = "127.0.0.1" 
    FTP_PORT = 6060
    FTP_USER = "username"
    FTP_PASS = "P@ssw0rd"

    # connect to the FTP server 
    ftp = ftplib.FTP() 
    ftp.connect(FTP_HOST,FTP_PORT) 
    ftp.login(FTP_USER,FTP_PASS) 

    # force UTF-8 encoding 
    ftp.encoding = "utf-8"

    # the name of file you want to download from the FTP server
    # filename = "Biography.docx" 

    with open(filename, "wb") as file:
        # use FTP's RETR command to download the file
        retCode = ftp.retrbinary(f"RETR {filename}", file.write) 
    ftp.dir()


    # quit and close the connection
    ftp.quit()

    if retCode.startswith('226'):
        print('download successfull')
    else:
        print('download unsuccessful')