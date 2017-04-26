# coding: utf-8
import os
import sys
import argparse
import calendar
import datetime
sys.path.append('../settings/')
import pandas as pd
import fitbit as fb
import user


def dict2df(raw):
    return pd.DataFrame.from_dict(raw)

def load_hr(day, month, year, level='1sec'):
    # haert rate
    date = '-'.join([year, str(month).zfill(2), str(day).zfill(2)])
    dat = client.intraday_time_series('activities/heart', date, detail_level=level)
    dat = dat["activities-heart-intraday"]["dataset"]
    return dict2df(dat)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Download fitbit data.')
    parser.add_argument('--heart', type=int, help='download heart rate')
    parser.add_argument('--steps', type=int, help='download # of steps')
    parser.add_argument('-y', '--year', type=str, help='')
    parser.add_argument('-m', '--month', type=str, help='')
    parser.add_argument('-d', '--day', type=str, help='')
    parser.add_argument('outdir', help='output directory')
    args = parser.parse_args()

    if not args.year:
        
    cal = calendar.Calendar()
    if args.month:
        # print(args.month)
        if args.day:
            print(args.day)
            load_hr(args.day, args.month, args.year)
        else:
            for d in cal.itermonthdays(args.year, args.month):
                if not d: continue
                load_hr(d, args.month, args.year)
    else:
        for m in range(1, 13):
            print(m)
            load_hr(args.day, args.month, args.year)

    # # setting
    # client = fb.Fitbit(user.fitbit_id,
    #                    user.fitbit_secret,
    #                    access_token=user.fitbit_access_token,
    #                    refresh_token=user.fitbit_refresh_token)
    
    # df.index = pd.to_datetime(['2017-04-01' + " " + t for t in df.time])
    # df.head()
    # print(df)