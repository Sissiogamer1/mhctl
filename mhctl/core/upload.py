from pathlib import *
import httpx

def upload_pomf(file: str, provider: str):
    file_path = Path(file)
    from .settings import provider_info
    provider_info = provider_info(provider)
    print("OUTPUT")
    print(provider_info)
    try:
        if not file_path.exists:
            # REWRITE BETTER TEXT
            raise ValueError(f"{file} does not exist")
        file_size = file_path.stat().st_size
        if file_size > int(provider_info[2]):
            raise ValueError(f"{file} is too big")
        with open(file_path, "rb") as f:
            with httpx.Client(timeout=30.0) as client:
                files = {"files[]": (file_path.name, f)}
                response = client.post(provider_info[1], files=files)
                if response.status_code != 200:
                    raise RuntimeError(f"Upload failed: HTTP {response.status_code}")
                return response.json()
    except Exception as e:
        raise e