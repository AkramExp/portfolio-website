import smtplib
import ssl


def sendMail(message):
    host = "smtp.gmail.com"
    port = 465

    username = "its.akram246@gmail.com"
    password = "uwtngsmbmoldgoon"

    receiver = "its.akram246@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
