import argparse
from api import get_inventory, add_item, get_item, edit_item, delete_item


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

    # get item by id
    getitem = subparser.add_parser("get-item", help="Get item by id.")
    getitem.add_argument("id", type=int, help="Id of queried item.")
    getitem.set_defaults(func=get_item)

    # edit item
    edititem = subparser.add_parser("edit", help="Edit inventory item")
    edititem.add_argument("id", type=int, help="Item id")
    edititem.add_argument("--name", "--n", type=str, help="Edit name")
    edititem.add_argument("--quantity", "--q", type=int, help="Edit quantity")
    edititem.add_argument("--brands", "--b", nargs="*", type=str, help="Edit brands")
    edititem.set_defaults(func=edit_item)

    # delte item
    deleteitem = subparser.add_parser("delete", help="Delete inventory item.")
    deleteitem.add_argument("id", type=int, help="Item id.")
    deleteitem.set_defaults(func=delete_item)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()
