import smtplib

my_email = 'garagyae4568@gmail.com'
password = "gara4568!!"

connection = smtplib.SMTP("smtp.gmail.com",port=587)
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="jinhong4107@gmail.com",msg='Hello')
connection.close()