from prefect import flow
from task.consume_api import get_character_name, get_first_episode, summarize

@flow(name="Rick and Morty Flow with Retry")
def main(character_name: str = "Rick Sanchez"):
    character_data = get_character_name(character_name)
    episode_data = get_first_episode(character_data)
    summarize(character_data, episode_data)