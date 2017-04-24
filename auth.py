# coding: utf-8
import sys

sys.path.append('../settings/')
from gather_keys_oauth2 import oauth
import user

if __name__ == '__main__':
    oauth(user.fitbit_id, user.fitbit_secret)