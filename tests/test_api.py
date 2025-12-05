from fastapi.testclient import TestClient
from src.ascv_genai.api.main import app

client = TestClient(app)

def test_read_main():
    """
    Test the root endpoint.
    """
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the ASCV-GenAI API"}

def test_upload_files_placeholder():
    """
    Test the file upload endpoint.
    This is a basic test to ensure the endpoint exists and returns the correct status.
    """
    # Create dummy files to upload
    files = [
        ("files", ("test1.txt", b"this is a test file", "text/plain")),
        ("files", ("test2.txt", b"this is another test file", "text/plain")),
    ]
    
    response = client.post("/ingest/files", files=files)
    
    # In the placeholder, the task runs in the background, so we just check the immediate response.
    assert response.status_code == 200
    assert "Started processing 2 files" in response.json()["message"]

