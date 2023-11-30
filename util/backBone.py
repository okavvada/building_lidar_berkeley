import pandas as pd, numpy as np
from ntpath import basename

from pgDataLoader import pgDataLoader
from pgMethods import Methods
from pyCluster import dbscan

class Building:
	def __init__(self, database='building', User='Olga', host='localhost', projection=4326, transform_to=None):
		# If the dataset is not in metric units, transform projection
		self.transform_to = transform_to;

		# file uploads 
		self.upload = pgDataLoader(database=database, User=User, host=host, projection=projection)

		# methods to cal to server
		self.methods = Methods(database=database, User=User, host=host, projection=projection);

		# Reset storage tables
		self.methods.tableSetUp(transform_to=transform_to);


if __name__ == "__main__":
	b = Building(transform_to=5070)