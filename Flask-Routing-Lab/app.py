from flask import Flask, redirect, request, render_template, url_for
from flask import session as login_session


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)
app.config["SECRET_KEY"] = "awekfhnqwepiou"
products = {"Health Potion":[500, "https://cdnb.artstation.com/p/assets/images/images/022/491/749/large/konstantin-andreev-.jpg?1575615525", "A Magic Potion that draws on the raw power of the Cosmere yada yada yada", "*the picture is for marketing purposes only, it may or may not come in a recycled coca cola can*"],
"A Magical Warrior":[2500, "https://img3.goodfon.com/wallpaper/nbig/f/22/voin-dospehi-mechi-magiya.jpg", "This Warrior Will defend you with his life and his ferocity is unmatched!", "*the picture is for marketing purposes only, the warrior happens to be 5 inches tall and will burst to tears at the first sign of violence*"],
"Magic Sword":[250, "https://cdna.artstation.com/p/assets/images/images/002/320/126/large/dmitriy-balashov-1.jpg?1460236757", "An sword forged by the dark eleves in the shadow lands", "*the picture is for marketing purposes only, it was really dark when they made it so they accidentally used rubber instead of steel sooo....*"],
"Magic Broom":[300, "https://clients.webtailorgroup.com/clientData/kmelite/media/products/120/120_d9a97397dc9ba4a3469761ee383f3e61.jpg", "IDK, it just cleans *really* well", "*yeah i got nonthin', for real a good product"]}

keys = list(products.keys())
# print(keys)

count = len(products)
# Your code should be below
@app.route("/")
def home():
    return render_template("home.html", products=products, len = count, key_list=keys)

@app.route("/product/<string:item>")
def product(item):
    return render_template("product.html", products=products, item=item)

@app.route("/cart", methods = ["get", "post"])
def cart():
    if request.method == "GET":
        return render_template("cart.html", products=products, cart_dict=login_session, len = len(login_session))
    else:
        item = request.form["item"]
        if item in login_session:
            login_session[item] += 1
        else:
            login_session[item] = 1
        return render_template("cart.html", products=products, cart_dict=login_session, len = len(login_session))


# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
