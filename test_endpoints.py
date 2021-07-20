import pytest, json
from web import config # config 파일을 불러와서 테스트 설정들을 읽어들이도록 함
from web import app

from web.models import video_table
import random, sqlalchemy

from sqlalchemy import create_engine, text

# 새로운 데이터베이스를 생성
db = create_engine(config.test_config['DB_URL'], encoding = 'utf-8', max_overflow = 0)
db.connect()

#database=SQLAlchemy(app)
#app.config.from_pyfile('config.py')

@pytest.fixture
def api():
    app.config['test'] = True
    api = app.test_client() # Flask에서 제공하는 test_client함수를 사용해서 테스트할 flask app을 만들어야 함

    return api # 테스트용 클라이언트 반환
# 데이터베이스에 비디오 영상 객체를 생성하는 함수를 setup_function으로 설정
# 데이터베이스에서 비디오 영상 객체와 테스트 데이터를 모두 지우는 함수를 teardown_function으로 설정
over_four = False
def setup_function(): # test 전에 바로 적용
    if over_four:
        for i in range(5):
            mixed_video = {
                'model_result': f"https://storage.googleapis.com/dayfly-bucket/testvid{i}mixed.mp4",
                'image_no': 1,
                'model_name': f'usernickname{i+1}',
                'category_no': 1,
                'model_date': f"2021-07-0{i+1} 16:12:07.822257+09"
                }
            
            db.execute(text
            ("""INSERT INTO video_info(model_result, image_no, model_name, category_no, model_date)
            VALUES (:model_result, :image_no, :model_name, :category_no, :model_date)
            """), mixed_video)
    else:
        mixed_video = {
            'model_result' :  "https://storage.googleapis.com/dayfly-bucket/testvid123456mixed.mp4",
            'image_no': 2,
            'model_name': 'usernickname',
            'category_no': 1,
            'model_date':  "2021-07-01 16:12:07.822257+09"
        }
        db.execute(text
            ("""INSERT INTO video_info(model_result, image_no, model_name, category_no, model_date)
            VALUES (:model_result, :image_no, :model_name, :category_no, :model_date)
            """), mixed_video)
    
def tear_down_function(): # test 후에 바로 적용
    db.execute(text("SET FOREIGN_KEY_CHECKS=0"))
    db.execute(text("TRUNCATE video_table"))
    db.execute(text("SET FOREIGN_KEY_CHECKS=1"))
        


    
def test_return_result_post(api):
    # captured vid, img no -> made mixed video (assume upload success)

    response = api.post('/api/model',
        data = json.dumps({
        'success' :  'True',
        'file' : 'Received',
        'model_result' : "https://storage.googleapis.com/dayfly-bucket/testvid123456mixed.mp4"}),
        content_type = 'application/json')
    assert response.status_code == 200

    response = api.post('/api/model/217',
                        data = json.dumps({"success" : True}),
                        content_type = 'application/json')

    assert response.status_code == 405
    


    assert response == api.post('/api/model/108',
        data = {'model_name': 'usernickname1', 'category_no':1}, 
        content_type = 'application/json')


    # model_id가 10인 영상에 대해서 영상 주인의 이름과 이모티콘 카테고리 번호를 반환받음

def test_return_result_get(api):
    # response로 GET형태의 HTTP에 대해서 반환해줄 return할 json 데이터   
    response = api.get(f'api/model/103')
    video_url = json.loads(response.form.decode('utf-8'))['model_result']

    assert response.status_code == 200
    assert video_url == "https://storage.googleapis.com/dayfly-bucket/testvid1234mixed.mp4"



def test_return_result_delete(api):
    # 일단 사용자가 본인의 사진을 받았음을 가정한다.
    # 먼저 특정 모델 아이디가 존재하는지 확인
    response = api.post('/api/models/103',
        data=json.dumps({'success':True}),
        content_type = 'application/json')

    # 이미지 번호와 캡쳐영상을 받고 반환하는게 정확했을 때에 200을 호출
    assert response.status_code == 404