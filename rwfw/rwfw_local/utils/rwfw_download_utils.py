import time
import os
from django.conf import settings
from rwfw_utils.models import rwfw_utils_imgdownload
# from rwfw_utils.models import jsons_path
from .rwfw_json_utils import rwfw_create_config
from .rwfw_remote_ops import rwfw_remote_build



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


def rwfw_ckver(rip, ru, rp, rl):
    print("Njan Okay")
    i = 5
    while i > 1 :
        i -= 1
        time.sleep(2)
        print("Njan Pinnem Okay")
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
    print(mybuild)
    # return 135
    return mybuild
