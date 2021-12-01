import sys
import time
from PyANGBasic import *
from PyANGKernel import *
from PyANGConsole import *
import shlex




def vdf(context, section, funcVolume):
    """this function is the default function found in the ang file we were playing with
    over the weekend keepting it here for backup and reference"""
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
    """to load the model"""
    if console.open(filepath):
        #model = console.getModel()
        model = GKSystem.getSystem().getActiveModel()
        print("Open network")
    else:
        console.getLog().addError("Cannot load the network")
        print("Cannot load the network")
        return -1
    catalog = model.getCatalog()
    geomodel = model.getGeoModel()
    return model, catalog, geomodel

def addColumn(userClassType, arg_list):
    #userClassType.addColumn( "GKUserClass::value_of_time_python", "value_of_time_python", GKColumn.Double, GKColumn.eExternal ) 
    userClassType.addColumn( arg_list[0], arg_list[1], arg_list[2] ) 
    print ('external was built')
    #return userClassType

def save(console, model):
    console.save("C:\\Users\\sandhela\\source\\repos\\williamsProject1\\aimsun_playground\\input_files\\aimsun_files\\test2.ang")
    # Reset the Aimsun undo buffer
    model.getCommander().addCommand( None )
    print ("Network saved Successfully")

def userClass(model, console,  catalog, geomodel):
    sectionType = model.getType("GKSection")
    userClassType = model.getType("GKUserClass")
    print (sectionType)
    print (dir(sectionType))
    print (dir(userClassType))
    print (userClassType.getName())
    cols = userClassType.getColumns( GKType.eSearchOnlyThisType )
    #print (cols)
    for item in cols:
        print (item, item.getName(), item.getId(), item.getExternalName(), str(item.getColumnType()))
    #print (dir(item))

    #add a new column
    addColumn(userClassType, ["GKUserClass::value_of_time_python", "value_of_time_python", GKColumn.Double, GKColumn.eExternal])
    addColumn(userClassType, ["GKUserClass::value_of_time2_python", "value_of_time2_python", GKColumn.Double, GKColumn.eExternal])
    
    #save the model 
    save(console, model)
    

    # attributes  = uc.getColumns( GKType.eSearchOnlyThisType )
    # for item in attributes:
    #     print (item, item.getName())

    #system = GKSystem.getSystem()
    #g_object = model.getType("GKObject")
    #print (g_object, g_object.getName())
    #print (dir(g_object))
    #ans = model.getCatalog().getObjectsByType(model.getType("GKUserClass"))
    #print (ans)
    #print (dir(ans[1043]))
    #attributes  = sectionType.getColumns( GKType.eSearchOnlyThisType )



    #user_class = model.getType("GKUserClass")
    #print (dir(catalog))
    
    #valueoftime = user_class.value_of_time()
    #print (valueoftime)

    # user_class_object = catalog.getObjectsByTypeWithSubTypes(user_class) #getObjectsByType(user_class)
    # print (user_class_object)
    # for item in user_class_object:
    #      print (item, item.getName() ) #user_class_object[item].getName())
    # print(dir(item))

    #print (dir(user_class_object[item]))
    #vehicle = model.userClass.getVehicle()
    # context = model.getType("GKFunctionCostContext")
    # print (str(context))
    # dta = model.getType("DTAManager")
    # print (dta)
    # print (dir(dta))
    
    #GKUserClass

    #print (dir(system))
    
    #AKIGetSectionUserDefinedCost()
    #AKIVehGetNbVehTypes
    
    #context is a GKFunctionCostContext python object. 
    #manager is a DTAManager python object. 
    #section is a DTASection python object. 

  
    #userClass = model.getType( "GKUserClass")
    #print (userClass)
    #print (dir(catalog))
    #print (dir(userClass))
    #this is a list of all userClass objects but this doesn't access the attributes as 
    #cleanly as we would like
    #userClassCatalog = catalog.getUsedSubTypesFromType(userClass)
    #userClassDict = userClassCatalog[0]
    #print ('userclassdict ', userClassDict)
    #for item in userClassDict:
    #    print (item, userClassDict[item].getName())
    #print (dir(userClassDict[item]))

    #to access the attributes of this class this outputs a huge list of pyangkernel objects
    # attributes  = userClass.getColumns( GKType.eSearchOnlyThisType )
    # #print ('attribures ', attributes)
    # #we need to iterate over it no choice to find the attribute of interest 
    # for item in attributes:
    #     print (item, item.getName())
    #     if item.getExternalName() == "value_of_time":
    #         #print ('yes')
    #         # print (item)
    #         # print (dir(item))
    #         # print (item.getContents())
    #         # print (item.getName())
    #         #xxx = userClass.getDataValueDouble(item)
    #         #print (xxx)
    #         break

            
    #for x in attributes:
    #    print (x, str(x.getName()), str(x.getExternalName()) )
    #print (dir(x))
    #     if x.getExternalName() == "value_of_time":
    #         value_of_time = context.userClass.getDataValueDouble(x)
    #         break

    

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
    userClass(model, console, catalog, geomodel)

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
