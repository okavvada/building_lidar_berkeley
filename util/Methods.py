import os
import pandas as pd
from sqlalchemy import create_engine
import string, random

class Methods:
	def __init__(self, database='building', User='Olga', host='localhost', projection=4326):
		# Start server 
		self.start_server(database, User, host)

		# Set projection
		self.projection = projection

	def start_server(self, database, User, host):
		# save database
		self.database = database

		# save cursor
		self.cur  = create_engine('postgresql://%s@%s:5432/%s' % (User, host,database))

	def pg_post(self, SQLcommand):
		connection = self.cur.connect()
		connection.execute(SQLcommand);
		connection.close()

	def pg_df(self, SQLcommand):
		
		return pd.read_sql(SQLcommand, self.cur)


	def df_pg(self, dataframe, table_name, if_exists='replace'):
		
		return dataframe.to_sql(table_name, self.cur, if_exists=if_exists)


	def tableSetUp(self, transform_to=None):
		if transform_to:
			projection = transform_to
		else:
			projection = self.projection 
		# Create connection
		connection = self.cur.connect()
		connection.execute("""DROP TABLE IF EXISTS spill_over_master; DROP TABLE IF EXISTS geometries_master; DROP TABLE IF EXISTS points_master;""")
		connection.execute("""CREATE TABLE  spill_over_master (x double precision, y double precision, z double precision, the_geom geometry(Point,%s));""" % projection);
		connection.execute("""CREATE TABLE  geometries_master (label bigint, height double precision, the_geom geometry)""");
		connection.execute("""CREATE TABLE  points_master (x double precision, y double precision, z double precision, the_geom geometry(Point,%s));""" % projection);
		connection.close()


