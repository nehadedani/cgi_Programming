#!C:\Users\nehad\AppData\Local\Programs\Python\Python310\python.exe
# Path to Python Executable

#Name:         Neha Dedani
#Class:        CS 4720
#Term:         Summer 2022
#Instructor :  Dr. North
#Assignment:   Assignment 5

import cgi

#FieldStorage is python keyword of metadata
form = cgi.FieldStorage()

shipName = str(form.getvalue('shippingName'))
shipZip = str(form.getvalue('shippingZip'))
billName = str(form.getvalue('billingName'))
billZip = str(form.getvalue('billingZip'))

formFile = open("address.txt", "w")
formFile.write("Shipping Name: "+shipName+" Shipping Zip: "+shipZip+" \nBilling Name: "+billName+" Billing Zip: "+billZip)
formFile.close()

print("Content-type:text/html\r\n\r\n")
print("<html>")
print("<head>")
print("<title> Address </title>")
print("</head>")
print("<body>")
print("Shipping name: <strong>%s</strong>  -- Shipping Zip:<strong> %s</strong> <br>" % (shipName, shipZip))
print("Billing name: <strong>%s</strong>   -- Billing Zip: <strong>%s</strong> <br>" % (billName, billZip))
print("<br>Info written to address.txt")
print("</body>")
print("</html>")