import requests
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/joke', methods=['GET'])
def get_joke():
    headers = {'Accept': 'application/json'}
    response = requests.get('https://icanhazdadjoke.com/', headers=headers)
    if response.ok:
        try:
            joke = response.json()['joke']
            # Return the joke as a JSON response
            return jsonify({'joke': joke})
        except json.decoder.JSONDecodeError as e:
            print(f'Error parsing json: {e}')
            print(f'Response: {response.text}')
    else:
        print(f'Error {response.status_code}')

if __name__ == '__main__':
    app.run(debug=True)
