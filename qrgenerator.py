import qrcode
url=input('enter the url')
image=qrcode.make(url)
image.save('qrcode.png')
print('Image created successfully')
