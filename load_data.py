# coding: utf-8
import os
import sys
import argparse
import calendar
sys.path.append('../settings/')
import pandas as pd
import fitbit as fb
import user

def load_hr():
    print('hoge')

def dict2df(raw):
    return pd.DataFrame.from_dict(raw)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Download fitbit data.')
    parser.add_argument('--heart', type=int, help='download heart rate')
    parser.add_argument('--steps', type=int, help='download # of steps')
    parser.add_argument('-d', '--day', type=int, help='')
    parser.add_argument('-m', '--month', type=int, help='')
    parser.add_argument('year', type=int, help='')
    parser.add_argument('outdir', help='output directory')
    args = parser.parse_args()

    cal = calendar.Calendar()
    if args.month:
        # print(args.month)
        if args.day:
            print(args.day)
        else:
            for d in cal.itermonthdays(args.year, args.month):
                if d:
                    print(d)
    else:
        for m in range(1, 13):
            print(m)

    # # setting
    # client = fb.Fitbit(user.fitbit_id,
    #                    user.fitbit_secret,
    #                    access_token=user.fitbit_access_token,
    #                    refresh_token=user.fitbit_refresh_token)
    
    # # haert rate
    # dat = client.intraday_time_series('activities/heart', '2017-04-01', detail_level='1sec')
    # hr = dat["activities-heart-intraday"]["dataset"]
    # df = dict2df(hr)
    # print(df.shape)
    # df.head()

    # df.index = pd.to_datetime(['2017-04-01' + " " + t for t in df.time])
    # df.head()
    # print(df)