# Task manager on FastAPI 
База данных: PostgreSQL
ORM: SQLAlchemy
Валидаторы данных (схемы): Pydantic

Функциональность:
1. POST /tasks/add добавляет задачу в базу данных
{
"task_uuid": "UUID",
"description": "тестовая задача",
"params": {
"param_1": "1",
"param_2": 1
}
}
2. GET /tasks - получает все существующие задачи
3. PUT /tasks/<task_uuid> - обновляет задачу по uuid
