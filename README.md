# auth0-fastmcp

This repository helps you implement and test the Auth0 interactive login flow with a FastMCP MCP Server. It provides example FastMCP servers and configuration to enable secure authentication and API access using Auth0.
- `server.py`: Main API server
- `server_openapi.py`: OpenAPI documentation server

## Prerequisites
- [Python 3.13](https://www.python.org/downloads/)


## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/hemdagem/auth0-fastmcp.git
cd auth0-fastmcp
```

### 2. Create .env file
```bash
cp .env.example .env
```
Edit `.env` with your credentials and settings as needed.
Refer to `.env.example` and the code for required variables.

You can configure your Auth0 setup here: https://auth0.com/docs/get-started/auth0-overview/create-applications/regular-web-apps

### 3. Create and Activate Virtual Environment
```bash
python3 -m venv env
source env/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Servers

### Run `server.py`
```bash
python server.py
```

- The API server will start at `http://localhost:8000`

### Run `server_openapi.py`
```bash
python server_openapi.py
```

- This will start the OpenAPI documentation server.
- The API server will start at `http://localhost:8000`


## Additional Notes

---
Feel free to contribute or open issues for bugs and feature requests.
