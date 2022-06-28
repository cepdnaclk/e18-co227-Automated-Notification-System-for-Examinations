import json
import configparser

def createJsonKeyFile():
    config = configparser.ConfigParser()# read the configuration file
    config.read('config.ini')# get all the connections


    KeysDict = {"type":config.get('Keys', "type"),
            "project_id":config.get('Keys', "project_id"),
            "private_key_id":config.get('Keys', "private_key_id"),
            "private_key":config.get('Keys', "private_key"),
            "client_email":config.get('Keys', "client_email"),
            "client_id":config.get('Keys', "client_id"),
            "auth_uri":config.get('Keys', "auth_uri"),
            "token_uri":config.get('Keys', "token_uri"),
            "auth_provider_x509_cert_url":config.get('Keys', "auth_provider_x509_cert_url"),
            "client_x509_cert_url":config.get('Keys', "client_x509_cert_url")}

    jsonString = json.dumps(KeysDict)
    jsonFile = open("keys.json", "w")
    jsonFile.write(jsonString)
    jsonFile.close()