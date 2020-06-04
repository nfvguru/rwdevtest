import time
import os
from django.conf import settings
from rwfw_utils.models import rwfw_utils_imgdownload
from rwfw_images.models import rwfw_image_downloaded
# from rwfw_utils.models import jsons_path
from .rwfw_json_utils import rwfw_create_config
from .rwfw_json_utils import rwfw_get_img_from_config
from .rwfw_remote_ops import rwfw_remote_build
from .rwfw_remote_ops import rwfw_download_build



def path_to_json_filename(path):
    fname  = os.path.join(settings.BASE_DIR,'jsons')
    fname = os.path.join(fname,path.split('/')[-5])
    fname += '_' + path.split('/')[-4] + '.json'
    print (fname)
    return fname

def convert_to_config(rip,ru,rp,rl):
    config_dict = {
        'rwfw_img': {
            'ip':rip,
            'user': ru,
            'pass': rp,
            'path': rl,
            'img' : 'tofill',
        }
    }
    return config_dict

def create_cfg_file(rip,ru,rp,rl):
    cfname = path_to_json_filename(rl)
    cdict  = convert_to_config(rip,ru,rp,rl)
    rwfw_create_config(cfname, cdict)
    idn = rl.split('/')[-5] + 'new1'
    new_db1 = rwfw_utils_imgdownload(imgdwn_path=rl, imgdwn_name=idn, json_config=cfname)
    new_db1.save()
    new_db1.id
    return new_db1

def build_path_from_db(dbobject, task_id):
        dpath = dbobject.repo_base
        dpath += dbobject.repo_verson + "/"
        my_build = dbobject.repo_build
        if my_build == '0':
            my_build="lastSuccessfulBuild"
        dpath += my_build +"/HW_CH_ODS-VA/DEBUG/"
        if task_id == 1:
            my_type = 'VMW'
        elif task_id == 2:
            my_type = 'ISO'
        elif task_id == 3:
            my_type = 'img'
        elif task_id == 4:
            my_type = 'KVM'
        dpath += my_type
        return dpath



def rwfw_ckver(rip, ru, rp, rl):
    db1_obj = rwfw_utils_imgdownload.objects.filter(imgdwn_path=rl)
    if db1_obj.exists():
        # print(db1_obj[0].imgdwn_name)
        db1_obj = db1_obj.first()
        print(db1_obj.imgdwn_name)
    else:
        print('NOT exists')
        db1_obj = create_cfg_file(rip,ru,rp,rl)
    my_config = ""
    try:
        my_config = db1_obj.json_config
    except:
        print('error')
    mybuild = rwfw_remote_build(my_config)
    # print(mybuild)
    # return 135
    return mybuild


def rwfw_dwnver(rip, ru, rp, rl):
    db1_obj = rwfw_utils_imgdownload.objects.filter(imgdwn_path=rl)
    if db1_obj.exists():
        db1_obj = db1_obj.first()
    else:
        print('Config NOT exists')
        db1_obj = create_cfg_file(rip,ru,rp,rl)
    my_config = ""
    try:
        my_config = db1_obj.json_config
    except:
        print('error')
    img_name  = rwfw_get_img_from_config(my_config)
    if (img_name == 'tofill' ):
        mybuild = rwfw_remote_build(my_config)
    img_name  = rwfw_get_img_from_config(my_config)
    if (img_name == 'tofill' ):
        return "error"
    ret_str = rwfw_download_build(my_config)
    db_obj = rwfw_image_downloaded.objects.filter(dwm_build=-100).first()
    if db_obj:
        vers = img_name.split('_')[0].split('-')[1]
        bld  = img_name.split('_')[2].split('.')[0]
        db_obj.dwn_version = vers
        db_obj.dwm_build = bld
        db_obj.dwn_index = db_obj.dwn_index + 1
        db_obj.dwn_path  = img_name
        db_obj.dwm_avail = 1
        db_obj.save()    
    return ret_str
