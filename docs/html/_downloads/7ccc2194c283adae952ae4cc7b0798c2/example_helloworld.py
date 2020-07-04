"""
Hello World
==============================
"""

from qparse import qparse


def parse():
    return qparse(
        descr="My first experiment",
        flags=[
            ("fig1", "Plot figure 1"),
            ("fig2", "Plot figure 2"),
            ("show", "Show plots during execution"),
            ("save", "Save plots during execution"),
        ],
    )


def make_fig_1(show, save):
    print("Making figure 1...")


def make_fig_2(show, save):
    print("Making figure 2...")


if __name__ == "__main__":
    args = parse()

    if args.fig1:
        make_fig_1(args.show, args.save)
    if args.fig2:
        make_fig_2(args.show, args.save)
