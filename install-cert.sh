#!/bin/bash

# Generate self-signed certificate and key for localhost
openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes -subj "/CN=localhost"

CERT_PATH="./cert.pem"
CERT_NAME="localhost"

# Import certificate to login keychain and trust it
security add-trusted-cert -d -r trustRoot -k ~/Library/Keychains/login.keychain-db "$CERT_PATH"

echo "Certificate generated, imported, and trusted. You may need to restart VS Code."
