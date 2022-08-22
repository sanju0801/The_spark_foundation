from flask import Flask, render_template, request
import marks as m

app = Flask(__name__,template_folder='template')

@app.route("/", methods = ['GET','POST'])
def marks():
    if request.method == "POST":
        hrs = request.form["hrs"]
        marks_pred = m.marks_prediction(hrs)
        mks = marks_pred
    return render_template("index.html",my_marks = mks)

if __name__ == '__main__':
    app.run(debug=True, port = 8000)