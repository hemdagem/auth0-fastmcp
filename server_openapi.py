from fastmcp import FastMCP
from fastmcp.server.auth import OAuthProxy
from fastmcp.server.auth.providers.jwt import JWTVerifier
import os
import uvicorn
import httpx
from typing import Literal
from dotenv import load_dotenv
load_dotenv()

# --- Configuration ---
# You must change these to your actual values
UPSTREAM_CLIENT_ID = os.environ.get("AUTH0_CLIENT_ID", "")
UPSTREAM_CLIENT_SECRET = os.environ.get("AUTH0_CLIENT_SECRET", "")
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN", "")
SERVER_BASE_URL = os.environ.get("SERVER_BASE_URL", "")
OPEN_API_SPEC_URL = os.environ.get("OPENAPI_SPEC_URL", "")
OPEN_API_BASE_URL = os.environ.get("OPENAPI_BASE_URL", "")

# --- Authentication Setup ---
auth = OAuthProxy(
    # Auth0 Endpoints
    upstream_authorization_endpoint=f"https://{AUTH0_DOMAIN}/authorize",
    upstream_token_endpoint=f"https://{AUTH0_DOMAIN}/oauth/token",
    
    # Your Registered Credentials
    upstream_client_id=UPSTREAM_CLIENT_ID,
    upstream_client_secret=UPSTREAM_CLIENT_SECRET,

    # Auth0 requires 'audience' for token requests (OIDC/JWT)
    extra_authorize_params={
        "audience": f"https://{AUTH0_DOMAIN}/api/v2/"
    },

    # Token Validation (Server validates the JWT issued by Auth0)
    token_verifier=JWTVerifier(
        jwks_uri=f"https://{AUTH0_DOMAIN}/.well-known/jwks.json",
        issuer=f"https://{AUTH0_DOMAIN}/",
        audience=f"https://{AUTH0_DOMAIN}/api/v2/" # Audience for validation
    ),

    # This is the public base URL of YOUR FastMCP server
    base_url=SERVER_BASE_URL 
)

# --- MCP Server Definition ---
# mcp = FastMCP(name="Auth0 FastMCP Server", auth=auth)

client = httpx.AsyncClient(base_url=OPEN_API_BASE_URL)
openapi_spec = httpx.get(OPEN_API_SPEC_URL).json()
mcp = FastMCP.from_openapi(openapi_spec=openapi_spec, auth=auth, client=client)


# @mcp.tool
# def get_user_status(level: Literal["basic", "full"]) -> str:
#     """Gets the status of the authenticated user based on the requested access level."""
#     # In a real app, you would inspect the token/context here to get user info.
#     return f"Status requested at {level} level. Connection successful and authenticated."

if __name__ == "__main__":
    # Note: Use uvicorn to run a production-ready async server
    # Running locally on 127.0.0.1:8000 for development purposes
    cert_file = os.path.join(os.path.dirname(__file__), "cert.pem")
    key_file = os.path.join(os.path.dirname(__file__), "key.pem")
    app = mcp.http_app(transport="http", path="/mcp") 
    uvicorn.run(
        app, 
        host="0.0.0.0", 
        port=8000, 
        ssl_certfile=cert_file,
        ssl_keyfile=key_file)