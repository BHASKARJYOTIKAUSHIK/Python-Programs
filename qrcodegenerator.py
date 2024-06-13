import qrcode as qr
s=input("Enter to convert into qrcode:")
img=qr.make(s)
img.save("bhaskar.jpg")