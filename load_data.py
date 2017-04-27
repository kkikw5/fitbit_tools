# coding: utf-8
import os
import sys
import csv
import argparse
import calendar
import datetime
sys.path.append('../settings/')
import pandas as pd
import pandas.tseries.offsets as offsets
import fitbit as fb
import gather_keys_oauth2 as Oauth2
import user

class Download:
    def __init__(self, client_id, client_secret,
                 access_token, refresh_token):
        """ Initiialize the FitbitOauth2Client """
        self.client = fb.Fitbit(
            client_id,
            client_secret,
            access_token=access_token,
            refresh_token=refresh_token
        )

    def load_heart(self, date, level='1min'):
        """ download heart rate """
        stats = self.client.intraday_time_series('activities/heart', base_date=date, detail_level=level)
        stats = stats["activities-heart-intraday"]["dataset"]
        return pd.DataFrame.from_dict(stats)

    def load_steps(self, level):
        stats = self.client.intraday_time_series('activities/steps', base_date=date, detail_level=level)
        stats = stats['activities-steps-intraday']['dataset']
        return pd.DataFrame.from_dict(stats)


def interpolate():
    """ interpolate """
    print('interpolate!!')

def df2csv(df, fn, path='./'):
    """ save dataFrame as csv file """
    df.to_csv(path + fn, index=True, encoding='utf-8')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Download fitbit data.')
    parser.add_argument('-a', '--all', action='store_true', default=False)
    parser.add_argument('-d', '--date', type=str, help='')
    parser.add_argument('--until', type=str, help='')
    parser.add_argument('-o', '--outdir', help='output directory')
    args = parser.parse_args()

    # for fitbit API
    server = Oauth2.OAuth2Server(user.fitbit_id, user.fitbit_secret)
    server.browser_authorize()
    ACCESS_TOKEN = server.fitbit.client.session.token['access_token']
    REFRESH_TOKEN = server.fitbit.client.session.token['refresh_token']
     
    dl = Download(user.fitbit_id,user.fitbit_secret,
                  ACCESS_TOKEN, REFRESH_TOKEN)
    cal = calendar.Calendar()

    if args.date:
        dt = datetime.date.today()
    else:
        dt = datetime.date.today()

    if not args.until:
        """ download """
        df = dl.load_heart(dt)
        try:
            df.index = pd.to_datetime([str(dt) + ' ' + t for t in df.time])
        except AttributeError:
            print('Error: empty data [', str(dt), ']')
        valid_index = pd.date_range(dt, dt + offsets.Day(), freq='1min', closed='left')
        df = df.reindex(valid_index)
        df2csv(df, 'heart-' + str(dt) + '.csv')

    else:
        """ download """
        print('download ')
        for i in range(10):
            print('hoge')