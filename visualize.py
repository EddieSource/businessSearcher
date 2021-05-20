# Import gmplot library.
import gmplot
import pandas

# read the coordiantes data from the csv file
colnames = ['latitude', 'longitude']

# use your sample file csv file here
data = pandas.read_csv('companies_with_coordiantes.csv', names=colnames, header=1)

latitude_list = data.latitude.tolist()
longitude_list = data.longitude.tolist()

# insert your own api key
gmap = gmplot.GoogleMapPlotter.from_geocode( 'New York, NY, USA', apikey='')

# set marker to be false if you just want scatter points
gmap.scatter(latitude_list, longitude_list, '#FF0000', size=40, marker=True)

# Location where you want to save your file.
gmap.draw('map.html')