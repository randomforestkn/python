from ftplib import FTP

host = "name_of_ftp"
user = "username"
password = "password"

with FTP(host) as ftp:

    ftp.login(user=user, passwd=password)
    print(ftp.getwelcome())

    #  download a file from ftp
    with open('test.txt', 'wb') as f:
        ftp.retrbinary("RETR " + "mytest.txt", f.write, 1024)


    # upload a file to ftp
    with open('myupload.txt', 'rb') as f:
        ftp.storbinary('STOR ' + 'upload.txt', f)


    # navigate to directory over the ftp server
    ftp.cwd("dirname")

    with open('myspecialfile.txt', 'wb') as f:
        ftp.retrbinary('RETR ' + 'otherfile.txt', f.write, 1024)

    ftp.quit()
