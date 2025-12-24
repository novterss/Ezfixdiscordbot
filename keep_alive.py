from flask import Flask
from threading import Thread
import os

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

def run():
  # แก้ตรงนี้: ให้ดึง PORT จาก Environment ของเครื่องเซิฟเวอร์ ถ้าไม่มีค่อยใช้ 8080
  app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))

def keep_alive():
    t = Thread(target=run)
    t.start()
