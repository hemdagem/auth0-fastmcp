from fastmcp import FastMCP
from fastmcp.server.auth import OAuthProxy
from fastmcp.server.auth.providers.jwt import JWTVerifier
import os
import uvicorn
from typing import Literal
from dotenv import load_dotenv
load_dotenv()

# --- Configuration ---
# You must change these to your actual values
AUTH0_CLIENT_ID = os.environ.get("AUTH0_CLIENT_ID", "")
AUTH0_CLIENT_SECRET = os.environ.get("AUTH0_CLIENT_SECRET", "")
AUTH0_DOMAIN = os.environ.get("AUTH0_DOMAIN", "")
SERVER_BASE_URL = os.environ.get("SERVER_BASE_URL", "")

# --- Authentication Setup ---
auth = OAuthProxy(
    # Auth0 Endpoints
    upstream_authorization_endpoint=f"https://{AUTH0_DOMAIN}/authorize",
    upstream_token_endpoint=f"https://{AUTH0_DOMAIN}/oauth/token",
    
    # Your Registered Credentials
    upstream_client_id=AUTH0_CLIENT_ID,
    upstream_client_secret=AUTH0_CLIENT_SECRET,

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
mcp = FastMCP(name="Auth0 FastMCP Server", auth=auth)

@mcp.tool
def get_user_status(level: Literal["basic", "full"]) -> str:
    """Gets the status of the authenticated user based on the requested access level."""
    # In a real app, you would inspect the token/context here to get user info.
    return f"Status requested at {level} level. Connection successful and authenticated."

if __name__ == "__main__":
    # Note: Use uvicorn to run a production-ready async server
    # Running locally on 127.0.0.1:8000 for development purposes
    app = mcp.http_app(transport="http", path="/mcp")
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=8000
    )