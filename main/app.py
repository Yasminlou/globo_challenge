import time
import httpx
from prefect import task 
from prefect.tasks import task_input_hash
from datetime import timedelta


BASE_API = "https://rickandmortyapi.com/api"


@task(cache_key_fn=task_input_hash, cache_expiration=timedelta(minutes=10))
def get_character_name(character_name: str) -> dict:
    url = f"{BASE_API}/character/?name={character_name}"
    response = httpx.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    # find first result
    character = data['results'][0]
    print(f"character found: {character['name']}")
    return character
