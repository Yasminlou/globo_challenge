from prefect import flow

@flow
def hello_flow():
    print("Hello from Prefect!")

hello_flow()
