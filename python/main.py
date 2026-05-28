import qrcode
import time

Base_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeVFgYvND5ziVfIFhugnBGFPWmaTycUkVjeHm97s3mC_Qg3jg/viewform?usp=publish-editor'

def Qrcode_generator(Base_url):
    
    img = qrcode.make(Base_url)
    img.save('qrcode.png')
    print('QRcode has be successfully created ✅')
    print('This will redirect you to the google form when scanned 🌐')
    expiration_time = time.sleep(10)
    print('QRcode has expired ❌')
    if expiration_time:
        img = qrcode.make(Base_url)
        img.save('qrcode.png')
if __name__ == "__main__":
    Qrcode_generator(Base_url)
dd=time.time()
print(dd)