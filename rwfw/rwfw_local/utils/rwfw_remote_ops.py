import json
from .rwfw_ssh_utils import rwfw_exists_chk


def rwfw_remote_exists(config_fpath):
    print(config_fpath.name)
    with open(config_fpath.name) as f:
        f_db = json.load(f)
        c_db = f_db['rwfw_img']
        # print(c_db)
        resultStr=rwfw_exists_chk(c_db['ip'], c_db['user'], c_db['pass'], c_db['path'])
        print(resultStr)
        if "AlteonOS" in resultStr:         
            c_db['img']=resultStr
            f_db['rwfw_img'] = c_db
            with open(config_fpath.name, 'w') as f:
                json.dump(f_db, f)
            build = resultStr.split('_')[-1].split('.')[0]
            print ('returing 1')
            return build
    print ('returing 2')
    return '-1'
    # with open(config_fpath) as f:
    # json.load(f)
    # c_db = f_db['rwfw_img']
    # return rwfw_exists_chk(c_db.ip, c_db.user, c_db.pass, c_db.path)


def rwfw_remote_build(config_fpath):
    ret_string = rwfw_remote_exists(config_fpath)
    # print(ret_string)
    # build = ret_string.split('_')[-1].split('.')[0]
    # print(build)
    return ret_string
    # return '-1'
