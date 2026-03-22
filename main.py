from flask import Flask,render_template,request,redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def home():
    conn = sqlite3.connect("cafes.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM cafe")
    cafes = cursor.fetchall()

    conn.close()
    return render_template("index.html",cafes=cafes)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        name =  request.form["name"]
        location = request.form["location"]

        conn = sqlite3.connect("cafes.db")
        cursor = conn.cursor()

        cursor.execute("INSERT INTO cafe(name,location) VALUES(?,?)",(name,location))
        conn.commit()
        conn.close()

        return redirect("/")

    return render_template("add.html")

@app.route("/delete/<int:id>")
def delete(id):
    conn = sqlite3.connect("cafes.db")
    cursor = conn.cursor()

    cursor.execute("DELETE FROM cafe WHERE id = ?",(id,))
    conn.commit()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)

