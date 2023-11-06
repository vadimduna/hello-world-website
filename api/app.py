from datetime import datetime
from typing import List

import requests
from flask import Flask, render_template, request
from pydantic import BaseModel

from utils_request import process_query

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
        "github_repo_info.html", name=username, my_repo_objects=repo_objects
    )


class Repository(BaseModel):
    repository_name: str
    time: datetime


def format_response(username: str) -> List[Repository]:
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repos = response.json()
        repo_objects = []
        for repo in repos:
            repo_name = repo["full_name"].split("/")[-1]
            created_time = datetime_return(repo)
            repo_objects.append(
                Repository(repository_name=repo_name, time=created_time)
            )

    return repo_objects


def datetime_return(repo):
    timestamp_str = repo["created_at"]
    timestamp_str = timestamp_str.replace(
        "Z", "+00:00"
    )  # Replace 'Z' with '+00:00' to specify UTC offset

    return datetime.fromisoformat(timestamp_str)


@app.route("/query", methods=["GET"])
def get_query():
    query_value = request.args.get("q")
    return process_query(query_value)
