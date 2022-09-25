import os
import math
import random
import smtplib

digits="0123456789"
OTP=""
for i in range(6):
    OTP+=digits[math.floor(random.random()*10)]
otp = OTP+"is your OTP"
msg = otp
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login("amd.azad2000@gmail.com","mohamedazadsince21042000")
emailid = input("Enter email :")
s.sendmail('&&&&&&&&&&&',emailid,msg)
a=input("Enter your OTP :")
if a==OTP:
    print("Verified")
else:
    print("Please verify OTP again")
