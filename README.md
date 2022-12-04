# Описание
Проект для сбора статистики трейсбеков по проектам для возможности выявления часто встречающихся ошибок и их дальнейшей оптимизации.

# Установка
```bash
git clone https://github.com/alexhook/traceback_stats.git && cd traceback_stats
```
В папке envs необходимо убрать префикс ".example" из их названия и заполнить файлы с переменными (по необходимости):
```bash
cd envs && mv pg.env.example pg.env && mv web.env.example web.env && cd ..
```

```bash
docker-compose up -d
```
Проведение миграций, сбор статических файлов и создание суперпользователя:
```bash
docker exec -it stats_web sh -c "make migrate && make collectstatic && make createsuperuser"
```
Проект будет доступен по адресу http://0.0.0.0:8080/admin
