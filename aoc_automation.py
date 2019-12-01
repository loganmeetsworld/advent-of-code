import requests
import os
import bs4

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

    headers = {"cookie": f"session={os.environ['SESSION_COOKIE']}",}
    data = {
        "level": level,
        "answer": str(answer)
    }

    response = requests.post(f"https://adventofcode.com/{year}/day/{day}/answer", headers=headers, data=data)

    soup = bs4.BeautifulSoup(response.text, "html.parser")
    message = soup.article.text

    if "That's the right answer" in message:
        print("Correct!")
    elif "That's not the right answer" in message:
        print("Wrong answer!")
    elif "You gave an answer too recently" in message:
        print("Wait a bit, too recent a answer...")
