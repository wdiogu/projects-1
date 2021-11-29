import sys
import time
from PyANGBasic import *
from PyANGKernel import *
from PyANGConsole import *
import shlex


def vdf(context, section, funcVolume):

    volume = funcVolume.getVolume()
    capacity = section.getCapacity()
    addVolume = section.getAdditionalVolume()

    factor1 = ( 60.0 / section.getSpeed() ) * section.length3D() / 1000.0
    factor2 = 15.0 * 22.0 * 0.985 ** 3.6 * (  ( (volume + addVolume) / capacity ) - 0.985 ) + 1.0 + 4.8 * 0.985 ** 4.6
    factor3 = 1.0 + 4.8 * ( (volume + addVolume) / capacity ) ** 4.6
    time = factor1 * max( factor2 , factor3 )

    #print (dir(section))
    #print( dir(context.userClass) )
    model = context.userClass.getModel()
    sectionType = model.getType( "GKUserClass" )
    attributes  = sectionType.getColumns( GKType.eSearchOnlyThisType )
    for x in attributes:
        #print ( str(x.getName()), str(x.getExternalName()) )
        if x.getExternalName() == "value_of_time":
            value_of_time = context.userClass.getDataValueDouble(x)
            break
    print ('value of time ', value_of_time) 
    vehicle = context.userClass.getVehicle()
    #print ( "ID ", section.getId(), vehicle.getValueOfTimeMean() )
    #print ( context.userClass.getVehicle(), "***", context.userClass.getId(), "***" , context.userClass.getName() )
    if context.userClass.getName() == "Car":
        time = 1000.0
    return time

def loadModel(filepath, console):
    if console.open(filepath):
        model = console.getModel()
        print("Open network")
    else:
        console.getLog().addError("Cannot load the network")
        print("Cannot load the network")
        return -1
    catalog = model.getCatalog()
    geomodel = model.getGeoModel()
    return model, catalog, geomodel

def extract_feature():
    pass

# Main script to complete the full netowrk import
def main(argv):
    overallStartTime = time.perf_counter()
    if len(argv) < 3:
        print("Incorrect Number of Arguments")
        print("Arguments: -script script.py campnou_network.ang output_folder")
        return -1
    # Start a console
    console = ANGConsole()
    Network = sys.argv[1]
    networkFolder = sys.argv[2]
    print ('argv: ', argv)
    # generate a model of the input network
    model, catalog, geomodel = loadModel(Network, console)

    overallEndTime = time.perf_counter()
    print(f"Overall Runtime: {overallEndTime-overallStartTime}s")
    # Reset the Aimsun undo buffer
    #model.getCommander().addCommand(None)
    #return 0


if __name__ == "__main__":
    main(sys.argv)


    # Load a network
    # if console.open(argv[1]):
    #     global model
    #     model = console.getModel()
    #     print("load campnou network")
    #     print(model.areaName())
    # else:
    #     console.getLog().addError("Cannot load the network")
    #     print("cannot load network")
    #     return -1
