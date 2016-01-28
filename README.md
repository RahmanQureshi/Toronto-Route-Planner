# Toronto Route Planner

Toronto route planner is a prototype solution to the UTEK 2016 Programming Competition package to assess viability, difficulty and to explore and understand the dataset. It computes the shortest path between two human-readable addresses, generates directions and displays it using google maps polylines.

## Demo

See live demo [here](http://toronto-route-planner.herokuapp.com/).

## Usage

1. Download the Address Points, Centerline Intersections, Centerline and Former Municipalities data sets in WGS84 format from the City of Toronto Data Catalogue and extract the folders into toronto_shapefiles directory
2. Type `pip install -r requirements.txt`
3. Generate the pickled data by typing in the following commands.
 - `python pickleaddresspoints.py`
 - `python pickleroadgraph.py`
 - `python pickletorontoboundaries.py`
4. Run using `python app.py`

(Credit to Johnson Zhong and Zhuowei Zhang for the clever pickling trick that enables faster startup time.)
