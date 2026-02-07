def get_default_provider():
    from mhctl.core.settings import content
    return content["default"]

def is_provider_supported(provider: str):
    from mhctl.core.settings import content
    if provider not in content.keys():
        raise ValueError(f"{provider} is not supported by mhctl\nPlease try again with a different provider")
    return True

def get_xxh3(f: str):
    import xxhash
    return xxhash.xxh3_64_hexdigest(f.read())

def get_sha1(f: str):
    import hashlib
    return hashlib.sha1(f.read()).hexdigest()

def get_timestamp():
    from datetime import datetime
    return datetime.now()