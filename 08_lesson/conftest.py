import pytest
from project_api import ProjectApi

# ⚠️ ВАЖНО: Вставьте сюда ваш токен или используйте переменную окружения
API_TOKEN = "YKxPh5XU613kPwN8y0EjEtQdOGhzd2mcaLBUz2IQMIExq_bp1SNEpY0gAZJecnVK" 
BASE_URL = "https://ru.yougile.com/api-v2"

@pytest.fixture()
def api():
    return ProjectApi(url=BASE_URL, token=API_TOKEN)

