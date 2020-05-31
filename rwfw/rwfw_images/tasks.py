from celery import shared_task
from rwfw_local.utils.rwfw_download_utils import rwfw_ckver


@shared_task
def adding_task(x, y):
    return x + y

@shared_task
def rwfw_chkdownload_image(rip, ru, rp, rl):
    bnum = rwfw_ckver(rip, ru, rp, rl)
    return bnum

@shared_task
def rwfw_dodownload_image(rl):
    print(rl)
    return 100
