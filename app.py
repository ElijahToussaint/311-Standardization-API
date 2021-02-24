import os, pandas
from flask import Flask, render_template, jsonify
from flask.helpers import send_file

app = Flask(__name__)

# Replace the existing home function with the one below
@app.route("/")
def home():
    path = './standardized_data/311_standardized/'
    cities = []
    #files = []
    dataList = []
    for directories in os.listdir(path):
        #print(directories)
        cities.append(directories)
        relativePath = os.path.join(path, directories)
        files = []
        for file in os.listdir(relativePath):
            #print(file)
            files.append(file)
            files.sort()
        data = {'city': directories, 'files': files}
        dataList.append(data)
    #print(dataList)
    for lists in dataList:
        for key, value in lists.items():
            if key == 'city':
                print('City: ' + value)
            else:
                print(value)
    return render_template("index.html", cities=dataList)


@app.route('/<path:path>', methods=['GET'])
def get_csv(path):
    return send_file(path, mimetype='text/json', as_attachment=True)


@app.route('/json/<path:path>', methods=['GET'])
def get_json(path):
    df = pandas.read_csv(path, low_memory=False)
    data = df.to_json(orient="table")
    api = jsonify(data)
    return api
