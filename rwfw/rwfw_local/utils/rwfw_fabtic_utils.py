import fabric

c= fabric.Connection(host='10.75.20.75', port=22, user='lava', connect_kwargs={'password':'lava'})
#c.run('touch lava_fabric_test.txt')
c.put('testLLL.txt', 'lava_fab_put')
c.get('AlteonOS-32.6.1.0_may12.img', '/home/devtest/Projects/rwdevtest/rwfw/downloads/AlteonOS-32.6.1.0_may12.img')
