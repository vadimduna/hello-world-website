from datetime import datetime
from typing import List

import requests
from flask import Flask, render_template, request
from pydantic import BaseModel

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template("index.html")


@app.route("/submit", methods=["POST"])
def submit():
    input_name = request.form.get("name")
    input_age = request.form.get("age")
    return render_template("hello.html", name=input_name, age=input_age)


@app.route("/submit_sum", methods=["POST"])
def submit_sum():
    input_num_1 = request.form.get("num_1")
    input_num_2 = request.form.get("num_2")
    return render_template("sum.html", num1=input_num_1, num2=input_num_2)


@app.route("/atm", methods=["GET"])
def atm():
    return render_template("atm.html")


@app.route("/atm/money", methods=["POST"])
def withdraw_money():
    dollar_amount = int(request.form.get("dollarAmount", 0))
    # check if the dollar amount is within the valid range (1 to 50)
    if 1 <= dollar_amount <= 50:
        return render_template("money.html", dollars=dollar_amount)
    else:
        return render_template("errors.html", dollars=dollar_amount)


@app.route("/github_form")
def github_form():
    return render_template("github_form.html")


@app.route("/process_github_username", methods=["POST"])
def process_github_username():
    username = request.form.get("username")
    repo_objects = format_response(username)
    return render_template(
        "github_repo_info.html", name=username, repo_objects=repo_objects
    )


class Repository(BaseModel):
    repository_name: str
    time_created: datetime
    last_commit_message: str
    time_last_commit: datetime
    commits_num: int


def format_response(username: str) -> List[Repository]:
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        repo_objects = []
        for repo in repos:
            repo_name = repo["full_name"].split("/")[-1]
            time_created = datetime_return(repo, "created_at")

            time_last_commit = datetime_return(repo, "pushed_at")
            last_commit_message, commits_num = process_commits(repo)
            repo_objects.append(
                Repository(
                    repository_name=repo_name,
                    time_created=time_created,
                    time_last_commit=time_last_commit,
                    last_commit_message=last_commit_message,
                    commits_num=commits_num,
                )
            )
    return repo_objects


def process_commits(repo):
    commits_url = repo["commits_url"].split("{")[0]
    response_commits = requests.get(commits_url)
    last_commit_message = "No commits found"  # Default message
    commits_num = 0  # Default number of commits

    if response_commits.status_code == 200:
        commits = response_commits.json()
        if commits:  # Check if the commits list is not empty
            commits_num = len(commits)
            last_commit_message = commits[0]["commit"]["message"]

    return last_commit_message, commits_num


def datetime_return(repo, key):
    timestamp_str = repo[key]
    utc_time = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
    # Convert the timezone-aware datetime object to local time
    local_time = utc_time.astimezone(tz=None)
    # If tz=None, it uses the local timezone
    local_time_str = local_time.strftime("%Y-%m-%d %H:%M:%S")

    return local_time_str


@app.route("/query", methods=["GET"])
def get_query():
    query_value = request.args.get("q")
    return process_query(query_value)


def process_query(query_string):
    if query_string == "dinosaurs":
        return "Dinosaurs ruled the Earth 200 million years ago"
    elif query_string == "asteroids":
        return "Unknown"
    elif "name" in query_string:
        return "Vadim_Mariia_Kevin_"
    elif "largest" in query_string:
        return process_max_number(query_string)
    elif "smallest" in query_string:
        return process_min_number(query_string)
    elif "multiplied" in query_string:
        return process_multiply(query_string)
    elif "plus" in query_string:
        return process_plus(query_string)
    elif "minus" in query_string:
        return process_minus(query_string)
    elif "both a square and a cube" in query_string:
        return process_cube_square(query_string)
    elif "prime" in query_string:
        return process_prime(query_string)
    else:
        return "Invalid query"


def process_max_number(query_string):
    numbers = query_string.split(" ")[-3:]
    return str(max([int(number[:-1]) for number in numbers]))


def process_min_number(query_string):
    numbers = query_string.split(" ")[-3:]
    return str(min([int(number[:-1]) for number in numbers]))


def process_multiply(query_string):
    number_1 = int(query_string.split(" ")[-4])
    number_2 = int(query_string.split(" ")[-1][:-1])
    return str(number_1 * number_2)


def process_plus(query_string):
    number_1 = int(query_string.split(" ")[-3])
    number_2 = int(query_string.split(" ")[-1][:-1])
    return str(number_1 + number_2)


def process_minus(query_string):
    number_1 = int(query_string.split(" ")[-3])
    number_2 = int(query_string.split(" ")[-1][:-1])
    return str(number_1 - number_2)


def process_cube_square(query_string):
    numbers_string = query_string.split(":")
    numbers_list = numbers_string[-1].split(" ")
    numbers_list = [number[:-1] for number in numbers_list][1:]
    numbers_list = [int(numb) for numb in numbers_list]

    if 1 in numbers_list:
        return "1"

    answer_cubed = []

    for num in numbers_list:
        for i in range(num):
            if i * i * i == num:
                answer_cubed.append(num)

    answer_final = []
    for num in answer_cubed:
        for i in range(num):
            if i * i == num:
                answer_final.append(num)

    return str(answer_final)[1:-1]


def process_prime(query_string):
    numbers_string = query_string.split(":")
    numbers_list = numbers_string[-1].split(" ")
    numbers_list = [number[:-1] for number in numbers_list][1:]
    numbers_list = [int(numb) for numb in numbers_list]

    answer_list = []
    non_prime = []

    for num in numbers_list:
        for i in range(2, num):
            if num % i == 0:
                non_prime.append(num)
                break

    answer_list = [n for n in numbers_list if n not in non_prime and n != 1]

    return str(answer_list)[1:-1]
