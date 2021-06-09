from src.ui.clear import clear
from src.ui.banner import get_banner
from src.core.detect import connect

from argparse import ArgumentParser

def main() -> None:
    clear()
    get_banner()

    parser = ArgumentParser()
    parser.add_argument('-u', help='Website URl to run Magenta', required=True)
    args = parser.parse_args()

    connect(args)


if __name__ == "__main__":
    main()