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

test_ssh()
