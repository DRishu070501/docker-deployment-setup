import os
import subprocess
import sys
import secrets
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def run(cmd):
    print(f"> {cmd}")
    subprocess.check_call(cmd, shell=True)

def docker_installed():
    try:
        subprocess.check_output("docker --version", shell=True)
        subprocess.check_output("docker compose version", shell=True)
        return True
    except:
        return False

def install_docker():
    print("Docker not found. Installing...")
    if sys.platform.startswith("win"):
        run("powershell -ExecutionPolicy Bypass -File scripts/install_docker_windows.ps1")
        run("wsl --update")
    else:
        run("bash scripts/install_docker_linux.sh")

def generate_env():
    if os.path.exists(".env"):
        print(".env already exists")
        return

    env = open("env.template").read()
    pwd = secrets.token_urlsafe(16)
    root_pwd = secrets.token_urlsafe(20)

    env = env.replace("CHANGE_ME", pwd, 1)
    env = env.replace("CHANGE_ME", root_pwd, 1)

    with open(".env", "w") as f:
        f.write(env)

    print(".env generated")

def start_containers():
    run("docker compose build")
    run("docker compose up -d")

def main():
    os.chdir(BASE_DIR)

    if not docker_installed():
        install_docker()

    generate_env()
    start_containers()
    time.sleep(72)  # Wait for containers to start
    run('docker compose stop tomcat')
    run('docker cp server.properties myapp_tomcat:/usr/local/tomcat/webapps/ROOT/WEB-INF/classes/server.properties')
    run('docker compose start tomcat')

    print("\n✅ Installation complete!")
    print("🌍 Open: http://localhost:8080")

if __name__ == "__main__":
    main()
