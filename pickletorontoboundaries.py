import shapefile
import pickle

fm_sf = shapefile.Reader("./toronto_shapefiles/former_municipality_wgs84/citygcs_former_municipality_wgs84")
fm_shapes = fm_sf.shapes()

toronto_boundary = [{'lat':e[1], 'lng':e[0]} for e in fm_shapes[5].points]

pickle.dump(toronto_boundary, open('torontoboundary.p', 'wb'))