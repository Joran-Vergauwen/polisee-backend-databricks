try: 
    from azure.identity import DefaultAzureCredential
    from azure.keyvault.secrets import SecretClient
except Exception as ex:
    logging.error(f"An error occurred in the keyvault file: {ex}")
    logging.error(f"Error when importing packages in keyvault")

def get_secret(kv_url: str, secret_name: str) -> str:
    """
    Given a name of the secret, returns the value
    KEYVAULT_URL environmentalparameter: the url of the keyvault, located in the overview of the keyvault in the portal (eg. https://KEYVAULT_NAME.vault.azure.net/)

    :param secret_name: The name of the secret we want to retrieve a value for
    :return: Value of the secret as a string, raises exception if secret doesn't exist
    """
    credential = DefaultAzureCredential()

    secret_client = SecretClient(kv_url, credential)
    secret = secret_client.get_secret(secret_name)
    return secret.value