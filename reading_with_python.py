import uproot
import argparse
import matplotlib.pyplot as plt
import numpy as np

def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", help="Path to the file to be read")
    return parser.parse_args()

class EosNtupleReader:
    """
    Two main trees:
        - output: Event-by-event information
        - meta: Run-by-run information
    """
    def __init__(self, filename, **kwargs):
        self.tfile = uproot.open(filename)
        self.output_tree_name = "output"
        self.meta_tree_name = "meta"
        self.output_tree = self.tfile[self.output_tree_name]
        self.meta_tree = self.tfile[self.meta_tree_name]
        selected_branches = kwargs.get("selected_branches", self.output_tree.keys())
        self.output = self.output_tree.arrays(selected_branches, 
                                              library=kwargs.get("library", "np"))
        self.meta = self.meta_tree.arrays(library=kwargs.get("library", "np"))

def main():
    args = parse_arguments()
    eos_reader = EosNtupleReader(args.filename)
    plt.hist(eos_reader.output['nhits'], bins=100)
    plt.show()

if __name__ == "__main__":
    main()
