import qrcode
name=input("please insert name : ")
mobile=input("please insert PhoneNumber : ")
img=qrcode.make(name+" | "+mobile)
img.save("name & mobile.jpg")