from sys import stdout
from re import sub
from datetime import datetime

LOG_PATH: str | None = None
WITH_TIMESTAMP: bool = False
SHOW_ON_TERMINAL: bool = True


def set_variables(
    log_path: str | None = LOG_PATH,
    reset_file: bool = False,
    with_timestamp: bool = WITH_TIMESTAMP,
    show_on_terminal: bool = SHOW_ON_TERMINAL,
):
    global LOG_PATH, WITH_TIMESTAMP, SHOW_ON_TERMINAL
    LOG_PATH = log_path
    WITH_TIMESTAMP = with_timestamp
    SHOW_ON_TERMINAL = show_on_terminal

    if reset_file and log_path:
        open(log_path, "w")


def _strip_ansi(text: str) -> str:
    return sub(r"\x1b\[[0-9;]*m", "", text)


def output_print(
    *args,
    sep=" ",
    end="\n",
):
    text = sep.join(str(arg) for arg in args) + end

    if SHOW_ON_TERMINAL:
        stdout.write(text)
        stdout.flush()

    if LOG_PATH:
        text_to_save = _strip_ansi(text)
        if WITH_TIMESTAMP:
            timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S] ")
            text_to_save = timestamp + text_to_save
        with open(LOG_PATH, "a", encoding="utf-8") as f:
            f.write(text_to_save)
