import pytest
from unittest.mock import AsyncMock, patch
from datetime import date


@pytest.mark.asyncio
async def test_create_user_success(client):
    fake_user = {
        "id": 1,
        "name": "Rodrigo",
        "email": "drigosf2012@email.com",
        "role_id": 1,
        "created_at": date.today().isoformat(),
    }

    payload = {
        "name": "Rodrigo",
        "email": "drigosf2012@email.com",
        "role_id": 1
    }

    with patch(
        "app.api.v1.routes_users.UserService.create_user",
        new=AsyncMock(return_value=fake_user)
    ):
        response = await client.post(
            "/api/v1/users",
            json=payload
        )

    assert response.status_code == 201
    assert response.json()["email"] == payload["email"]
    assert "password" not in response.json()


@pytest.mark.asyncio
async def test_create_user_email_already_exists(client):
    payload = {
        "name": "Rodrigo",
        "email": "drigosf2012@email.com",
        "role_id": 1
    }

    with patch(
        "app.api.v1.routes_users.UserService.create_user",
        new=AsyncMock(side_effect=ValueError("Email já cadastrado"))
    ):
        response = await client.post(
            "/api/v1/users",
            json=payload
        )

    assert response.status_code == 400
    assert response.json()["detail"] == "Email já cadastrado"
