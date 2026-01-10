def get_default_provider():
    from ..core.settings import content
    print(content["default"])
    return content["default"]

def is_provider_supported(provider: str):
    print("1")
    from ..core.settings import content
    if provider not in content.keys():
        print("a")
        raise ValueError(f"{provider} is not supported by mhctl\nPlease try again with a different provider")
    return True
