from celery import shared_task

@shared_task
def adding_task(x, y):
    return x + y

@shared_task
def rwfw_download_image(rip, ru, rp, rl):
    print(rip)
    print(ru)
    print(rp)
    print(rl)
    return 1
