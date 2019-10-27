import requests
import json

class GetLocation():

	URL_MAIN = "https://eu1.locationiq.com/v1/"
	FORWARD_SERCH = "search.php"
	REVERSE_SEARCH = "reverse.php"
	data = {
	'key': '21a6a444588a80',
	'q': None,
	'lat': None,
	'lon': None,
	'format': 'json'
	}
	
	def get_requests(self, url, params):
		response = requests.get(url, params)
		return json.loads(response.text)

	def get_location_by_place (self, q_format):
		url = self.URL_MAIN+self.FORWARD_SERCH
		self.data['q'] = str(q_format)
		params = self.data
		return self.get_requests(url, params)

	def get_location_by_coords(self, lat, lon):
		url = self.URL_MAIN+self.REVERSE_SEARCH
		self.data['lat'] = str(lat)
		self.data['lon'] = str(lon)
		params = self.data
		return self.get_requests(url, params)


get = GetLocation()
coords = get.get_location_by_place('luvr')
print("Place: {} \nLon: {}, Lat: {}".format(coords[0]['display_name'], coords[0]['lat'], coords[1]['lon']))
print(get.get_location_by_coords('14.333', '78.222')['display_name'])


#Homework4 for pull_request

