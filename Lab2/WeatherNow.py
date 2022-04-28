from requests import get
from time import sleep
from os import system
from datetime import date
import json

def WeatherIcon(weatherN, line=1):
	if(weatherN=="Sun"):
		if(line==1): return "     ▒     "
		if(line==2): return " ▒ ▒▒▒▒▒ ▒ "
		if(line==3): return "  ▒     ▒  "
		if(line==4): return "▒▒▒     ▒▒▒"
		if(line==5): return "  ▒     ▒  "
		if(line==6): return " ▒ ▒▒▒▒▒ ▒ "
		if(line==7): return "     ▒     "
	if(weatherN=="Clouds"):
		if(line==2): return " ▒▒▒▒ ▒▒▒▒ "
		if(line==3): return "▒    ▒    ▒"
		if(line==4): return "▒▒▒▒▒▒▒▒▒▒▒"
	if(weatherN=="Snow"):
		if(line==1): return " ▒   ▒   ▒ "
		if(line==2): return "  ▒  ▒  ▒  "
		if(line==3): return "   ▒ ▒▒▒   "
		if(line==4): return "   ▒▒▒ ▒   "
		if(line==5): return "  ▒  ▒  ▒  "
		if(line==6): return " ▒   ▒   ▒ "
	if(weatherN=="Rain"):
		if(line==1): return " ▒▒▒▒▒ ▒▒▒ "
		if(line==2): return "▒     ▒   ▒"
		if(line==3): return "▒▒▒▒▒▒▒▒▒▒▒"
		if(line==4): return "  ▒  ▒  ▒  "
		if(line==5): return " ▒  ▒  ▒   "
		if(line==6): return "▒  ▒  ▒    "
	return "           "

def StaticPrint(Aday, Aweek, Location):
        print("╔═════════════╦═════════════════════════════════════════╗")
        print("║ {wet:6s} ║ Город: {loc:20s}             ║".format(wet = WeatherIcon(Aday['weather'][0]['main'], 1), loc=Location))
        print("║ {wet:6s} ║ Погода: {dt:25s}       ║".format(wet = WeatherIcon(Aday['weather'][0]['main'], 2), dt=Aday['weather'][0]['description']))
        print("║ {wet:6s} ║ Температура: {dt:14.2f} °C          ║".format(wet = WeatherIcon(Aday['weather'][0]['main'], 3), dt=Aday['main']['temp']))
        print("║ {wet:6s} ║ Влажность: {dt:8d} %  Ветер: {dr2:5.3f} m/c ║".format(wet = WeatherIcon(Aday['weather'][0]['main'], 4), dt=Aday['main']['humidity'], dr2 = Aday['wind']['speed']))
        print("║ {wet:6s} ║ Давление: {dt:8d} Pa  Вид-ть: {dr2:5d} m  ║".format(wet = WeatherIcon(Aday['weather'][0]['main'], 5), dt=Aday['main']['pressure'], dr2 = Aday['visibility']))
        print("║ {wet:6s} ║                                         ║".format(wet = WeatherIcon(Aday['weather'][0]['main'], 6)))
        print("║ {wet:6s} ║ Дата: {dt:10s}                        ║".format(wet = WeatherIcon(Aday['weather'][0]['main'], 7), dt = str(date.today())))
        print("╠═════════════╩═════════════════════════════════════════╣")
        print("║             Прогноз погоды на неделю:                 ║")
        for i in Aweek:
                print("╠═══════════════════════════════════════════════════════╣")
                print(f"║Прогноз погоды на {i['dt_txt'][:10:]}: {i['weather'][0]['description']:25s}║")
                print(f"║Темп:{i['main']['temp']:5.2f}°C Давл:{i['main']['pressure']:5.1f}Pa Ветер:{i['wind']['speed']:3.1f}m/c Вид-ть:{i['visibility']:5d}m  ║")
        print("╠═══════════════════════════════════════════════════════╣")
        print("║ Erokhin K © 2022                                      ║")
        print("╚═══════════════════════════════════════════════════════╝")

def LocationFinder():
        IpFinderURL = r"https://icanhazip.com"          #Ip Adress request service URL
        a = json.loads(get(r"https://ipapi.co/" + get(IpFinderURL).text[:-1] + r"/json").text)
        return a['city'] + r"," + a['country']

def WeatherFinder(location, key):
        return get("http://api.openweathermap.org/data/2.5/weather",params=
        {'q': location, 'units': 'metric', 'lang': 'ru', 'APPID': key}).json()

def WeatherWeek(location, key):
	 return get("http://api.openweathermap.org/data/2.5/forecast",params=
        {'q': location, 'units': 'metric', 'lang': 'ru', 'APPID': key}).json()

def main():
        key = "HERE IS YOUR !OPENWRATHERMAP! KEY"
        while(True):
                location = LocationFinder()
                system("clear")
                weather_stat = WeatherFinder(location, key)
                weather_week = WeatherWeek(location, key)
                #print(weather_stat)
                StaticPrint(weather_stat, weather_week['list'][7::8], location)
                sleep(20)
main()
