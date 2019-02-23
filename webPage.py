from flask import Flask, render_template, url_for
app = Flask(__name__)

userDetails = [
    { "name":"Alishan Ahamad",
      "from":"Varanasi",
      "contact": 1234567890
        },
    { "name":"Abhilash Das",
      "from":"Pune",
      "contact": 9889863212
        },
    { "name":"Aditya Chobey",
      "from":"Pune",
      "contact": 9175110966
        }
    ]
print(userDetails)

@app.route("/")
def default():
    return "This is default page bro!!!"

@app.route("/home")
def home():
    return render_template('home.html', title="Home page", userDetails=userDetails)

@app.route("/about")
def hello():
    return render_template('index.html', title="About Us", userDetails=userDetails)

if __name__ == "__main__":
    app.run(debug=True)

