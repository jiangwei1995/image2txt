# -*- coding: utf-8 -*-
from flask import Flask,request,render_template
import pytesseract
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
    f = open('src/static/img/'+str(count)+'.jpg','wb')
    data = file_obj.read()
    f.write(data)
    f.close()
    result = img2txt(str(count)+'.jpg')
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
    image = Image.open('img/'+img_path)
    text = pytesseract.image_to_string(image, lang='chi_sim')  # 使用简体中文解析图片
    endtime = datetime.datetime.now()

    print (r"计算机网络_"+str(i)+r"转换完成，耗时：" + str((endtime - starttime).seconds))

    text=text.replace(" ","")
    text=text.replace("\n","<br />")
    return render_template("/views/result.html", text=text)
    
