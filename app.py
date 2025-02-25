from flask import Flask

app = Flask(__name__)

@app.route('/getcode')
def get_code():
    team = 'group5: นิ่งไว้'
    return team

@app.route('/pita/<int:a>/<int:b>/<int:c>')
def pita(a,b,c):
    return f'Yes' if (a*a+b*b) == (c*c) else f"No"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
