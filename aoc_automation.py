import requests
import os

automation_path = "/".join(os.path.abspath(__file__).split("/")[0:-1])
SESSION_COOKIE = open(f"{automation_path}/session.txt", "r").read().strip()

def problem_input(path):
    year = path.split("/")[-3]
    day = path.split("/")[-2].split("-")[1]
    headers = {"cookie": f"session={SESSION_COOKIE}",}
    response = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", headers=headers)

    if response.status_code == 404:
        print("This day is not available yet!")
        return
    elif response.status_code == 400:
        print("Bad creds!")
        return

    return response.text.strip()

def submit(path, level, answer):
    year = path.split("/")[-3]
    day = path.split("/")[-2].split("-")[1]

    print(f"For Day {day}, Part {level}, we are submitting answer: {answer}")

    headers = {"cookie": f"session={SESSION_COOKIE}",}
    data = {
        "level": level,
        "answer": str(answer)
    }

    response = requests.post(f"https://adventofcode.com/{year}/day/{day}/answer", headers=headers, data=data)

    print(response.text)
    return response
