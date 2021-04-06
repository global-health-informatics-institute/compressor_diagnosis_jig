import os
from flask import Flask, render_template, request

app = Flask(__name__, template_folder="views", static_folder="assets")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/compressors/select')
def select_compressor():
    path = os.getcwd()
    compresors= []
    # read the entries
    with os.scandir(path+"/lib/pressure_measures") as listOfEntries:
        for entry in listOfEntries:
            # print all entries that are files
            if entry.is_file():
                compresors.append(entry.name.replace(".json", ""))

    return render_template("compressors/select.html", options=compresors)


@app.route('/compressors/list')
def list_compressors():
    return render_template("compressors/list.html")


@app.route('/compressors/test', methods=["POST", "GET"])
def test_compressors():
    return render_template("compressors/test.html")


if __name__ == '__main__':
    app.run(host='127.0.0.1', port="30500", debug=True)
