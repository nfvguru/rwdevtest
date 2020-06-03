import fabric
from django.conf import settings
import os

def sampleLinux():
    c= fabric.Connection(host='10.75.20.75', port=22, user='lava', connect_kwargs={'password':'lava'})
    #c.run('touch lava_fabric_test.txt')
    c.put('testLLL.txt', 'lava_fab_put')
    c.get('AlteonOS-32.6.1.0_may12.img', '/home/devtest/Projects/rwdevtest/rwfw/downloads/AlteonOS-32.6.1.0_may12.img')


def sampleWindows():
    c= fabric.Connection(host='10.75.20.75', port=22, user='lava', connect_kwargs={'password':'lava'})
    c.put('testLLL.txt', 'lava_fab_put_win')


# if os.name == 'nt' :
#     sampleWindows()
# else :
#     sampleLinux()

def rwfw_fabric_download(rip, ru, rp, rl, ri):
    conn_ptr = fabric.Connection(host=rip, port=22, user=ru, connect_kwargs={'password':rp})
    p_sep = '/'
    if os.name == 'nt' :
        p_sep = '\\'
    dwn_path = os.path.join(settings.BASE_DIR,'downloads')
    dwn_img  =  dwn_path + p_sep + ri
    print(dwn_img)
    remote_img  =  rl + '/' + ri
    print(remote_img)
    conn_ptr.get(remote_img, dwn_img)
    return "Success"
