import time
from rwfw_utils.models import rwfw_utils_imgdownload as rwfw_utils_imgdownload


def rwfw_ckver(rip, ru, rp, rl):
    print("Njan Okay")
    i = 5
    while i > 1 :
        i -= 1
        time.sleep(5)
        print("Njan Pinnem Okay")
    db1_obj = rwfw_utils_imgdownload.objects.filter(imgdwn_path=rl)
    if db1_obj.exists():
        print(db1_obj[0].imgdwn_name)
    else:
        print('NOT exists')
    return 135
