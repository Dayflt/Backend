# Backend

## βοΈ How to use 
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


## π SWAGGER

+ https://app.swaggerhub.com/apis/harloxx/WeirdMuseum/1-oas3  

+ Enter *localhost:5000/swagger* after Flask run   
![20210717_195035](https://user-images.githubusercontent.com/79822913/126034610-20bff471-7e80-48c8-88f8-c30e28dfd37d.png)
## π§Ύ PYTEST
```
(myenv) $ python run.py create_db
(myenv) $ flask run
# open another terminal
(myenv) $ pytest
```

## π§ Directory Structure
```bash
βββ Backend/                                - λ°±μλ νλΌμ€ν¬ λλ ν λ¦¬
    βββ test_endpoints.py                   - unit test μ€ν νμΌ
    βββ run.py                              - Flask μ€ν μν νμΌ
    βββ views.py                            - SQLAlchamyμ κΈ°λ₯μ μ μν νμΌ
    βββ .flaskenv                           - Flask μ€νμ μν νκ²½λ³μ μ€μ  νμΌ
    βββ dayfly-318913-a4b443321e00.json     - Google Cloud Bucketμ μ κ·ΌνκΈ° μν κΆν μ λ³΄κ° λ΄κΈ΄ νμΌ        
    βββ requirements.txt                    - λͺ¨λλ€μ μ λ¦¬ν νμΌ
    βββ web/
         βββ AI/                            - AIλͺ¨λΈ μκ³ λ¦¬μ¦
         βββ data/result/                   - λ°±μλ λμμ μμ μ μ₯ λλ ν λ¦¬
         βββ __init__.py                    - μ€νμν€λ €λ flask appμ΄ μ μλμ΄μλ νμΌ νλ‘μ νΈλ₯Ό μ€νμν€λ©΄ appμ κ΅¬λμν΄
         βββ config.py                      - νμ configuration μ¬ν­λ€μ΄ μ μλ νμΌ
         βββ gcp.py                         - google cloud bucketμ μ΄μ©ν΄ νμΌ μμΆλ ₯ μ€νΈλ¦Όμ λ€λ£¨κΈ° μν ν¨μκ° μ μλ νμΌ
         βββ models.py                      - video_tableμ΄λΌλ database classκ° μ μλ νμΌ
         βββ prdedictmix.py                 - AI λͺ¨λΈμ μ μ©ν΄μ μλΉμ€μ ν΅μ¬μΈ μμΈ μμ μμ±μ νκΈ° μν νμΌ
         βββ routes.py                      - API λͺμΈμκ° λͺ¨λ μ μλ νμΌ
         βββ views.py                       - database ORM μ μ νμΌ
         βββ static/
               βββ swagger.json             -swagger μ μ νμΌ
 ```
