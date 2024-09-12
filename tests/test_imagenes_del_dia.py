import pytest
from src import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_imagenes_del_dia(client):
    response = client.get('/Imagenes_del_Dia')
    assert response.status_code == 200
    assert "Imágenes del Día" in response.data.decode('utf-8')  # Decodificar los bytes a str
