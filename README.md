# crud-fastapi
just a repository for crud with fastapi

The central ideia is provide a url shortner with a basic register, basic url slug register and http redirect.

There are a lot of tests to do and anothers exceptions to deal, but... it works well 🥲

## How to run it

### 1 Visual Studio Code: Debug

You can use default setup of debug for fastapi press ```F5``` and *voilà* it is running.

```.vscode/launch.json```
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python Debugger: FastAPI",
            "type": "debugpy",
            "request": "launch",
            "module": "uvicorn",
            "args": [
                "main:app",
                "--reload"
            ],
            "jinja": true,
            "envFile": "${workspaceFolder}/.env",
            "console": "internalConsole"
        }
    ]
}
```


If wanna use pytest for any reason... inside ```.vscode``` folder you can create the ```settings.json``` file and put this fallow configuration.

```json
{
    "python.testing.pytestArgs": [
        "application/tests"
    ],
    "python.testing.unittestEnabled": false,
    "python.testing.pytestEnabled": true
}
```
```python.testing.pytestArgs```: path to your tests. 😊

Poetry and pyenv together is used for dependency manegment and virtual environment. The idea of poetry build own virtual environment generate a lot of garbage on my machine.

To install dependencies

```bash
(env) $ python -m pip install poetry
Collecting poetry
.
.
.
sts-2.32.3 requests-toolbelt-1.0.0 shellingham-1.5.4 tomlkit-0.12.5 trove-classifiers-2024.5.22 urllib3-2.2.2 virtualenv-20.26.3 xattr-1.1.0
(env) $ poetry install
Updating dependencies
Resolving dependencies... (63.2s)

Package operations: 41 installs, 0 updates, 0 removals

  - Installing mdurl (0.1.2)
  - Installing markdown-it-py (3.0.0)
  - Installing pygments (2.18.0): Pending...
  - Installing sniffio (1.3.1): Pending...
.
.
.
Writing lock file
...
(env) $ uvicorn "main:app" --reload --host localhost --port 8000 # I recomend use the debug
INFO:     Started server process [6314]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
```


### 2 Docker

well... in my machine docker do not works well, if you wanna try run with it... good luck!

[postgesapp](https://postgresapp.com/) works very well for me.

if right now you're thinking: "ah, but docker is important for this" or "this is important for that over there..."

dude... docker is problematic on my machine. I'm sorry for this.