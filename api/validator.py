import subprocess


def main():
    error_catch = 'Illegal character in path segment: "{" is not allowed'
    ignored_errors = [error_catch]
    cmd = ["html5validator", "--root", "api/templates"]
    result = subprocess.check_output(cmd).decode("utf-8")

    for line in result.splitlines():
        if not any(ignored in line for ignored in ignored_errors):
            print(line)
            raise SystemExit(1)
