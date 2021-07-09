from app.models import video_table

from operator import mod, pos

from flask_sqlalchemy import model
from app import db
from sqlalchemy import desc

DISPLAY_VIDEO=4


#model id리턴
def video_insert(model_result, image_no):
    video_temp=video_table(model_result, image_no)
    db.session.add(video_temp)
    db.session.commit()
    model_idR=db.session.query(video_table.model_id).filter(video_table.model_result==model_result).first()
    return model_idR.model_id


def get_video_url(model_id):
    a= db.session.query(video_table).filter(video_table.model_id==model_id).first()
    return a.model_result

def remove_vid(model_id):
    remove=db.session.query(video_table).filter(video_table.model_id==model_id).first()
    db.session.delete(remove)
    db.session.commit()

def check_existance(model_id, user_name = False, category_id = False):
    first_vid = db.session.query(video_table).filter(video_table.model_id==model_id).first()
    if first_vid != None and not user_name:
        return False
    elif user_name:
        if first_vid['user_name'] and first_vid['category_id']:
            return True
    else:
        return False
    

from sqlalchemy import sql
def gallery_info(model_id,model_name,category_no):
    post=db.session.query(video_table).filter(video_table.model_id==model_id).first()
    post.model_name=model_name
    post.category_no=category_no
    post.model_date=sql.func.now()#str(dt.datetime.now())
    db.session.commit()

def post_gallery_category(category_no):
    video=db.session.query(video_table).filter(video_table.category_no==category_no).order_by(video_table.model_date.desc())
    return video.all()

def gallery_remove_oldvid(model_result):
    remove=db.session.query(video_table).filter(video_table.model_result==model_result).first()
    db.session.delete(remove)
    db.session.commit()

def post_gallery(category_no):
    result=[]
    for instance in db.session.query(video_table).filter(video_table.category_no==category_no).order_by(video_table.model_date.desc()):
        result.append(instance.model_result)
    if len(result)>DISPLAY_VIDEO:
        for i in result[DISPLAY_VIDEO:]:
            gallery_remove_oldvid(i)
    return print(result[:DISPLAY_VIDEO])
