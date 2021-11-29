import sys
import time
from PyANGBasic import *
from PyANGKernel import *
from PyANGConsole import *
import shlex

# Main script to complete the full netowrk import
def main(argv):
    overallStartTime = time.perf_counter()
    if len(argv) < 3:
        print("Incorrect Number of Arguments")
        print("Arguments: -script script.py campnou_network.ang output_folder")
        return -1
    # Start a console
    console = ANGConsole()
    # Load a network
    if console.open(argv[1]):
        global model
        model = console.getModel()
        print("load campnou network")
        print(dir(model))
    else:
        console.getLog().addError("Cannot load the network")
        print("cannot load network")
        return -1

    overallEndTime = time.perf_counter()
    print(f"Overall Runtime: {overallEndTime-overallStartTime}s")
    # Reset the Aimsun undo buffer
    model.getCommander().addCommand(None)
    return 0


if __name__ == "__main__":
    main(sys.argv)
