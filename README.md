# ⚡ Rick and Morty Flow

This project orcherstrate a flow to consume data from the [Rick and Morty API](https://rickandmortyapi.com/api) using the package [Prefect](https://docs.prefect.io/).

## 💡 What does the project do?

- Search for information about a character (e.g. Rick Sanchez)
- Accesses the first episode where he appears
- Simulates random timeout error in the episode task
- Uses **automatic retries** with Prefect
- Displays a final summary with the combined data

## 🛠️ Technologies used

- [Python 3.10+](https://www.python.org/)
- [Prefect 2.x](https://docs.prefect.io/)
- [httpx](https://www.python-httpx.org/)
- Rick and Morty API

---

## 🚀 How to run

### 1. Clone the repository
```bash
git clone https://github.com/Yasminlou/globo_challenge.git
cd globo_challenge
```
### 2. Create and activate the virtual environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install -r requirements.txt
```
### 4. Execute the flow
```bash
python app.py
```
## 📁 Preject Estrut
```bash
├── flows/
│   └── main.py # call flow
├── task/
│   └── consume_api.py # consuming the api
├── app.py # main flow call
├── requirements.txt # Project dependencies
└── README.md # Project documentation
