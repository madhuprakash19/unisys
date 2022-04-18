from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
course = [
    {"id": 1, "name": "Lakshana"},
    {"id": 2, "name": "Madhu"},
    {"id": 3, "name": "Nikitha"},
    {"id": 4, "name": "Laisha"},
]


@app.route("/app/api/course/all")
def show():
    return jsonify(course)


@app.route("/update/")
def update():
    id = request.args.get("id")
    name = request.args.get("name")
    for i in range(0, len(course)):
        temp = course[i]["id"]
        if int(temp) == int(id):
            course[i]["name"] = name
            return jsonify(course)


@app.route("/append/")
def append():
    id = request.args.get("id")
    name = request.args.get("name")
    d = {"id": int(id), "name": name}
    course.append(d)
    return jsonify(course)


@app.route("/showit/")
def showit():
    id = request.args.get("id")

    for i in range(0, len(course)):
        temp = course[i]["id"]
        print(temp)
        if int(temp) == int(id):
            print("sucess")
            return course[i]
    return "not found"

@app.route('/post', methods=['POST'])
def result():
    print("HELLo")
    print(request.data)  # raw data
    print(request.json)  # json (if content-type of application/json is sent with the request)
    print(request.get_json(force=True))  # json (if content-type of application/json is not sent)


if __name__ == "__main__":
     app.run(ssl_context=("cert.pem", "key.pem"),debug=True)
