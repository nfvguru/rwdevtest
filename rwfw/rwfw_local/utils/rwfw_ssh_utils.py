import os
if os.name != 'nt':
    import pexpect
    from pexpect import pxssh




def test_ssh():
    s = pxssh.pxssh()
    s.login('10.75.20.75', 'lava', 'lava')

    s.sendline('uptime')   # run a command
    s.prompt()             # match the prompt
    print(s.before)        # print everything before the prompt.
    s.sendline('ls -l')
    s.prompt()
    print(s.before)
    s.logout()

def rwfw_exists_chk(rip, ru, rp, rl):
    if os.name == 'nt':
        return 'AlteonOS-32.6.2.0_dbg_35.ova'
    s = pxssh.pxssh()
    s.login(rip, ru, rp)
    my_cmd = 'ls ' + rl
    s.sendline(my_cmd)
    s.prompt()
    return s.before.decode('utf-8').split('\r\n')[1]

def rwfw_ftp_client(rip, ru, rp, rl, ri):
    print("seetha")
    newru='reluser'
    newrp='qwerty1!'
    f_cmd='ftp ' + rip + ' ,timeout=100000'
    print(f_cmd)
    child = pexpect.spawn (f_cmd)
    child.expect ('Name .*: ')
    child.sendline (newru)
    child.expect ('Password:')
    child.sendline (newrp)
    child.expect ('ftp> ')
    print(child.before)
    child.sendline ('lcd /home/devtest/Projects/rwdevtest/rwfw')
    child.expect ('ftp> ')
    print(child.before)
    child.sendline ('bin')
    child.expect ('ftp> ')
    cd_cmd = 'cd '+ rl
    print(cd_cmd)
    child.sendline (cd_cmd)
    child.expect('ftp> ')
    gt_cmd = 'get ' + ri
    print(gt_cmd)
    child.sendline (gt_cmd)
    child.expect('ftp> ')
    print(child.before)
    child.sendline ('bye')
    print("Satyam")



def rwfw_do_ftp(rip, ru, rp, rl, ri):
    if os.name == 'nt':
        return 'Success'
    print("MAAANOOO");
    rwfw_ftp_client(rip, ru, rp, rl, ri)
    return "Success"
