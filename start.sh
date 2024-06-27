# !/bin/bash
echo "=======================================Setting ENV Variables================================"
######### Environment Variables #########
export PYTHONPATH="${PYTHONPATH}:$(pwd)/app"
export KEY_VAULT_NAME="kv-datapilot-web-app-dev"
export AZURE_CLIENT_ID="b15b6789-be61-455e-bd26-b501ae45edce"
export LOG_LEVEL="DEBUG"
export FLASK_APP="app\__init__.py"

# When running locally, disable OAuthlib's HTTPs verification.
# ACTION ITEM for developers:
#     When running in production *do not* leave this option enabled. Set it to '0'.
export OAUTHLIB_INSECURE_TRANSPORT='0'

echo "=======================================Starting Gunicorn Server============================"
gunicorn -w 4 -b 0.0.0.0:8000 app:app
# gunicorn -k gevent -w 4 app:app