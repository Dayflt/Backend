from web.models import video_table

from operator import mod, pos

from flask_sqlalchemy import model
from web import db
from sqlalchemy import desc,sql

DISPLAY_VIDEO=4
def test_sql1(image_no):
    db.session.add(image_no)

def test_sql2(image_no):
    model_idR = db.session.query(video_table.model_id).filter(video_table.image_no == image_no).first()
    return(model_idR.model_id)

#model id리턴
def video_insert(model_result, image_no):
    "model_id return + insert video url to db"

    video_temp=video_table(model_result, image_no)
    db.session.add(video_temp)
    db.session.commit()
    model_idR=db.session.query(video_table.model_id).filter(video_table.model_result==model_result).first()
    return model_idR.model_id


def get_video_url(model_id):
    "gets model_result from model_id"
    a= db.session.query(video_table).filter(video_table.model_id==model_id).first()
    return a.model_result

def remove_vid(model_id):
    "removes video from model_id"
    remove=db.session.query(video_table).filter(video_table.model_id==model_id).first()
    db.session.delete(remove)
    db.session.commit()

def gallery_info(model_id,model_name,category_no):
    "uploads information for uploading video on gallery"
    post=db.session.query(video_table).filter(video_table.model_id==model_id).first()
    post.model_name=model_name
    post.category_no=category_no
    post.model_date=sql.func.now()#str(dt.datetime.now())
    db.session.commit()

def post_gallery_category(category_no):
    "returns info about 4(or less) videos based on category_no"
    video=db.session.query(video_table).filter(video_table.category_no==category_no).order_by(video_table.model_date.desc())
    print(video.all())
    return video.all()

def gallery_remove_oldvid(model_result):
    "removes the old video of such model_result"
    remove=db.session.query(video_table).filter(video_table.model_result==model_result).first()
    db.session.delete(remove)
    db.session.commit()

def post_gallery(category_no):
    "based on the category_no remove video except for the recent 4 videos"
    result=[]
    for instance in db.session.query(video_table).filter(video_table.category_no==category_no).order_by(video_table.model_date.desc()):
        result.append(instance.model_result)
    if len(result)>DISPLAY_VIDEO:
        for i in result[DISPLAY_VIDEO:]:
            gallery_remove_oldvid(i)
