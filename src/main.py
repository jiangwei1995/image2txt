# -*- coding: utf-8 -*-
from flask import Flask,request,render_template, make_response
import pytesseract
import random
from PIL import Image
import datetime
app = Flask(__name__)
count = 1

@app.route('/', methods=['GET'])
def index():
  return render_template('/views/index.html')

@app.route('/image2txt', methods=['POST'])
def image2txt():
  file_obj = request.files.get('pic')
  print(file_obj)
  if file_obj:
    # f = open('img/'+str(count)+'.jpg','wb')
    img_path = 'src/static/img/'+ranstr(6)+'.jpg'
    f = open(img_path,'wb')
    data = file_obj.read()
    f.write(data)
    f.close()
    result = img2txt(img_path)
    return result
  else: 
    return "文件上传失败"


def img2txt(img_path):
  # for i in range(1,2):
  #   starttime = datetime.datetime.now()
  #   image = Image.open('img/'+img_path)
  #   text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文解析图片
  #   endtime = datetime.datetime.now()

  #   print (r"计算机网络_"+str(i)+r"转换完成，耗时：" + str((endtime - starttime).seconds))

  #   text=text.replace(" ","")
  #   # with open(r"./txt/"+img_path+".txt", "a") as f: # 将识别出来的文字存到本地
  #   #   f.write(str(text))
        
  #   return text
  for i in range(1,2):
    starttime = datetime.datetime.now()
    image = Image.open(img_path)
    text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文解析图片
    endtime = datetime.datetime.now()

    print (r"计算机网络_"+str(i)+r"转换完成，耗时：" + str((endtime - starttime).seconds))

    text=text.replace(" ","")
    resp = make_response(render_template("/views/result.html", text=text, img_path= img_path[4:]))
    resp.cache_control.no_cache = False
    return resp
    

def ranstr(num):
  # 猜猜变量名为啥叫 H
  H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'

  salt = ''
  for i in range(num):
      salt += random.choice(H)
  return salt
  salt = ranstr(6)
  return salt
