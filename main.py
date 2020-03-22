import requests
import json
from geopy.geocoders import Nominatim
from gmplot import gmplot


class Space:

    # Doing requests
    response1 = requests.get("http://api.open-notify.org/astros.json")
    response2 = requests.get("http://api.open-notify.org/iss-now.json")

#Prints out current astronauts in space
    def get_astronauts_in_space(self):

        try:
            #check success
            if self.response1.status_code == 200:
                print("Request success")
                readable_text = json.dumps(self.response1.json(), sort_keys=True, indent=4)
                print(readable_text)

            else:
                print("Ups, something went wrong. Status Code: " + str(requests.status_codes))

        except:
            print("An Error occurred in get_ISS_Location()")


#Prints out ISS Location and finds corresponding address
    def get_ISS_Location(self):

        # check success
        if self.response2.status_code == 200:
            print("Request success")
            readable_text = json.dumps(self.response2.json(), sort_keys=True, indent=4)
            print(readable_text)

            #extracts coordinates
            coordinates = self.response2.json()['iss_position']
            latitude = coordinates["latitude"]
            longitude = coordinates["longitude"]

            #Gives you current position as an adress
            geolocator = Nominatim(user_agent="some_name")
            address_query = "{}, {}".format(latitude, longitude)
            location = geolocator.reverse(address_query)

            if location.address != None:
                print(location.address)
            else:
                print("No address for this location available. It's in the nowhere. Please try again in a few seconds!")

            #get position on google maps and save it as PDF
            gmap = gmplot.GoogleMapPlotter(float(latitude), float(longitude), 13)
            gmap.marker(float(latitude), float(longitude), 'cornflowerblue')
            gmap.draw("my_map.html")

        else:
            print("Ups, something went wrong. Status Code: " + str(requests.status_codes))


Space().get_astronauts_in_space()
Space().get_ISS_Location()








