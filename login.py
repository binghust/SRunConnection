import argparse

from core.LoginManager import LoginManager

parser = argparse.ArgumentParser(description='命令行参数')
parser.add_argument('-u', '--username', type=str, help='账号，必须参数', required=True)
parser.add_argument('-p', '--password', type=str, help='密码，必须参数', required=True)
args = vars(parser.parse_args())

lm = LoginManager(username=args['username'], passwd=args['password'])
lm.login()
