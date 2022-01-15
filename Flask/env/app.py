from flask import Flask

app = Flask(__name__)

@app.route('/hello')
def hello():
    my_name = "John"
    return f'Hello, {my_name}!'

@app.route('/blog/<id>')
def blog(id):
    return f"This is blog entry #{id}"

@app.route('/message', methods=['POST'])
def post_message():
    return "OK"

@app.route('/message_ugly', methods=['GET'])
def message_form_ugly():
    text = """
        <html>
            <head></head>

            <body>
                <form action="" method="POST">
                    <label>First Name</label>
                    <input name="firstname"/>
                    <input type="submit"/>
                </form>
            </body>
        </html  >
    """
    return text

from flask import request, redirect

from flask import render_template

@app.route('/greeting', methods=['GET', 'POST'])
def message():
   if request.method == 'GET':
       print("We received GET")
       return render_template("greeting.html")
   elif request.method == 'POST':
       print("We received POST")
       print(request.form)
       return redirect("/")
    
@app.route("/warehouse")
def warehouse():
    items = ["screwdriver", "hammer", "saw"]
    errors = []
    return render_template("warehouse.html", items=items, errors=errors)
