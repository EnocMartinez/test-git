#!/usr/bin/env python3
"""

author: Enoc Martínez
institution: Universitat Politècnica de Catalunya (UPC)
email: enoc.martinez@upc.edu
license: MIT
created: 27/2/23
"""

from argparse import ArgumentParser
import rich


if __name__ == "__main__":
    argparser = ArgumentParser()
    # argparser.add_argument("-v", "--verbose", action="store_true", help="Shows verbose output", default=False)
    # argparser.add_argument("positional", type=str, help="Positional argument", default="")
    # argparser.add_argument("-f", "--file", help="Another argument", type=str, required=False, default="")
    args = argparser.parse_args()
    rich.print("[green]Hello world!")
    animals = ["cat", "dog", "rabbit"]
    for animal in animals:
        rich.print(f"[cyan] animal: {animal}")


