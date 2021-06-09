from rich import print


def read_banner() -> str:
    with open('src/ui/banner.txt') as banner_file:
        file_content = banner_file.read()
        return file_content


def get_banner() -> str:
    return print(f"[magenta][b]{read_banner()} [/][/]")