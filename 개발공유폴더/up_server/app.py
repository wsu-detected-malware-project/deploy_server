from flask import Flask, send_from_directory, abort
import os

app = Flask(__name__)

#배포 폴더 경로
DEPLOY_DIR = 'C:/Users/ljw01/Desktop/up_server'

@app.route('/')
def index():
    return '''
        <h2>ClickOnce 앱 설치</h2>
        <a href="/setup.application">설치하기</a>
    '''

@app.route('/<path:filename>')
def serve_file(filename):
    print(f"[요청 파일]: {filename}")

    # 경로 보정: /setup.application/ 로 시작하면 앞부분 잘라냄
    if filename.startswith("setup.application/"):
        filename = filename.replace("setup.application/", "", 1)

    # 디코딩된 경로 사용
    full_path = os.path.join(DEPLOY_DIR, filename)
    if not os.path.isfile(full_path):
        print(f"파일 없음: {full_path}")
        return abort(404)

    return send_from_directory(DEPLOY_DIR, filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=1234)
