# description: Generates a map from human-readable addresses to address records

import shapefile
import pickle

path = './toronto_shapefiles'
ap_sf = shapefile.Reader(path + "/address_points_wgs84/ADDRESS_POINT_WGS84")
municipalities = ['former toronto'] # address scope for memory reasons

ap_map = {}

for record in ap_sf.iterRecords():
    if record[20].lower() in municipalities:
        # GEO_ID, LINK, ADDRESS_NUMBER, LFNAME, LONG, LAT
        reduced_record = [record[0], record[1], record[3], record[4], record[17], record[18]]
        ap_map[record[3] + ' ' + record[4].lower()] = reduced_record

pickle.dump(ap_map, open('addresspoints.p', 'wb'))