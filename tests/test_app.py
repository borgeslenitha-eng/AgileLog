import sys
import os
# adiciona a pasta src ao path para que possamos importar src.app
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SRC = os.path.join(ROOT, "src")
if SRC not in sys.path:
    sys.path.insert(0, SRC)

from app import app  # agora importa app.py direto da pasta src

def test_index_route():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert b"AgileLog" in response.data