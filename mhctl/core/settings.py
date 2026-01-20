from pathlib import *
from yamlium import parse

clipath = Path(__file__).parent.parent
configpath = Path(clipath) / "config" / "providers.yml"

content = parse(configpath)
#yml = content.to_dict()

def list_providers():
    print("func called")
    for contentkey in content.keys():
        print(contentkey)

def provider_info(provider_name: str):
    for contentkey in content.keys():
        provider_str = str(contentkey)
        if provider_name in provider_str:
            print(f"Provider name: {provider_name}")
            print(f"Endpoint: {content["uguu.se"]["endpoint"]}")
            print(f"Max upload filesize: {content["uguu.se"]["max_size"]} bytes")
            return provider_name, content["uguu.se"]["endpoint"], content["uguu.se"]["endpoint"]