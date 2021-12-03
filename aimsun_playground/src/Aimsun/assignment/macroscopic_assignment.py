import sys
import time
from PyANGBasic import *
from PyANGKernel import *
from PyANGConsole import *
import shlex

# Main script to complete the full netowrk import
def main(argv):
    # overallStartTime = time.perf_counter()
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
    else:
        console.getLog().addError("Cannot load the network")
        print("cannot load network")
        return -1
    centroids = matrix.getCentroidConfiguration().getCentroidsInOrder()
    print(centroids)

    # Reset the Aimsun undo buffer
    # model.getCommander().addCommand(None)


def create_scenario():
    """
    - read traffic plan
    read public transport plan
    read path assignment plan
    read master control plan
    """
    pass


def create_experiment():
    """
    set assignment method
    store path assingment to save_path_assignment_info()
    """
    ...


def save_path_assignment_info():
    """
    set where to save file
    """
    ...


def save_network():
    ...


def _execute(output_file, model, console):
    """
    create scenario
    create experiment
    save path assignment
    run experiment
    """


if __name__ == "__main__":
    main(sys.argv)
