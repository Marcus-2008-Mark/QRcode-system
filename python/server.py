
import time
from  pyngrok import ngrok 
import qrcode
from flask import Flask, redirect, abort, render_template_string, request

app = Flask(__name__)

url = 'https://docs.google.com/forms/d/e/1FAIpQLSeVFgYvND5ziVfIFhugnBGFPWmaTycUkVjeHm97s3mC_Qg3jg/viewform?usp=publish-editor'
 
expiration_timestamp = time.time() + 300
scanned_ips = set()
def qrcode_generator():
    ngrok.set_auth_token(f"3E4xfn60TrYLsjVvwrDVd1zNWnP_3phY6c41k2hroPASyPSPC")  # Replace with your actual ngrok auth token
    
    tunnel = ngrok.connect(8080,proto="http",domain="grafting-embody-rounding.ngrok-free.dev")
    
    redirect_url = f"{tunnel.public_url}/scan"
    img = qrcode.make(redirect_url)
    img.save("QRcode.png")
    
    
    print('✅ QR code successfully created as QRcode.png!')
    print(f"🌐 public URL: {tunnel.public_url}")
    print('⏳ It will expire exactly 5 minutes after the server starts up...\n')

@app.route('/scan')
def handle_scan():
    current_time = time.time()
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    
    if current_time > expiration_timestamp:
        error_html = '<h2>❌ Error: this QR has expired'
        return render_template_string(error_html), 410
    if client_ip in scanned_ips:
        already_scanned_html = '<h2>❌ Error: this QR code has already been scanned'
        return render_template_string(already_scanned_html), 403
    
    scanned_ips.add(client_ip)
    response = redirect(url)
    response.headers['ngrok-skip-browser-warning'] = 'true'
    return response

if __name__ == "__main__":
    qrcode_generator()
    app.run(host='0.0.0.0', port=8080, debug=False)