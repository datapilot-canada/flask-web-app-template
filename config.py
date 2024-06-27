import os
import secrets

import logging
from dotenv import load_dotenv

# from redis import StrictRedis

# from azure.keyvault.secrets import SecretClient
# from azure.identity import DefaultAzureCredential

load_dotenv()
basedir     = os.path.abspath(os.path.dirname(__file__))
log_path    = os.path.join(basedir, 'app.log')
client_id   = os.environ["AZURE_CLIENT_ID"]

log_lvl = logging.getLevelName(os.environ.get("LOG_LEVEL"))

# Setup logging
logging.basicConfig(filename=log_path, level=log_lvl, format='%(asctime)s [[%(name)s]] %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


# Get the secrets names fot eh Key VaultSetup the Azure Speech Service Key and Region
# client_id                       = os.environ['AZURE_CLIENT_ID']


# # Setup access to the Key Vault.
# key_vault_name  = os.environ["KEY_VAULT_NAME"]
# key_vault_uri   = f"https://{key_vault_name}.vault.azure.net"
# credential      = DefaultAzureCredential(managed_identity_client_id=client_id)
# client          = SecretClient(vault_url=key_vault_uri, credential=credential)


# # Redis Cache Connection Details TODO: Move to Key Vault
# myHostname = os.environ["KV_REDIS_HOSTNAME_SECRET_NAME"]
# myPassword = os.environ["KV_REDIS_PASSWORD_SECRET_NAME"]


def export_env_variables():    
    os.environ['APP_BASE_DIR'] = basedir    
    # os.environ['REDIS_CACHE_PORT'] = '6380'
    # os.environ['REDIS_CACHE_HOSTNAME'] = myHostname
    # os.environ['REDIS_CACHE_PASSWORD'] = myPassword
    # os.environ['REDIS_CACHE_SSL'] = 'True'
   

export_env_variables()


class Config:
    SECRET_KEY                          = secrets.token_hex()
    SQLALCHEMY_TRACK_MODIFICATIONS      = False
    APP_BASE_DIR                        = basedir    
    # REDIS_CACHE_PORT                    = 6380
    # REDIS_CACHE_HOSTNAME                = myHostname
    # REDIS_CACHE_PASSWORD                = myPassword
    # REDIS_CACHE_SSL                     = True
    # Setup session management with Azure Redis Cache
    SESSION_TYPE                        = 'redis'
    # SESSION_REDIS                       = StrictRedis(host=myHostname, port=6380, password=myPassword, ssl=True)