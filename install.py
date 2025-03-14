import subprocess

def install_dependencies():
    packages = ["fastapi", "nest-asyncio", "pyngrok", "uvicorn", "vllm"]
    for package in packages:
        subprocess.run(["pip", "install", package], check=True)

if __name__ == "__main__":
    install_dependencies()