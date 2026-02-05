import pytest
from unittest.mock import AsyncMock, patch


@pytest.mark.asyncio
async def test_get_role_success(client):
    fake_role = {
        "id": 1,
        "description": "ADMIN"
    }

    with patch(
        "app.api.v1.routes_roles.RoleService.get_role_by_id",
        new=AsyncMock(return_value=fake_role)
    ):
        response = await client.get("/api/v1/roles/1")

    assert response.status_code == 200
    assert response.json() == fake_role


@pytest.mark.asyncio
async def test_get_role_not_found(client):
    with patch(
        "app.api.v1.routes_roles.RoleService.get_role_by_id",
        new=AsyncMock(side_effect=ValueError("Role não encontrada"))
    ):
        response = await client.get("/api/v1/roles/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "Role não encontrada"
