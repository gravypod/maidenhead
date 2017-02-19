from string import ascii_uppercase as letters
from itertools import starmap, combinations


MAX_LAT, MIN_LAT =  90,  -90
MAX_LON, MIN_LON = 180, -180

#  Total distance on the LAT scale
LAT_DISTANCE = (abs(MIN_LAT) + MAX_LAT)

#  Total distance on the LON scale
LON_DISTANCE = (abs(MIN_LON) + MAX_LON)


def slide(array, size=2):
	"""
	Slide an iteratable. This will chop of a list into `size` length bits.
	array - a collection of data
	size  - the length of every piece to take
	"""
	if len(array) % size != 0:
		raise Exception("Bad slide size!")

	for i in range(int(len(array) / size)):
		start = i * size

		yield array[start:start + size]


def parse_scale(lon_name, lat_name):
	"""
	Parse the Lon and Lat from their character representation.
	lon_name - A-z0-9 to parse.
	lat_name - A-z0-9 to parse.
	"""
	parse_letter = lambda letter: float(letters.index(letter.upper()))

	if lon_name.isdigit():
		return float(lon_name), float(lat_name)
	else:
		return parse_letter(lon_name), parse_letter(lat_name)


def square_sizes():
	"""
	Generate the patterns of the base sizes. This generates:
		 18, 10, 24, 10, 24, 10....
	This is needed for finding the step sizes.
	"""
	sizes = [18, 10, 24, 10]
	for size in sizes:
		yield size
	while True:
		for size in sizes[2:]:
			yield size


def grid2latlon(grid_name):
	"""
	Convert a grid square to a lat, lon, top_right_lat, top_right_lon.
	"""
	lon_step, lat_step = float(LON_DISTANCE), float(LAT_DISTANCE)
	lat, lon = float(MIN_LAT), float(MIN_LON)

	for (lon_scale, lat_scale), size in zip(starmap(parse_scale, slide(grid_name)), square_sizes()):
		lat_step /= size
		lon_step /= size
		lat += lat_step * lat_scale
		lon += lon_step * lon_scale

	return lat, lon, lat + lat_step, lon + lon_step


def latlon2grid(lat, lon):
	pass


if __name__ == "__main__":

	grid_name = "BL11bh"

	for lon_major, lat_major in combinations(letters[:19], 2):
		for lon_minor, lat_minor in combinations(list(range(10)), 2):
			grid_name = "{}{}{}{}".format(lon_major, lat_major, lon_minor, lat_minor)
			print(grid_name +":", grid2latlon(grid_name), ",")

	print(grid2latlon(grid_name))
