from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/alert', methods=['POST'])
def send_alert():
    return jsonify({"message": "Alert sent successfully!"})

@app.route('/api/provider/<provider_id>/data', methods=['GET'])
def share_data_with_provider(provider_id):
    return jsonify({"provider_id": provider_id, "data_shared": True})

if __name__ == '__main__':
    app.run(debug=True)
