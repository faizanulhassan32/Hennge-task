import pyotp
import base64
import hashlib

userid = "faizanulhassan043@gmail.com"  # Replace with your email address
shared_secret = userid + "HENNGECHALLENGE003"
shared_secret = base64.b32encode(shared_secret.encode()).decode()

def generate_totp_password():
    totp = pyotp.TOTP(shared_secret, interval=30, digits=10, digest=hashlib.sha512)
    return totp.now()

totp_password = generate_totp_password()
print(totp_password)

email = "faizanulhassan043@gmail.com"  # Replace with your email address

credentials = f"{email}:{totp_password}"
encoded_credentials = base64.b64encode(credentials.encode()).decode()

authorization_header = f"Basic {encoded_credentials}"

print(authorization_header)
