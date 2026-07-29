# Sprint_5 — автотесты Stellar Burgers

Учебный проект с UI-автотестами сервиса
[Stellar Burgers](https://stellarburgers.education-services.ru/).
Тесты написаны на Python с использованием Selenium и pytest.

## Покрытие

- регистрация пользователя;
- вход в аккаунт разными способами;
- переходы в личный кабинет и конструктор;
- выход из аккаунта;
- переключение разделов конструктора.

## Установка

```bash
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## Запуск

```bash
pytest
```

Для запуска нужен установленный Google Chrome.

