from pathlib import *
import httpx

def upload_uguu(file: str, provider: str):
    file_path = Path(file)
    from .settings import provider_info
    provider_info = provider_info(provider)
    try:
        if not file_path.exists:
            # REWRITE BETTER TEXT
            raise ValueError(f"{file} does not exist")
        file_size = file_path.stat().st_size
        if file_size > int(str(provider_info[2])):
            raise ValueError(f"{file} is too big")
        with open(file_path, "rb") as f:
            from ..runtime.internal import get_xxh3
            xxh3_hash = get_xxh3(f)
            with httpx.Client(timeout=30.0) as client:
                files = {"files[]": (file_path.name, f)}
                response = client.post(str(provider_info[1]), files=files)
                temp_response = response.json()
                if response.status_code != 200: # VEDI SE ANZICHE' USARE ERROR CODE PUOI USARE "SUCCESS" DALL'ENDPOINT
                    raise RuntimeError(f"Upload failed: HTTP {response.status_code}")
                if xxh3_hash != temp_response["files"][0]["hash"]:
                    # MODIFICA QUESTO E MIGLIORA IL MESSAGGIO DI ERRORE !
                    raise RuntimeError(f"Errore dell'hash")
                # Caricamento nel database sql
                from .save import save_uguu
                save_uguu(
                    file_path.name,
                    temp_response["files"][0]["url"],
                    provider,
                    temp_response["files"][0]["size"]
                )
                return response.json()
    except Exception as e:
        raise e
    
def upload_pomf(file: str, provider: str):
    file_path = Path(file)
    from .settings import provider_info
    provider_info = provider_info(provider)
    try:
        if not file_path.exists:
            # REWRITE BETTER TEXT
            raise ValueError(f"{file} does not exist")
        file_size = file_path.stat().st_size
        if file_size > int(str(provider_info[2])):
            raise ValueError(f"{file} is too big")
        with open(file_path, "rb") as f:
            from ..runtime.internal import get_sha1
            sha1_hash = get_sha1(f)
            with httpx.Client(timeout=30.0) as client:
                files = {"files[]": (file_path.name, f)}
                response = client.post(str(provider_info[1]), files=files)
                temp_response = response.json()
                if response.status_code != 200 or temp_response["success"] != True: # VEDI SE ANZICHE' USARE ERROR CODE PUOI USARE "SUCCESS" DALL'ENDPOINT
                    raise RuntimeError(f"Upload failed: HTTP {response.status_code}")
                if sha1_hash != temp_response["files"][0]["hash"]:
                    # MODIFICA QUESTO E MIGLIORA IL MESSAGGIO DI ERRORE !
                    raise RuntimeError(f"Errore dell'hash")
                # Caricamento nel database sql
                from .save import save_uguu
                save_uguu(
                    file_path.name,
                    temp_response["files"][0]["url"],
                    provider,
                    temp_response["files"][0]["size"]
                )
                return response.json()
    except Exception as e:
        raise e