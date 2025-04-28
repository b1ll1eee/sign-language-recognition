# Sign language แปลภาษามือเป็นข้อความด้วย AI

เว็บไซค์ที่ช่วยสำหรับแปล ภาษามือของคนไทยเป็นข้อความต่างๆ โดยซัพพอร์ตทั้งหมด 17 ท่า ได้แก่
รัก ฉัน เธอ สวัสดี สบายดี ชอบ ดีใจ เสียใจ โกรธ ร้องให้ กลัว อิ่ม ยาก ง่าย ลืม คิดถึง ยืน

  - Model สร้างด้วย Python ใน Jupyter notebook   โดยใช้ LSTM Model และ MediaPipe ในการ Trian model
  -   WebSite เขียนแบบ MVT โดยใช้ Django ในการเชื่อมต่อ Model  และ Database และใช้ HTML CSS JS 

## สารบัญการใช้งาน
 
 - ติดตั้งโปรแกรมเบื้องต้น
 - ดาวน์โหลด Dataset
 - ดาวน์โหลด Database
 - วิธีใช้งานโปรแกรม
 

## ขั้นตอนการติดตั้งโปรแกรมเบื้องต้น
![enter image description here](https://arcade-pk.readthedocs.io/en/latest/_images/setup_windows_1.png)



![enter image description here ](https://www.comscidev.com/wp-content/uploads/2019/01/Install-VSCode-3.jpg)

      git clone https://github.com/sophonwit379/MIT_Sign_Language_Recognition.git
      pip install requirements.txt
      pip install notebook

## ดาวน์โหลด Dataset
[    คลิกเพื่อดาวน์โหลด Dataset](https://drive.google.com/file/d/17-hhCr_5tQIkMToAlevN3njRZiemX1wO/view?usp=share_link)

## ดาวน์โหลด Database
ในส่วนของ databse เราได้ใช้เป็น [MongoDB Atlas](https://www.mongodb.com/cloud/atlas/register) ในการเก็บข้อมูลโดยเราจะเก็บเป็นลิ้งวีดีโอที่ได้ upload ลง google drive
ซึ่งผู้ใช้จะต้องทำการ download [MongoDB Compass](https://www.mongodb.com/try/download/compass) ก่อนจากนั้นจึง import collection Action.json แล้วค่อย
connect กับ MongoDB Atlas ก็สามารถใช้งานได้แล้ว

## วิธีใช้งานโปรแกรม

    cd slrsite 
    py manage.py

## เครดิต
Youtube [  Nicholas Renotte](https://www.youtube.com/@NicholasRenotte)
