from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
course = [
    {"id": 1, "name": "Lakshana"},
    {"id": 2, "name": "Madhu"},
    {"id": 3, "name": "Nikitha"},
    {"id": 4, "name": "Laisha"},
]
@app.route("/app/api/course/all",methods=['GET'])
def show():
    return jsonify(course)


@app.route("/update/", methods=['PUT'])
def update():
    id = request.form.get("id")
    print(id)
    name = request.form.get("name")
    print(name)
    for i in range(0, len(course)):
        temp = course[i]["id"]
        if int(temp) == int(id):
            course[i]["name"] = name
            return jsonify(course)


@app.route("/append/",methods=['POST'])
def append():
    print(request.content_length)
    id = request.form.get("id")
    name = request.form.get("name")
    print(id)
    print(name)
    d = {"id": int(id), "name": name}
    course.append(d)
    return jsonify(course)


@app.route("/remove/",methods=['DELETE'])
def remove():
    id = request.form.get("id")

    for i in range(0, len(course)):
        temp = course[i]["id"]
        if int(temp) == int(id):
            course.remove(course[i])
            return jsonify(course)
    return "ID NOT FOUND TO DELETE"


@app.route("/showit/",methods=['GET'])
def showit():
    id = request.args.get("id")

    for i in range(0, len(course)):
        temp = course[i]["id"]
        print(temp)
        if int(temp) == int(id):
            print("sucess")
            return course[i]
    return "not found"

if __name__ == "__main__":
    # app.run(host="0.0.0.0",debug=False)
    app.run(host="0.0.0.0", port=8086 ,debug=True)

