import os
import json

# ================= 설정 =================
SERVER_URL = "http://localhost:7070"
FILES_DIR = "static/files"
MANIFEST_PATH = "static/update_manifest.json"
VERSION_FILE = "version.txt"
RELEASE_NOTES = "자동 생성된 업데이트"  # 필요하면 바꿔도 됨
# ======================================

def get_version():
    # 버전 번호를 version.txt 에서 읽거나 새로 생성
    if not os.path.exists(VERSION_FILE):
        with open(VERSION_FILE, "w") as f:
            f.write("1.0.0")
        return "1.0.0"

    with open(VERSION_FILE, "r") as f:
        return f.read().strip()

def auto_increment_version(version):
    major, minor, patch = map(int, version.split("."))
    patch += 1
    return f"{major}.{minor}.{patch}"

def update_version_file(new_version):
    with open(VERSION_FILE, "w") as f:
        f.write(new_version)

def build_manifest(version):
    files = []

    for root, _, filenames in os.walk(FILES_DIR):
        for filename in filenames:
            rel_path = os.path.relpath(os.path.join(root, filename), FILES_DIR).replace("\\", "/")
            files.append({
                "path": rel_path,
                "url": f"{SERVER_URL}/static/files/{rel_path}"
            })

    manifest = {
        "version": version,
        "release_notes": RELEASE_NOTES,
        "files": files
    }

    return manifest

def save_manifest(manifest):
    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    current_version = get_version()
    new_version = auto_increment_version(current_version)
    update_version_file(new_version)

    manifest = build_manifest(new_version)
    save_manifest(manifest)

    print(f" update_manifest.json 생성 완료: 버전 {new_version}")
