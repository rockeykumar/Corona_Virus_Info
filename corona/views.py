import csv
import pandas as pd
from django.shortcuts import render


def index(request):
    url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv'
    cr = pd.read_csv(url).values.tolist()
    row = len(cr)
    col = len(cr[0])

    dict = {}
    for row in range(row):
        state = cr[row][0]
        country = cr[row][1]
        total = cr[row][col-1]
        change = total - cr[row][col-2]
        list = {'state': state, 'country': country, 'total': total, 'change': change}
        dict[row] = list
    #
    # print(dict[0])
    return render(request, 'index.html', {'dict': dict})

