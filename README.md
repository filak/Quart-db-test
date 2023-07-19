# Quart with quart-sqlalchemy extension

https://github.com/pallets/quart/

https://github.com/joeblackwaslike/quart-sqlalchemy/

## Testing

- Create and activate VENV
- Install deps from requirements_test.txt
- Install latest Quart - https://github.com/pallets/quart/commit/206d93f74846fd697650bf85ef1de36c86716d48

       pip install https://github.com/pallets/quart/archive/refs/heads/main.zip

Run Flask app - OK:

    flask --app flask-app.py run

Run Quart app:

    py quart-app.py

=> Error

```
Traceback (most recent call last):
  File "D:\Decko\Quart-db-test\quart-app.py", line 17, in <module>
    with app.app_context():
AttributeError: __enter__
```

Run Quart app factory without SQLAlchemy - OK:

    py quart-srv.py

Run Quart app factory with SQLAlchemy:

    py quart-srv.py --db

=> Error

```
Traceback (most recent call last):
  File "D:\Decko\Quart-db-test\quart-srv.py", line 24, in <module>
    main()
  File "D:\Decko\Quart-db-test\quart-srv.py", line 20, in main
    app = create_app(use_db=args.db)
  File "D:\Decko\Quart-db-test\application\quart_app_factory.py", line 20, in create_app
    db.drop_all()
  File "D:\Decko\Quart-db-test\venv\lib\site-packages\quart_sqlalchemy\extension.py", line 764, in drop_all
    self._call_for_binds(bind_key, "drop_all")
  File "D:\Decko\Quart-db-test\venv\lib\site-packages\quart_sqlalchemy\extension.py", line 718, in _call_for_binds
    engine = self.engines[key]
  File "D:\Decko\Quart-db-test\venv\lib\site-packages\quart_sqlalchemy\extension.py", line 580, in engines
    app = current_app._get_current_object()
  File "D:\Decko\Quart-db-test\venv\lib\site-packages\werkzeug\local.py", line 508, in _get_current_object
    raise RuntimeError(unbound_message) from None
RuntimeError: Not within an app context
```

The latest version (v3.0.2) of quart-sqlalchemy does not wotk either:

```
Traceback (most recent call last):
  File "D:\Decko\Quart-db-test\quart-app.py", line 4, in <module>
    from quart_sqlalchemy import SQLAlchemy
  File "D:\Decko\Quart-db-test\venv\lib\site-packages\quart_sqlalchemy\__init__.py", line 3, in <module>
    from .bind import AsyncBind
  File "D:\Decko\Quart-db-test\venv\lib\site-packages\quart_sqlalchemy\bind.py", line 15, in <module>
    from . import signals
  File "D:\Decko\Quart-db-test\venv\lib\site-packages\quart_sqlalchemy\signals.py", line 6, in <module>
    from quart.signals import AsyncNamespace
ImportError: cannot import name 'AsyncNamespace' from 'quart.signals' (D:\Decko\Quart-db-test\venv\lib\site-packages\quart\signals.py)
```

## Currently installed libs

```
Package           Version
----------------- -------
aiofiles          23.1.0
aiosqlite         0.19.0
annotated-types   0.5.0
anyio             3.3.4
blinker           1.6.2
click             8.1.6
colorama          0.4.6
exceptiongroup    1.1.2
Flask             2.3.2
Flask-SQLAlchemy  3.0.5
greenlet          2.0.2
h11               0.14.0
h2                4.1.0
hpack             4.0.0
hypercorn         0.14.4
hyperframe        6.0.1
idna              3.4
itsdangerous      2.1.2
Jinja2            3.1.2
MarkupSafe        2.1.3
pip               23.2
priority          2.0.0
pydantic          2.0.3
pydantic_core     2.3.0
quart             0.18.3
quart-flask-patch 0.1.0
quart-sqlalchemy  3.0.2
setuptools        68.0.0
sniffio           1.3.0
SQLAlchemy        1.4.41
SQLAlchemy-Utils  0.41.1
sqlapagination    0.0.1
tenacity          8.2.2
tomli             2.0.1
typing_extensions 4.7.1
Werkzeug          2.3.6
wsproto           1.2.0
```

