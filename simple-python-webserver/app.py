from flask import Flask, request, render_template_string

app = Flask(__name__)

base_template = '''
<html>
    <head><title>{{ title }}</title></head>
    <body>
        <nav>
            <a href="/">Main</a> |
            <a href="/status">Status</a> |
            <a href="/metrics">Metrics</a>
        </nav>
        {{ content|safe }}
    </body>
</html>
'''

@app.route('/status', methods=['GET'])
def status():
    content = '''
        <h1>Status</h1>
        <p>Status: running</p>
    '''
    return render_template_string(
        base_template,
        title="Status",
        content=content
    ), 200

@app.route('/metrics', methods=['GET'])
def metrics():
    metrics_data = (
        "# HELP python_app_requests_total Total number of requests\n"
        "# TYPE python_app_requests_total counter\n"
        "python_app_requests_total{endpoint=\"/status\"} 1\n"
    )
    content = f'''
        <h1>Metrics</h1>
        <pre>{metrics_data}</pre>
    '''
    return render_template_string(
        base_template,
        title="Metrics",
        content=content
    )

@app.route('/', methods=['GET', 'POST'])
def welcome():
    digital_value = ""
    if request.method == 'POST':
        digital_value = request.form.get('digital', '')
    content = '''
        <h1>Welcome!</h1>
        <form method="post">
            <label for="digital">Enter digital value:</label>
            <input type="text" id="digital" name="digital">
            <input type="submit" value="Submit">
        </form>
    '''
    if digital_value:
        content += f'<p>digital = {digital_value}</p>'
    return render_template_string(
        base_template,
        title="Welcome",
        content=content
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)