import os
import json
import base64
import sqlite3
import win32crypt
from Crypto.Cipher import AES
import shutil
from datetime import timezone, datetime, timedelta

def get_chorme_datetime(chromedate):
    """Retorna un objeto `datetime.datetimev desde una fecha y hora en formato Chrome 
    dado que `chromedate` esta formateado como el numero de microsegundos desde enero de 1601"""
    return datetime(1601, 1, 1) + timedelta(microseconds=chromedate)

def get_encryption_key():
    local_state_path = os.path.join(
        os.environ["USERPROFILE"],
        "AppData",
        "Local",
        "Google",
        "Chrome",
        "User Data",
        "Local State",
    )

def decrypt_password(password, key):
    pass

def main():
    pass

if __name__ == "__main__":
    main()
    
    
    