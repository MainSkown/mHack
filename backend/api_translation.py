import requests
import urllib.parse
import json

class ApiTranslation():

    def __init__(self) -> None:
        
        self.api_command = ''
        self.specialist = ''
        self.province = '01'
        self.forChildren = 'false'
        self.provider = ''
        self.place = ''
        self.street = ''
        self.locality = ''
        self.disabled = ''
        self.elevator = ''
    
    def get_request(self, request: dict):

        self.specialist = request.get('specialist', '')
        self.province = request.get('province', '')
        self.forChildren = request.get('forChildren', 'false')
        self.provider = request.get('provider', '')
        self.place = request.get('place', '')
        self.street = request.get('street', '')
        self.locality = request.get('locality', '')
        self.disabled = request.get('disabled', '')
        self.elevator = request.get('elevator', '')

    def html_parse(self, to_parse: str):

        return urllib.parse.quote(to_parse)


    def constructing_filters(self):

        if self.province: #must have

            self.province = "&province=" + self.province
        
        self.forChildren = "&benefitForChildren=" + str(self.forChildren) #must have

        if self.provider:

            self.provider = "&provider=" + self.provider

        if self.place:

            self.place = "&place=" + self.place
        
        if self.street:

            self.street = "&street=" + self.street    
        
        if self.locality:

            self.locality = "&locality=" + self.locality


    def generating_api_command(self):
        
        self.api_command = "https://api.nfz.gov.pl/app-itl-api/queues?page=1&limit=25&format=json&case=1" + self.province + self.forChildren + self.provider + self.place + self.street + self.html_parse(self.locality)+ "&api-version=1.3"
        print(self.api_command)


    def getting_json(self):

        try:

            response = requests.get(self.api_command)

            if response.status_code == 200:

                json_data = response.json()
                json_data = json_data['data']

                return self.response_generator(json_data)

            else:
                
                return {
                        "status":503,
                        "error":"Internal Server Error"
                        }
        
        except Exception as e:
            print(f"An error occurred: {e}")


    def response_generator(self, json_data: list):

        data_list = []


        for record in json_data:

            temp_location_template = {
                                    'city' : None,
                                    'street' : None,
                                    }
            temp_data_template = {
                                'queue_id': None,
                                'place_name' : None,
                                'location': temp_location_template,
                                'visit_date' : None,
                                'visit_name' : None,
                                'phone': None
                             }
            
            temp_location_template['city'] = record['attributes']['locality']
            temp_location_template['street'] = record['attributes']['address']

            temp_data_template['queue_id'] = record['id']
            temp_data_template['place_name'] = record['attributes']['provider']
            temp_data_template['location'] = temp_location_template
            temp_data_template['visit_date'] = record['attributes']['dates']['date']
            temp_data_template['visit_name'] = record['attributes']['benefit']
            temp_data_template['phone'] = record['attributes']['phone']
            

            data_list.append(temp_data_template)


        return data_list

d = {"specialist": "",
    "province": "05",
    "forChildren": False,
    "provider": "",
    "place": "stomatolog",
    "street": "",
    "locality": "",
    "disabled": "",
    "elevator": ""}

# c = ApiTranslation()
# c.get_request(d)
# c.constructing_filters()
# c.generating_api_command()
# c.getting_json()



