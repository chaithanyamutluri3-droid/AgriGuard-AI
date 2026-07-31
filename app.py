from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# -------------------- HOME --------------------

@app.route("/")
def home():
    return render_template("home.html")


# -------------------- LOGIN --------------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        # Temporary Login
        print("Email :", email)
        print("Password :", password)

        return redirect(url_for("dashboard"))

    return render_template("login.html")


# -------------------- REGISTER --------------------

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        fullname = request.form["fullname"]
        email = request.form["email"]
        mobile = request.form["mobile"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        if password != confirm_password:
            return "Passwords do not match!"

        # Temporary Registration
        print("Name :", fullname)
        print("Email :", email)
        print("Mobile :", mobile)

        return redirect(url_for("login"))

    return render_template("register.html")


# -------------------- DASHBOARD --------------------

@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


# -------------------- AI ASSISTANT --------------------

@app.route("/ai")
def ai():
    return render_template("ai_assistant.html")


# -------------------- CROP PREDICTION --------------------

@app.route("/crop")
def crop():
    return render_template("crop.html")


# -------------------- DISEASE DETECTION --------------------

@app.route("/disease")
def disease():
    return render_template("disease.html")


# -------------------- SOIL HEALTH --------------------

@app.route("/soil")
def soil():
    return render_template("soil.html")


# -------------------- WEATHER FORECAST --------------------

@app.route("/weather")
def weather():
    return render_template("weather.html")


# -------------------- FERTILIZER --------------------

@app.route("/fertilizer")
def fertilizer():
    return render_template("fertilizer.html")


# -------------------- SMART IRRIGATION --------------------

@app.route("/irrigation")
def irrigation():
    return render_template("irrigation.html")


# -------------------- IoT SENSOR --------------------

@app.route("/iot")
def iot():
    return render_template("iot.html")


# -------------------- REPORTS --------------------

@app.route("/report")
def report():
    return render_template("report.html")


# -------------------- HISTORY --------------------

@app.route("/history")
def history():
    return render_template("history.html")


# -------------------- PROFILE --------------------

@app.route("/profile")
def profile():
    return render_template("profile.html")


# -------------------- RUN APPLICATION --------------------

if __name__ == "__main__":
    app.run(debug=True)