from demo import load_checkpoints, make_animation
import imageio
from skimage.transform import resize


def join_path(file, root = '/Users/leekunsang/Dayfly/Ai'):
    import os
    return os.path.join(root, file)

def generate(config_path = 'mraa.yaml', cp_path = 'mraa.tar', source_img = 'ia.png', driving_video = 'testvid.mp4'):
    """
    source_img : 현재 디렉토리에 저장된 이미지중 선택된 이미지의 상대 경로
    driving_video : 캡쳐영상의 상대 경로 (db에 저장)
    """
    config_path, cp_path, source_img, driving_video = join_path(config_path), join_path(cp_path), join_path(source_img), join_path(driving_video)

    source_img = resize(imageio.imread(source_img), (256, 256))
    reader = imageio.get_reader(driving_video)
    fps = reader.get_meta_data()['fps']

    driving_video = []
    for im in reader:
        driving_video.append(im)
    reader.close()

    driving_video = [resize(frame, (256, 256)) for frame in driving_video]

    # load model
    model_gen, model_kp = load_checkpoints(config_path, cp_path, cpu = True)
    
    # numpy array 형태로 영상 반환
    vid = make_animation(source_img, driving_video, 
        generator = model_gen, kp_detector = model_kp, relative = True, adapt_movement_scale = True, cpu = True)
    
    # 동영상을 numpy의 의 형태로 변환
    return vid