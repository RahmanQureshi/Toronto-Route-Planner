# description: Generates graph of roads (excluding highways) in the City of Toronto and neighboring municipalities.

import shapefile
import networkx
from haversine import haversine
import pickle

path = './toronto_shapefiles'
cl_sf = shapefile.Reader(path + "/centreline_wgs84/CENTRELINE_WGS84")
cli_sf = shapefile.Reader(path + "/centreline_intersection_wgs84/CENTRELINE_INTERSECTION_WGS84")
cl_inclusion_list = [201200, 201201, 201300, 201301, 201400, 201401, 201500, 201600, 201601, 201700, 201800]
G = networkx.Graph()

def get_cl_length(points):
    return sum([haversine((points[i][1], points[i][0]), (points[i+1][1], points[i+1][0])) for i in range(len(points)-1)])

for shapeRecord in cl_sf.iterShapeRecords():
    if shapeRecord.record[13] in cl_inclusion_list:
        w = get_cl_length(shapeRecord.shape.points)
        G.add_edge(shapeRecord.record[11], shapeRecord.record[12], weight=w, record=shapeRecord.record, shape=shapeRecord.shape.points)

for record in cli_sf.iterRecords():
    G.node[record[0]] = record

pickle.dump(G, open('roadgraph.p', 'wb'))