from flask import Flask, render_template, jsonify, send_from_directory
import os

app = Flask(__name__)
DATA_FOLDER = os.path.join('static', 'data')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list_csvs')
def list_csvs():
    files = [f for f in os.listdir(DATA_FOLDER) if f.endswith('.csv')]
    return jsonify(files)

@app.route('/data/<path:filename>')
def serve_data(filename):
    return send_from_directory(DATA_FOLDER, filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Required for Render
    app.run(debug=False, host='0.0.0.0', port=port)  # Bind to 0.0.0.0 for external access
