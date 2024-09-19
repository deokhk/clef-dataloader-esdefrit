from clef_extractors import *

CLEF_BASE_DIR = "/home/deokhk/project/CLEF03/DocumentData/DataCollections/"
CLEF_LOWRES_DIR = ""

if not CLEF_BASE_DIR:
  raise FileNotFoundError(f"Download CLEF and set CLEF_BASE_DIR in {__file__}")

#
# CLEF paths
#
PATH_BASE_QUERIES = "/home/deokhk/project/CLEF03/Topics/"
PATH_BASE_DOCUMENTS = "/home/deokhk/project/CLEF03/DocumentData/DataCollections/"
PATH_BASE_EVAL = CLEF_BASE_DIR + "RelAssess/"


# Prepare italian CLEF data paths
it_lastampa = (PATH_BASE_DOCUMENTS + "Italian_data/la_stampa/", extract_italian_lastampa)
it_sda94 = (PATH_BASE_DOCUMENTS + "Italian_data/sda_italian/", extract_italian_sda9495)
it_sda95 = (PATH_BASE_DOCUMENTS + "Italian_data/agz95/", extract_italian_sda9495)
italian = {"2001": [it_lastampa, it_sda94],
           "2002": [it_lastampa, it_sda94],
           "2003": [it_lastampa, it_sda94, it_sda95]}

# Prepare german CLEF data paths
der_spiegel = (PATH_BASE_DOCUMENTS + "German_data/der_spiegel/", extract_german_derspiegel)
fr_rundschau = (PATH_BASE_DOCUMENTS + "German_data/fr_rundschau/", extract_german_frrundschau)
de_sda94 = (PATH_BASE_DOCUMENTS + "German_data/sda_german/", extract_german_sda9495)
de_sda95 = (PATH_BASE_DOCUMENTS + "German_data/sda95/", extract_german_sda9495)
german = {"2003": [der_spiegel, fr_rundschau, de_sda94, de_sda95]}


# Prepare Spanish CLEF data paths
es_efe94 = (PATH_BASE_DOCUMENTS + "Spanish_data/efe/", extract_spanish_efe9495)
es_efe95 = (PATH_BASE_DOCUMENTS + "Spanish_data/efe95/", extract_spanish_efe9495)
spanish = {"2003": [es_efe94,es_efe95]}

# Prepare French CLEF data paths
fr_sda94 = (PATH_BASE_DOCUMENTS + "French_data/sda_french/", extract_french_sda9495)
fr_sda95 = (PATH_BASE_DOCUMENTS + "French_data/ats95/", extract_french_sda9495)
fr_lemonde94 = (PATH_BASE_DOCUMENTS + "French_data/new_docno/", extract_french_lemonde)

french = {"2003": [fr_sda94, fr_sda95, fr_lemonde94]}


all_paths = {"it": italian, "de": german, "fr": french, "es": spanish}

# Utility function
languages = [("de", "german"), ("it", "italian"),
             ("fr", "french"), ("es", "spanish"),
             ("en", "english")]
short2pair = {elem[0]: elem for elem in languages}
long2pair = {elem[1]: elem for elem in languages}
def get_lang2pair(language):
  return long2pair[language] if len(language) != 2 else short2pair[language]
