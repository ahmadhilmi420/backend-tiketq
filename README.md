# Ticket API Builder

> Build a simple REST API to manage tickets — including basic CRUD, validations.

<!-- If you have the project hosted somewhere, include the link here. -->

## Table of Contents

- [Technologies Used](#technologies-used)
- [Setup](#setup-and-run-locally)
- [API Endpoints](#api-endpoints)
- [Contact](#contact)
<!-- * [License](#license) -->

## Technologies Used

- flask : 15.4.5 version 3.1
- flask-sqlalchemy - version 3.1
- Python - version 3.11
- Use ORM with SQLite

## Setup and Run Locally

Clone the project

```bash
  git clone https://github.com/ahmadhilmi420/backend-tiketq.git
```

Go to the project directory

```bash
  cd backend-tiketq
```

Install dependencies

```bash
  uv init
  uv add flask
```

Start the server

```bash
  flask --app main run --reload --debug
```

## API Endpoints

The API will be accessible at: `http://127.0.0.1:5000`

### List all tickets

- **Endpoint:** `GET /tickets`

Example using PowerShell:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/tickets" -Method Get
```

```
Result:
eventName : DWP 2025
id        : 1
isUsed    : True
location  : Jakarta
time      : 2025-08-31T20:00:00Z

eventName : Java Jazz Festival
id        : 2
isUsed    : True
location  : Jakarta
time      : 2025-03-01T19:00:00Z
```

### View a Specific Ticket

- **Endpoint:** `GET /tickets/:id`

Example using PowerShell:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/tickets/1"  -Method Get
```

```
eventName : DWP 2025
id        : 1
isUsed    : True
location  : Jakarta
time      : 2025-08-31T20:00:00Z
```

### Create a New Ticket

- **Endpoint:** `POST /tickets`

Example using PowerShell:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/tickets" -Method Post -Body '{"id": 9, "eventName": "Festival Jogja", "location": "Yogyakarta", "time": "2025-12-13T19:30:00Z", "isUsed": true}' -ContentType "application/json"
```

```JSON
{
    "id": 9,
    "eventName": "Festival Jogja",
    "location": "Yogyakarta",
    "time": "2025-12-13T19:30:00Z",
    "isUsed": true
}
```

### Mark a Ticket as Used

- **Endpoint:** `PATCH /tickets/:id`

Example using PowerShell:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/tickets/1" -Method Patch -Body '{"isUsed": true}' -ContentType "application/json"
```

```JSON
{
    "isUsed": true
}
```

### Remove a Ticket

- **Endpoint:** `DELETE /tickets/:id`
  Example using PowerShell:

```powershell
Invoke-RestMethod -Uri "http://127.0.0.1:5000/tickets/1" -Method Delete
```

## Contact

Created by [@ahmadhilmi420](https://github.com/ahmadhilmi420) - feel free to contact me!
