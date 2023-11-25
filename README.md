
# Task Manager API

Task Manager API предоставляет RESTful интерфейс для управления задачами. Вы можете создавать, получать, обновлять и удалять задачи, а также фильтровать их по различным параметрам.

## Требования

- Python 3.7 и выше
- Django 3.2
- Django REST Framework 3.12

## Установка

1. Клонирование репозитория:

```bash
git clone https://github.com/m1ja/task_manager
cd task_manager
```

2.  Установка зависимостей:
```bash
pip install -r requirements.txt
```

3.  Применение миграций:
``` bash
python manage.py migrate
```

4.  Запуск сервера

```bash
python manage.py runserver
```

# API Reference

### Get all tasks
``` http
  GET /api/tasks
```

|Parameter|Type|description|
|:---|:----|:-----------|
|date|string|**Optional**. Filter tasks by date (Format: YYYY-MM-DD)|
|status|string|**Optional**. Filter tasks by status (e.g., 'completed', 'pending')|
|Authorization|string|**Required**.Your API token|

Response
```json
[
  {
    "id": 1,
    "title": "Task 1",
    "description": "Description of Task 1",
    "status": "false",
    "date": "2023-11-24"
  },
  {
    "id": 2,
    "title": "Task 2",
    "description": "Description of Task 2",
    "status": "true",
    "date": "2023-11-25"
  },
  ...
]
```

### Get a specific task
```http
  GET /api/tasks/${id}
```

|Parameter|Type|Description|
|:---|:----|:-----------|
|id|int|**Required**. Task ID|
|Authorization|'string'|**Required**. Your API token|

Response

```json
{
  "id": 1,
  "title": "Task 1",
  "description": "Description of Task 1",
  "status": "false",
  "date": "2023-11-24"
}
```

### Create a new task

```http
  POST /api/tasks
```

|Parameter|Type|Description|
|:---|:----|:-----------|
|title|string|**Required**. Task title|
|description|string|**Optional**. Task description|
|status|string|**Optional**. Task status|
|date|string|**Optional**. Task date (Format: YYYY-MM-DD)|
|Authorization|string|**Required**. Your API token|

Request
```json
{
  "title": "New Task",
  "description": "Description of the new task",
  "status": "true",
  "date": "2023-11-26"
}
```
Response
```json
{
  "id": 3,
  "title": "New Task",
  "description": "Description of the new task",
  "status": "true",
  "date": "2023-11-26"
}
```

### Update a task

```http
  PUT /api/tasks/${id}
```

|Parameter|Type|Description|
|:---|:----|:-----------|
|title|string|**Optional**. Task title|
|description|string|**Optional**. Task description|
|status|string|**Optional**. Task status|
|date|string|**Optional**. Task date (Format: YYYY-MM-DD)|
|Authorization|string|**Required**. Your API token|

Request
```json
{
  "title": "Updated Task",
  "description": "Updated description",
  "status": "true",
  "date": "2023-11-27"
}
```

Response
```json
{
  "id": 3,
  "title": "Updated Task",
  "description": "Updated description",
  "status": "true",
  "date": "2023-11-27"
}
```

### Delete a task
```http
  DELETE /api/tasks/${id}
```

|Parameter|Type|Description|
|:---|:----|:-----------|
|id|int|**Required**. Task ID|
|Authorization|string|**Required**. Your API token|

Response

```json
{
  "message": "Task deleted successfully"
}
```


## Documentation

[Documentation](https://5024-91-204-150-128.ngrok-free.app/api/docs/)

