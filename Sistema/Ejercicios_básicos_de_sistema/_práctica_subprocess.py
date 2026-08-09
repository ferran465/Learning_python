import subprocess

result = subprocess.run(["shutdown", "/r", "/t", "1"]) # la lista [] sirve para decirle a subprocces donde empieza y donde acaba el comando.

