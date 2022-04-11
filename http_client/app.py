from flask import Flask, jsonify, render_template, request

app = Flask(__name__)
course = [
    {"id": 5, "name": "Lakshana"},
    {"id": 2, "name": "Rita"},
    {"id": 3, "name": "Gita"},
    {"id": 1, "name": "Mita"},
]
# @app.route('/')
# def index():
#     return render_template('index.html')


@app.route("/app/api/course/all")
def show():
    return jsonify(course)


@app.route("/hello/<id>")
def hello(id):
    print(type(course))
    for i in range(0, len(course)):
        temp = course[i]["id"]
        print(temp)
        if int(temp) == int(id):
            print("sucess")
            return course[i]
    return "request data not found"


@app.route("/append/<id>/<name>")
def helloooooo(id, name):
    id = int(id)
    name = str(name)
    for i in range(0, len(course)):
        temp = course[i]["id"]
        if int(temp) == int(id):
            course[i]["name"] = name
            return "name updated"
    a = {"id": id, "name": name}
    course.append(a)
    return "name added"


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


if __name__ == "__main__":
    app.run(debug=True)
