import requests

class ProjectApi:
    def __init__(self, url, token) -> None:
        self.url = url
        self.token = token
        # Yougile требует токен в заголовках
        self.headers = {
            "Authorization": f"Bearer {self.token}",
            "Content-Type": "application/json"
        }

    # [POST] Создать проект
    def create_project(self, title):
        payload = {"title": title}
        resp = requests.post(f"{self.url}/projects", headers=self.headers, json=payload)
        return resp

    # [PUT] Обновить проект
    def update_project(self, project_id, new_title):
        payload = {"title": new_title}
        resp = requests.put(f"{self.url}/projects/{project_id}", headers=self.headers, json=payload)
        return resp

    # [GET] Получить проект по ID
    def get_project(self, project_id):
        resp = requests.get(f"{self.url}/projects/{project_id}", headers=self.headers)
        return resp

    