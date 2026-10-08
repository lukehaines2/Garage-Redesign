from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
from pathlib import Path
root=Path(__file__).resolve().parent/'dist'
print('Local: http://127.0.0.1:8767',flush=True)
ThreadingHTTPServer(('127.0.0.1',8767),partial(SimpleHTTPRequestHandler,directory=str(root))).serve_forever()
