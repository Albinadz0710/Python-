import pytest

# --- ТЕСТЫ ДЛЯ POST /api-v2/projects ---

def test_create_project_positive(api):
    """Позитивный: Создание проекта с валидным названием."""
    resp = api.create_project("Тестовый проект")
    assert resp.status_code == 201
    assert "id" in resp.json()

def test_create_project_negative(api):
    """Негативный: Создание проекта с пустым названием."""
    resp = api.create_project("")
    # Ожидаем ошибку 400 (Bad Request) из-за отсутствия обязательного поля
    assert resp.status_code in [400, 422]

# --- ТЕСТЫ ДЛЯ PUT /api-v2/projects/{id} ---

def test_update_project_positive(api):
    """Позитивный: Обновление названия существующего проекта."""
    create_resp = api.create_project("Проект для обновления")
    project_id = create_resp.json()["id"]
    
    resp = api.update_project(project_id, "Новое название")
    assert resp.status_code == 200

def test_update_project_negative(api):
    """Негативный: Обновление несуществующего проекта."""
    # Передаем заведомо неверный ID
    resp = api.update_project("invalid-id-123", "Новое название")
    assert resp.status_code in [400, 404]

# --- ТЕСТЫ ДЛЯ GET /api-v2/projects/{id} ---

def test_get_project_positive(api):
    """Позитивный: Получение информации о созданном проекте."""
    create_resp = api.create_project("Проект для чтения")
    project_id = create_resp.json()["id"]
    
    resp = api.get_project(project_id)
    assert resp.status_code == 200
    assert resp.json()["title"] == "Проект для чтения"

def test_get_project_negative(api):
    """Негативный: Получение проекта по несуществующему ID."""
    resp = api.get_project("invalid-id-123")
    assert resp.status_code in [400, 404]

    