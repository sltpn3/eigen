# Galang Suara Backend

## Requirements.

Python >= 3.7

## Installation & Usage

### Install Requirements

```bash
pip3 install -r requirements.txt
```

### Run Main API

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

#### Run API Behind Reverse Proxy
```bash
uvicorn app.main:app --host 0.0.0.0 --port <port> --root-path /<proxy_path>
```

and open your browser at `http://localhost:<port>/docs/` to see the docs.


## Alembic
#### Upgrade DB to latest revision
```bash
alembic upgrade head
```
#### Autogenerate revision
```bash
alembic revision --autogenerate -m "<revision_message>"
```
#### Generate SQL script
```bash
alembic upgrade <revision_id> --sql
```

## Testing
### Run Tests
#### Run all tests in module tests.unit
```
python -m unittest discover testing.unit --verbose
```
#### Run single test file
```
python -m unittest <path>/<to>/<test_file>.py  --verbose
```
#### Run single test method
```
python -m unittest testing.unit.test_auth.TestAuthAsync.test_get_token --verbose
```

### Code Coverage
#### Run Code Coverage
```
coverage run -m unittest discover tests.unit
```

#### Generate Code Coverage
```
coverage report -m
```
or
```
coverage html -d /save/to/dir
```

## Additional Info
### Day Of Week Conversion
```
0 = monday
1 = tuesday
2 = wednesday
3 = thursday
4 = friday
5 = saturday
6 = sunday
```