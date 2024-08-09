from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = '1234567890'  

@app.route('/', methods=['GET', 'POST'])
def connect_to_vpn():
    if request.method == 'POST':
        server_address = request.form['server_address']
        username = request.form ['username']
        password = request.form ['password']

        if server_address and username and password:
            flash("Connected to VPN Server", "success")
        else:
            flash("Please fill in all the fields", "error")
        
        return redirect(url_for('connect_to_vpn'))

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
