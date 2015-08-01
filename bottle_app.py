# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route, template
import requests,get_weather

@route('/')
def hello_world():
    return "hello vvk"

@route('/data')
def hello_world():
    data = (
        { "lat":43.52,"lon":68.50,"temp":29.3,"city":"kent"},
        { "lat":41.09,"lon":-80.64,"temp":22,"city":"youngstown"},
        { "lat":31.5,"lon":-84.87,"temp":25.6,"city":"cleveland"}
    )
    my_names = ["Dave","John","Sally","Liz","Aaron"]
    return template("sample",data=data)



@route('/data1')
def hello_table():
    req = requests.get('http://api.openweathermap.org/data/2.5/find?lat=41.099781&lon=-80.649521&cnt=10')
    data = req.json()
    rows=[]
    for i in range(0,8):
        tempk = data['list'][i]['main']['temp']
        tempc = tempk - 273.16
        tempf = tempc * 1.8 + 32.0
        f2 = data['list'][i]['coord']['lat']
        f3 = data['list'][i]['coord']['lon']
        nam = data['list'][i]['name']
        rows.append((f2,f3,tempf,nam))
    return template("sample1",rows=rows)

@route('/chart')
def chart_ikl():
     return template("chart")

@route('/chart1')
def chart_1():
     return template("chart1")

@route('/map')
def map_1():
     return template("map")

@route('/map1')
def stream_data():
   # req = requests.get('https://data.sparkfun.com/output/pwvdJgMDnETWRaDRNlxo.json?')
   # data = req.json()
    req = requests.get('http://api.openweathermap.org/data/2.5/find?lat=41.099781&lon=-80.649521&cnt=10')
    data = req.json()
    rows=[]
    for i in range(0,10):
        tempk = data['list'][i]['main']['temp']
        tempc = tempk - 273.16
        tempf = tempc * 1.8 + 32.0
        f2 = data['list'][i]['coord']['lat']
        f3 = data['list'][i]['coord']['lon']
        nam = data['list'][i]['name']
        #we = ['list'][i]['weather'][0]['main']
        #humidity = data['list'][i]['main']['humidity']
        rows.append((f2,f3,tempf,nam))
    return template('map1',rows=rows)

@route('/usaMap')
def map_route():
    list = get_weather.get_weather_list()
    states = []
    reds = []
    greens = []
    blues = []
    for item in list:
        states.append(item)
        reds.append(list[item]['humidity']*2)
        greens.append(0)
        blues.append(int(list[item]['temp']-273)*5)
    return template("unfinished", states = states, reds = reds, greens = greens, blues = blues)

@route('/map2')
def map_2():
    req=requests.get('https://data.sparkfun.com/output/q5XKJ7pYq0fANqbJbZrO.json?')
    data = req.json()
    return template("map2",data=data)

@route('/weather')
def weather_data():
    req=requests.get('https://data.sparkfun.com/output/q5XKJ7pYq0fANqbJbZrO.json?')
    data = req.json()
    return template('weather',data=data)

@route('/visualization')
def visual():
     return template("visualization")

application = default_app()
