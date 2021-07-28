# Backend

## ✏️ How to use 
### 1. Cloning
```
$ git clone https://github.com/Dayflt/Backend.git
```
### 2. Download file
- Download *vox-cpk.pth.tar* [here](https://drive.google.com/drive/folders/1PyQJmkdCsAkOYwUyaj_l-l0as-iLDgeH) and add it inside Backend\web\AI\ after changing its name with *mraa.tar*

### 3. Make Virtual Environment & Download Requirements
+ Go to *Backend/* directory
```
cd Backend
```
+ Make virtual environment
```
$ pip install virtualenv
$ virtualenv myenv # make virtual environment
```
+ Activate virtual environment
```
$ .\myenv\Scripts\activate
```
+ Go back to Backend directory and install requirements.txt
```
(myenv) $ cd ../../
(myenv) $ pip install -r requirements.txt 
```
+ If you want to deactivate
```
(myenv) $ deactivate
```
### 5. Make Database

+ Database setting
+ Change Backend/web/config.py
```
2 PORT= '(Enter your PORT)'
3 USERNAME='(Enter your USERNAME)'
4 PASSWORD='(Enter your PASSWORD)'
```
+ Create new database
```
(myenv) $ python run.py create_db
```

### 6. RUN
+ Run Flask
```
(myenv) $ python run.py run
```


## 📗 SWAGGER

+ https://app.swaggerhub.com/apis/harloxx/WeirdMuseum/1-oas3  

+ Enter *localhost:5000/swagger* after Flask run   
![20210717_195035](https://user-images.githubusercontent.com/79822913/126034610-20bff471-7e80-48c8-88f8-c30e28dfd37d.png)
## 🧾 PYTEST
```
(myenv) $ python run.py create_db
(myenv) $ flask run
# open another terminal
(myenv) $ pytest
```

## 🔧 Directory Structure
```bash
├── Backend/                                - 백엔드 플라스크 디렉토리
    ├── test_endpoints.py                   - unit test 실행 파일
    ├── run.py                              - Flask 실행 위한 파일
    ├── views.py                            - SQLAlchamy의 기능을 정의한 파일
    ├── .flaskenv                           - Flask 실행을 위한 환경변수 설정 파일
    ├── dayfly-318913-a4b443321e00.json     - Google Cloud Bucket에 접근하기 위한 권한 정보가 담긴 파일        
    ├── requirements.txt                    - 모듈들을 정리한 파일
    └── web/
         ├── AI/                            - AI모델 알고리즘
         ├── data/result/                   - 백엔드 동영상 임시 저장 디렉토리
         ├── __init__.py                    - 실행시키려는 flask app이 정의되어있는 파일 프로젝트를 실행시키면 app을 구동시킴
         ├── config.py                      - 필수 configuration 사항들이 정의된 파일
         ├── gcp.py                         - google cloud bucket을 이용해 파일 입출력 스트림을 다루기 위한 함수가 정의된 파일
         ├── models.py                      - video_table이라는 database class가 정의된 파일
         ├── prdedictmix.py                 - AI 모델을 적용해서 서비스의 핵심인 섞인 영상 생성을 하기 위한 파일
         ├── routes.py                      - API 명세서가 모두 정의된 파일
         ├── views.py                       - database ORM 정의 파일
         └── static/
               └── swagger.json             -swagger 정의 파일
 ```
