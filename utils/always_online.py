import os
import time

from core.LoginManager import LoginManager


def is_online(test_ip):
    status = os.system(u"ping {} -c 8".format(test_ip))
    return status == 0


def always_login(username, password, testip, checkinterval):
    lm = LoginManager(username=username, passwd=password)
    login = lambda: lm.login()
    timestamp = lambda: print(time.asctime(time.localtime(time.time())))

    timestamp()
    try:
        login()
    except Exception:
        pass
    while 1:
        time.sleep(checkinterval)
        if not is_online(testip):
            timestamp()
            try:
                login()
            except Exception:
                pass


if __name__ == "__main__":
    username = "Your srun account name"
    password = "Your password"
    test_ip = "223.5.5.5"  # IP to test whether the Internet is connected
    check_interval = 5 * 60

    always_login(username, password, test_ip, check_interval)
