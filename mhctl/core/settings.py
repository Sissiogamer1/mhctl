from pathlib import *
from yamlium import parse

clipath = Path(__file__).parent.parent
configpath = Path(clipath) / "config" / "providers.yml"

content = parse(configpath)
yml = content.to_dict()

def list_providers():
    print("func called")
    for contentkey in content.keys():
        print(contentkey)

def provider_info(name: str):
    for key, value, obj in content.walk_keys():
        print("Key:")
        print(key)
        print("Value:")
        print(value)
        print("Obj:")
        print(obj)
        print("test")
        print(str(key))

def provider_info(provider_name: str):
    for contentkey in content.keys():
        provider_str = str(contentkey)
        if provider_name in provider_str:
            test = content[contentkey]
            o_endpoint = str(test["endpoint"])
            o_maxsize = str(test["max_size"])
            print(f"Provider name: {provider_name}")
            print(f"Endpoint: {o_endpoint}")
            print(f"Max upload filesize: {o_maxsize} bytes")