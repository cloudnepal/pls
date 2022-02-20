#!/usr/bin/env python3
from pls.args import args
from pls.data.getters import node_specs
from pls.fs.list import read_input
from pls.table.table import write_output


def main() -> None:
    """
    Represents the starting point of the application. This function:

    - accepts no inputs: options are read from CLI arguments using ``argparse``
    - returns no outputs: output is written to ``STDOUT`` using ``rich``
    """

    node_map, node_list = read_input()

    if not node_list:
        return

    for node in node_list:
        node.match_specs(node_specs)
        if args.collapse:
            node.find_main(node_map)
    if args.collapse:
        for node in node_list:
            if node.is_sub:
                continue
            node.set_sub_pre_shapes()

    write_output(node_list)


if __name__ == "__main__":
    main()
