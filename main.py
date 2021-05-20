import requests
import json
import csv

# insert your api_key
api_key=''

headers = {'Authorization': 'Bearer %s' % api_key}

# using yelp's api
url='https://api.yelp.com/v3/businesses/search'

# set up col and row for csv file
cols = ['Name', 'Phone', 'Latitude', 'Longitude']
rows = []

# initialize a dict to deduplicate phone_number
phone_number = {}

# limit is 50 for each request, and it can give up to 1000 result, and so we call 20 times with offset.
for i in range(0, 1000, 50):
    params = {'term': 'law', 'location': 'New York City', 'limit': 50, 'offset': i}
    # Making a get request to the API
    req=requests.get(url, params=params, headers=headers)

    # proceed only if the status code is 200
    print(i, 'th try. The status code is {}'.format(req.status_code))

    business_collection = json.loads(req.text)
    #ready to change it to csv file
    for business in business_collection["businesses"]:
        # print("name:", business["name"])
        # print("phone: ", business["phone"])
        # print("coordinates:", business['coordinates'])
        if business['phone'] not in phone_number:
            rows.append([business['name'], business['phone'], business['coordinates']['latitude'], business['coordinates']['longitude']])
            phone_number[business['phone']] = 1
        print('')

with open('companies_with_coordiantes.csv', 'w') as f:
    write = csv.writer(f)
    write.writerow(cols)
    write.writerows(rows)







