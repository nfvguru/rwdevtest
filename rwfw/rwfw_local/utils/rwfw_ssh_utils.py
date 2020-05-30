from pexpect import pxssh



def test_ssh():
    s = pxssh.pxssh()
    s.login('10.75.20.75', 'lava', 'lava')
    s.logout()

test_ssh
