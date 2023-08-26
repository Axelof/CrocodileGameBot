
# CrocodileBot

[supported_platforms]: ## "VK | Telegram"
[supported_languages]: ## "Русский | English"
[what_is_alias]: ## "Словесный варинт игры \"крокодил\""
 
_[Кроссплатформенный][supported_platforms] бот для игры в "[алиас][what_is_alias]"_ с друзьями.

![logo](/assets/logo.png)



---

## Виртуальное окружение

Для запуска этого проекта необходимо добавить в файл .env следующие переменные окружения

`VK_BOT_TOKEN`

`TELEGRAM_BOT_TOKEN`

---

## Запуск

### _Все команды запускаются в корне проекта_

Чтобы установить докер (в случае если он не установлен)
```bash
  sh docker.sh
```

Чтобы запустить контейнер
```bash
  docker-compose up --build
```

---

## Особенности

- Python 3.11
- Dockerized
- [internalization][supported_languages]
- [Cross-platform][supported_platforms]

