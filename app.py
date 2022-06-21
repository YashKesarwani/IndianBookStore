from flask import Flask,render_template,request

from models.database import Orders

app=Flask(__name__,static_url_path='',
    static_folder='static',
    template_folder='templates')
app.config['DEBUG']=True
app.config['ENV']='development'

dbObj=Orders()

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/SignIn",methods=["POST"])
def signIn():
    if request.method=="POST":
        userID=int(request.form["userID"])
        password=request.form["password"]
        signIn=dbObj.signIn(userID,password)
        if signIn==1:
            return render_template("orders.html",userID=userID)
        return {"result":"error"}
    else:
        return render_template("error.html")

@app.route("/track")
def track():
    orderID=int(request.args.get('orderID'))
    userID=int(request.args.get('userID'))
    
    trackStatus=dbObj.orderTracking(orderID)

    return render_template("tracking.html",trackingStatus=trackStatus)

@app.route("/test")
def test():
    # log=dbObj.login("x","y")
    # ins=dbObj.insertOrder(1,1) #1 is bookID
    records=dbObj.showAll()
    return {"records":records}

if __name__=="__main__":
    app.run(host="localhost",port=8000,debug=True)