from flask import Flask, jsonify
import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'hostname': socket.gethostname(),
        'time': datetime.datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        "message": "Details endpoint is working"
    }), 200

@app.route('/api/v1/health')
def health():
    return jsonify({
        'message': 'Health endpoint is working!',
        'status': 'healthy'
    }), 200


if __name__ == '__main__':
    # We need '0.0.0.0' to be accessible from outside the container
    app.run(debug=True, host='0.0.0.0')