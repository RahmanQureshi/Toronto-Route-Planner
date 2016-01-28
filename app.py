from flask import Flask, send_from_directory, jsonify, request
import os
from RoadGraph import RoadGraph

app = Flask(__name__, static_url_path='/static')
app.debug = True
roadGraph = RoadGraph()

@app.route('/js/<path:jsFileName>')
def send_js(jsFileName):
    return send_from_directory('js', jsFileName)
    
@app.route('/css/<path:cssFileName>')
def send_css(cssFileName):
    return send_from_directory('css', cssFileName)

@app.route('/img/<path:imgFileName>')
def send_img(imgFileName):
    return send_from_directory('img', imgFileName)

@app.route('/former-municipalities')
def getFormerMunicipalities():
        return jsonify(roadGraph.get_boundary())

@app.route('/address-submit')
def addressSubmit():
    address_one = request.args.get('address_one')
    address_two = request.args.get('address_two')
    data = {
        'pretty-driving-directions': [],
        'latLngList': [],
        'length': -1,
    }
    try:
        weight, latLngList, directions = roadGraph.shortest_route(address_one, address_two)
        data = {
            'pretty-driving-directions': directions,
            'latLngList': latLngList,
            'length': weight
        }
    except Exception as e:
        print(e)
        data['error'] = e.message
    return jsonify(data)

@app.route('/')
def root():
    return app.send_static_file('index.html')


port = int(os.environ.get('PORT', 33507))
print("Binding to port: " + str(port))
app.run(host='0.0.0.0', port=port, use_reloader=False)