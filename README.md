# Backend_repo

## ✏️ How to use 
### 1. Cloning
```
$ git clone https://github.com/Dayflt/Backend_repo.git
```
### 2. Download file
- Download *vox-cpk.pth.tar* [here](https://drive.google.com/drive/folders/1PyQJmkdCsAkOYwUyaj_l-l0as-iLDgeH) and add it inside Docker\Backend\web\AI\ after changing its name with *mraa.tar*

### 3. Make Virtualenv & Download Requirements
```
$ pip install virtualenv
$ virtualenv myenv # make virtual environment
$ .\myenv\Scripts\activate
```
(myenv) 가상환경 진입 확인
```
$ pip install -r requirements.txt #install requirements
```

## 📗 SWAGGER
![20210717_195035](https://user-images.githubusercontent.com/79822913/126034610-20bff471-7e80-48c8-88f8-c30e28dfd37d.png)

## 🔧 Directory Structure
```bash
├── Backend/             - 백엔드 플라스크 디렉토리
    ├── errors.py
    ├── run.py                
    ├── views.py               - SQLAlchamy의 기능을 정의한 파일
    ├── .flaskenv
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
         ├── views.py
         └── static/
               └── swagger.json 
 ```
