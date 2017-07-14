# Contact Trace

Development challenge of an application, using an api rest to store browsing history of websites.

### Pre-requisites

* Python 3.5
* Sqlite or Postgres
* Make

Using Makefile to describe the possible tasks used in development.

### Setup

Clone the repository in a local folder.
```
$ git clone https://github.com/Zapelini/user_trace_py.git
$ cd user_trace_py
$ pip install -r requirements-dev.txt
```

### Running test

```bash
make test
```

### Running code convention

```bash
make code-convention
```

### Running app

```bash
make run_server
```

Access your browser at http://localhost:5000/admin.

### Running migrantions

```bash
make db_up
make db_migrate
```
