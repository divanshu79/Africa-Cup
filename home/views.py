from django.shortcuts import render
import pandas as pd
import folium
import numpy as np
import os


def highlight_function(feature):
    return {
        'fillColor': '#ffaf00',
        'color': 'green',
        'weight': 3,
        'dashArray': '5, 5'
    }


def find_ans(host, team, a, b):
    m = folium.Map(
        location=[10, 20],
        zoom_start=3,
        tiles='cartodbpositron',
        control_scale=True,
        prefer_canvas=True
    )

    df = pd.read_json('E:/job/ptoj/ASS/3rd/my_work/AFRICA_CUP_OF_NATION/home/cc.json')

    def my_color_function(feature):
        if feature['properties']['name'] in np.array(host[team]):
            return '#ff0000'
        else:
            return '#008000'

    def style_function(feature):
        return {
            'fillColor': my_color_function(feature),
            'color': 'blue',
            'weight': 1.5,
            'dashArray': '5, 5'
        }

    def winner_count(feature):
        h1 = host[host[team] == feature['properties']['name']]
        h1.reset_index()
        t = len(h1.index)
        if t == 0:
            return ''
        else:
            return t

    for i, j in df.iterrows():
        c = folium.GeoJson(
            j['features'],
            name=('{}{}'.format(j['features']['properties']['name'], winner_count(j['features']))),
            overlay=True,
            style_function=style_function,
            highlight_function=highlight_function
        )
        folium.Popup('{}\n{}'.format(j['features']['properties']['name'], winner_count(j['features']))).add_to(c)
        c.add_to(m)

    folium.LayerControl().add_to(m)
    m.save('home/templates/home/' + str(team) + str(a) + str(b) + '.html')

    return 0


def winner(type1, a, b):
    h = pd.read_csv('home/data/' + str(type1) + '.csv', encoding='ISO-8859-1')
    if a < b:
        host = h[(h['year'] >= int(a)) & (h['year'] <= int(b))]
        find_ans(host, type1, a, b)
        return 1
    elif a == b:
        host = h[h['year'] == int(a)]
        find_ans(host, type1, a, b)
        return 1
    else:
        return 0



def check(request):
    type1 = request.GET.get('type')
    form_year = request.GET.get('Form_year')
    to_year = request.GET.get('To_year')

    if type1 == 'winner':
        try:
            return render(request, 'home/' + str(type1) + str(form_year) + str(to_year) + '.html')
        except:
            k = winner(type1, form_year, to_year)
            if k == 1:
                return render(request, 'home/' + str(type1) + str(form_year) + str(to_year) + '.html')

            else:
                return render(request, 'home/404_error.html')
    elif type1 == 'host':
        try:
            return render(request, 'home/' + str(type1) + str(form_year) + str(to_year) + '.html')
        except:
            k = winner(type1, form_year, to_year)
            if k == 1:
                return render(request, 'home/' + str(type1) + str(form_year) + str(to_year) + '.html')
            else:
                return render(request, 'home/404_error.html')
    elif type1 == 'team':
        try:
            return render(request, 'home/' + str(type1) + str(form_year) + str(to_year) + '.html')
        except:
            k = winner(type1, form_year, to_year)
            if k == 1:
                return render(request, 'home/' + str(type1) + str(form_year) + str(to_year) + '.html')
            else:
                return render(request, 'home/404_error.html')
def home(request):
    data = pd.read_csv('home/data/winner.csv', encoding='ISO-8859-1')
    year = np.array(data['year'])
    year1 = year[::-1]

    return render(request, 'home/home.html', {'year': year, 'year1': year1})

