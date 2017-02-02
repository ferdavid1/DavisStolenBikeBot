from craigslist import CraigslistForSale, CraigslistEvents
import json
from twilio.rest import TwilioRestClient

json_data = open('twilioauth.json').read()
data = json.loads(json_data)

accountsid = data['ACCOUNT SID']
token = data['TOKEN']
twilioCli = TwilioRestClient(accountsid, token)
myTwilioNumber = data['TwilioNum']
myCellPhone = data['MyNum']

query = ['purple', 'schwinn', 'bike', 'bicycle', 'hybrid', 'Bike', 'Bicycle', 'Schwinn', 'Purple', 'womens', 'ladies']
cl_e = CraigslistForSale(site='sacramento', filters={'search_titles':True, 'query':'bike', 'has_image':True})

print('/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////\n')
print('Results:\n')

for result in cl_e.get_results(sort_by='newest', limit=3000):
	if result['where'] == ('Davis' or 'Davis, CA' or 'davis'):
		for search in query:
			if search in result['name']:
				print ('Location: {}\n'.format(result['where']))
				print ('Date: {}\n'.format(result['datetime']))
				print ('Post Title: {}\n'.format(result['name']))
				print ('URL: {}\n'.format(result['url']))
				print ('Price: {}\n'.format(result['price']))
				print ('Has an Image Available (True or False): {}\n'.format(result['has_image']))
		if query[0] and query[1] in result['name']:
			print('Red Alert')
			badmessage = twilioCli.messages.create(body='Suspicious Sale posted', from_=myTwilioNumber, to=myCellPhone)
			exec(message)
		elif query[0] and query[4] in result['name']:
			print('Red Alert')
			exec(badmessage)
		elif query[7] and query[8] in result['name']:
			print('Red Alert')
			exec(badmessage)
		else:
			print('This is not a clear suspicion\n\n'.upper())
print('////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////')    

regmessage = twilioCli.messages.create(body='No Suspicious Sales made today', from_=myTwilioNumber, to=myCellPhone)
regmessage