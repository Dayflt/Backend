# Flask를 이용하여 AI를 호스트 하는데 사용
# Flask를 사용해서 모델을 API로 rapping을 함
# 이제 Flask를 사용하면 프로그램이 IP 주소를 얻고 인터넷 어디에서나 API 호출을 사용하여 사용이 가능

from flask import Flask, redirect
from predict import generate
from predict import join_path
import imageio
from skimage import img_as_ubyte

app = Flask(__name__)
prediction = None

@app.route('/')
def loading():
    return redirect('/showvid')

@app.route('/showvid', methods = ['GET', 'POST'])
def mixvid():
    global prediction
    # 실제로는 이미지로는 서버에 저장된 이미지의 경로
    # reader의 경우에는 웹캠과 서버를 연결해 저장된 동영상의 경로
    prediction = generate()
    imageio.mimsave(join_path('result.mp4'), [img_as_ubyte(frame) for frame in prediction])
    if prediction:
        html = '''
            <!doctype html>
            <html>
                <head>
                    <title>(-: VIDEOFIED YOU :-)</title>
                </head>
                <body>
                    <video width="720" controls>
                    <source src="/Users/leekunsang/Dayfly/Ai/result.mp4" type="video/mp4">
                    </video>
                </body>
            </html>
            '''
        return html
    else:
        redirect('/Failed')
        
@app.route('/Failed')
def fail():
    return "VIDEO NOT MADE"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug = True)



