from wikipediaapi import Wikipedia
import six
import os
from google.cloud import translate_v2 as translate
credential_path = r"googlekey.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path
translate_client = translate.Client()



def get_summary(title):
	intro = Wikipedia().page(title).summary
	
	# translate = Wikipedia(lang).page(title).summary
	return intro

def translate(text, lang):
	if isinstance(text, six.binary_type):
		text = text.decode("utf-8")
	result = translate_client.translate(text, target_language=lang)
	return result["translatedText"]

