import argparse
from api import get_inventory, add_item


def main():
    parser = argparse.ArgumentParser(
        prog="Nala cli",
        description="Nala cli tool serving as the client for the nala backend api.",
    )

    subparser = parser.add_subparsers()

    # get inventory items
    getinventory = subparser.add_parser("get", help="Get inventory items")
    getinventory.set_defaults(func=lambda args: get_inventory())

    # add inventory item
    additem = subparser.add_parser("add", help="add new inventory item")
    additem.add_argument("--name", "--n", required=True, help="Product name", type=str)
    additem.add_argument(
        "--quantity", "--q", type=int, help="Quantity of product being added."
    )
    additem.add_argument("--brands", "--b", type=str, nargs="*")

    additem.set_defaults(func=add_item)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
