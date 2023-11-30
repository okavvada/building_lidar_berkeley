import os
from util.backBone import Building


def Search(path_to_lidar_directoy, database='building', User='Mike', host='localhost', projection=4326):
	try:
		files = [f for f in os.listdir(path_to_lidar_directoy) if f.endswith('.txt') or f.endswith('.csv')];
		assert (len(files) >0)
	except:
		print "Please provide a path directory containing '.txt' or '.csv' files types."

	# Load building class
	building = Building(files=files, database=database, User=User, host=host, projection=projection);


Search('../Data/Lidar', projection=32610);