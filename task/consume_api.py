import time
import httpx
from prefect import flow, task 
from prefect.tasks import task_input_hash
from datetime import timedelta
from random import randint


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

@task(retries=3, retry_delay_seconds=5)
def get_first_episode(character_info: dict) -> dict:
    try:
        episodes = character_info.get("episode", [])
        if not episodes:
            raise ValueError("No episodes found for the character.")

        # Simula timeout aleatório
        if randint(0, 1):
            print("Simulating timeout...")
            time.sleep(15)

        first_episode_url = episodes[0]
        response = httpx.get(first_episode_url, timeout=10)
        response.raise_for_status()
        episode = response.json()
        print(f"Episode found: {episode['name']}")
        return episode

    except Exception as e:
        print(f"[ERROR] Failed to fetch episode: {e}")
        raise  

