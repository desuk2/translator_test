from flask import Flask, jsonify, Response

app = Flask(__name__)

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "running"}), 200

@app.route('/metrics', methods=['GET'])
def metrics():
    # Example of standard Prometheus metrics format
    metrics_data = (
        "# HELP python_app_requests_total Total number of requests\n"
        "# TYPE python_app_requests_total counter\n"
        "python_app_requests_total{endpoint=\"/status\"} 1\n"
    )
    return Response(metrics_data, mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)