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
![20210717_195035](https://user-images.githubusercontent.com/79822913/126034610-20bff471-7e80-48c8-88f8-c30e28dfd37d.png)
## 🧾 PYTEST
```
(myenv) $ pytest -p no:warnings -vv
```

## 🔧 Directory Structure
```bash
├── Backend/             - 백엔드 플라스크 디렉토리
    ├── test_endpoints.py   - unit test 실행 파일
    ├── run.py             -Flask 실행 위한 파일
    ├── views.py               - SQLAlchamy의 기능을 정의한 파일
    ├── .flaskenv           -Flask 실행을 위한 환경변수 설정 파일
    ├── dayfly-318913-a4b443321e00.json         
    ├── requirements.txt     - 모듈들을 정리한 파일
    └── web/
         ├── AI/                  - AI모델 알고리즘
         ├── data/result/         - 백엔드 동영상 임시 저장 디렉토리
         ├── __init__.py        
         ├── config.py
         ├── gcp.py
         ├── models.py
         ├── prdedictmix.py
         ├── routes.py
         ├── views.py           -database ORM 정의 파일
         └── static/
               └── swagger.json     -swagger 정의 파일
 ```
