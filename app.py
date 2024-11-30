from flask import Flask, render_template, Response, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    """Homepage to display the live feed."""
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)