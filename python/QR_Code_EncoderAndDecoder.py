import qrcode

qr_input = input('enter the content of your desired qrcode!')
myqr = qrcode.make(qr_input)
myqr.save('myqr.png')
