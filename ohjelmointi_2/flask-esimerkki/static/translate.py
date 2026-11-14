from flask import send_from_directory, request, Flask
import json

app = Flask(__name__)
@app.route('/translate/<sana>')
def sanakirja(sana):
    with open('sanakirja.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data[sana]

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000, use_reloader=True)
    
