from wikipediaapi import Wikipedia
import six
import os
from google.cloud import translate_v2 as translate
import environ
from google.oauth2 import service_account

env = environ.Env()
environ.Env.read_env()
gcp_json_credentials_dict = env.json("google_key")
credentials = service_account.Credentials.from_service_account_info(
    gcp_json_credentials_dict)
# credential_path = r"googlekey.json"
# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
translate_client = translate.Client(credentials=credentials)



def get_summary(title):
	intro = Wikipedia().page(title).summary
	
	# translate = Wikipedia(lang).page(title).summary
	return intro

def translate(text, lang):
	if isinstance(text, six.binary_type):
		text = text.decode("utf-8")
	result = translate_client.translate(text, target_language=lang)
	return result["translatedText"]

