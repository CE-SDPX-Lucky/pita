from flask import Flask


app = Flask(__name__)

@app.route('/getcode')
def get_code():
    team = 'group5: นิ่งไว้'
    return team
    
@app.route('/cir_round/<x>')
def cir_round(x):
    x = float(x)
    if x < 0:
        return "0.00"
    return str(2*3.14*x)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
