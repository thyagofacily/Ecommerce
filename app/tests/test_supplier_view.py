from fastapi.testclient import TestClient

def test_create_supplier(client: TestClient , admin_auth_header):
        response = client.post('/suppliers/', headers=admin_auth_header,
                           json={'name': 'Supplier 1'})

        assert response.json()['name'] ==  "Supplier 1"