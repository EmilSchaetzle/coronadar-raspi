import requests

def post(lon, lat, count):
	data = {'loc':{'lon':lon,'lat':lat}, 'count':count}
	try:		
		res = requests.post(url='https://api2.coronadar.de/location/', json=data)
		print(vars(res))
		print(res.text)
	except Exception as e:
		print(e)
