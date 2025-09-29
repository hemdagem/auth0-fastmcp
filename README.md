# auth0-fastmcp

This repository helps you implement and test the Auth0 interactive login flow with a FastMCP MCP Server. It provides example FastMCP servers and configuration to enable secure authentication and API access using Auth0.
- `server.py`: Main API server
- `server_openapi.py`: OpenAPI documentation server

## Prerequisites
- [Python 3.13](https://www.python.org/downloads/)

### macOS SSL Certificate (Required)
If you are running this project on macOS, you must install the development SSL certificate before running the server. This is required for browsers and VS Code to trust the MCP server for secure connections.

Run:
```sh
./install-cert.sh
```

This step is only needed for macOS users. Other operating systems may require different certificate installation steps.

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

- The API server will start. Default port and host are defined in the script (usually `localhost:8000`).
- Check the script for custom port or host settings.

### Run `server_openapi.py`
```bash
python server_openapi.py
```

- This will start the OpenAPI documentation server.
- Access the OpenAPI docs at the URL printed in the terminal (usually `http://localhost:8000/docs`).


## Additional Notes

---
Feel free to contribute or open issues for bugs and feature requests.
