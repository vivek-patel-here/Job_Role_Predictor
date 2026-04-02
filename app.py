from flask import Flask
app = Flask(__name__)


# Index Route
@app.route("/",methods=['GET','POST'])
def index():
    print("Server is running on port 5000.")
    return "Server is running healthy."

# main EndPoint
@app.route("/resume/predict",methods=["POST"])
def predict():
    print("/resume/predict. route hit")
    # here code for prediction and 
    return {
        "ATS score":"8.5",
        "skills" : ["HTML","CSS","JS","python","SQL","MERN stack","docker","kubernetes","redux & redux toolKit" ],
        "Education":"Undergrad B.tech from IIT delhi",
        "role" :"Software developer intern"
    }

