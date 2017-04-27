# coding: utf-8
import sys
sys.path.append('../settings/')
import gather_keys_oauth2 as Oauth2
import user

# get tokens to use fitbit API
if __name__ == '__main__':
    server = Oauth2.OAuth2Server(user.fitbit_id, user.fitbit_secret)
    server.browser_authorize()
