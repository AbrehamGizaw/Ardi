import os
import django
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail

# Adjust the path to your Django project settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ardimarble.settings')
django.setup()

# res = send_mail("testing","fuckyou", "fuckyou", ['abreshgize@gmail.com'], fail_silently=False)
# print(res)

import smtplib

def test_smtp_connection():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('your_email@gmail.com', 'your_password')
        print("SMTP connection successful!")
    except Exception as e:
        print(f"SMTP connection failed: {e}")
    finally:
        server.quit()

if __name__ == "__main__":
    test_smtp_connection()

