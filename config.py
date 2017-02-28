import os

basedir = os.path.abspath(os.path.dirname(__name__))

config = {
    'sqlite': 'sqlite:///{}/test.data'.format(basedir),
    'mysql': 'mysql+pymysql://root:passwd@localhost/ziroom?charset=utf8'
}
