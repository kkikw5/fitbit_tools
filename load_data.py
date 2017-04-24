# coding: utf-8
import sys
import argparse
import calendar as cal
sys.path.append('../settings/')
import pandas as pd
import fitbit as fb
import user

def load_hr():
    print('hoge')

def dict2df(raw):
    return pd.DataFrame.from_dict(raw)

if __name__ == '__main__':
    
    # setting
    client = fb.Fitbit(user.fitbit_id,
                       user.fitbit_secret,
                       access_token=user.fitbit_access_token,
                       refresh_token=user.fitbit_refresh_token)
    
    # haert rate
    dat = client.intraday_time_series('activities/heart', '2017-04-01', detail_level='1sec')
    hr = dat["activities-heart-intraday"]["dataset"]
    df = dict2df(hr)
    print(df.shape)
    df.head()

    df.index = pd.to_datetime(['2017-04-01' + " " + t for t in df.time])
    df.head()
    print(df)