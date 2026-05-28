import qrcode 




def Qrcode_generator():
    email = 'mailto:mybusiness222002@gmail.com?subject=QR Scan&body=I have scanned the QR code.'
    
    
    img = qrcode.make(email)
    img.save('qrcode.png')
    print('QRcode has be successfully created ✅')
if __name__ == "__main__":
    Qrcode_generator()