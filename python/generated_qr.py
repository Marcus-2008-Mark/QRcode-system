import uuid  
import qrcode

Base_url = 'http://192.168.174.15:5000'
def gen_qrcode(label ):
    token = uuid.uuid4().hex # Generate a unique token used for the QR code
    
    url = f'{Base_url}/scan?token={token}' 
    
    img = qrcode.make(url)
    file_name = f"qr_{token}.png"
    img.save(file_name)
    
    
    print(f'[created] Label:  {label}')
    print(f"Token:  {token}")
    print(f"URL:    {url}")
    print(f"QR code saved as: {file_name}")
if __name__ == "__main__":
    gen_qrcode(label='test.1')
     
    
    