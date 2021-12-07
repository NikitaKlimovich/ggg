import flask
import json
import ibm_db_dbi as db

app = flask.Flask(__name__)

def get_connection():
    conn = db.connect('DATABASE=IBA_EDU;'
                     'HOSTNAME=3d-edu-db.icdc.io;'  
                     'PORT=8163;'
                     'PROTOCOL=TCPIP;'
                     'UID=stud07;'
                     'PWD=12345;', '', '')
    cur = conn.cursor()
    return cur

@app.route('/', methods=['GET'])
def load_to_json():
    query=("SELECT * FROM EXCHANGE_RATES")
    cur=get_connection()
    cur.execute(query)
    values = []
    for (id, er_date, rate , currency) in cur.fetchall():
        values.append({"id": id, "ER_DATE": er_date, "RATE": rate, "CURRENCY": currency})
    return flask.jsonify(values)
if __name__ == "__main__":
    app.run(debug='True')
