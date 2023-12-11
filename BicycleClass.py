import random

random.seed(10)

class BicycleClass:
    def __init__(self, vehID):
        self.vehID = vehID
        self.drivenOnRoads = {}
        self.roadsReceivedFromOthers = {}
        self.connectedWithCars = {}
        self.amountOfDoubleDataSent = 0
        self.roadsCollected = 0

    def addRoad(self, roadId):
        # prevent junctions being added to the list
        if roadId not in self.drivenOnRoads and roadId[0] != ':':
            self.drivenOnRoads[roadId] = [self.vehID]
                        
    def setDrivenOnRoads(self, roads):
        self.drivenOnRoads = roads

    def printRoads(self):
        print("veh " + self.vehID + " has driven on " + str(self.drivenOnRoads) + "\n     - and recieved from others " + str(self.roadsReceivedFromOthers))
        
    def getRecievedRoads(self):
        return self.roadsReceivedFromOthers
    
    def getRoads(self):
        return self.drivenOnRoads
    
    def getConnections(self):
        return self.connectedWithCars
    
    def printData(self):
        if self.roadsCollected != 0:
            print(str(self.amountOfDoubleDataSent) + " of " + str(self.roadsCollected) + " is " + str(round(self.amountOfDoubleDataSent*100/self.roadsCollected)) + "%.")
        
    def recieveDesseminationData(self, dataFromOtherVehicle, vehIDOther):
        # print("veh " + self.vehID + " has recieved " + str(dataFromOtherVehicle))
        if vehIDOther not in self.connectedWithCars:
            self.connectedWithCars[vehIDOther] = 1
        else:
            self.connectedWithCars[vehIDOther] += 1

        for recievedRoadSegment in dataFromOtherVehicle:
            self.roadsCollected +=1
            if recievedRoadSegment in self.roadsReceivedFromOthers:
                for senderName in dataFromOtherVehicle[recievedRoadSegment]:
                    if senderName not in self.roadsReceivedFromOthers[recievedRoadSegment]:
                        # If the road is already been recieved but is has been collected by another person origionally
                        self.roadsReceivedFromOthers[recievedRoadSegment].append(senderName)
                    else:
                        self.amountOfDoubleDataSent += 1
                        # If the road is already been collected from the same original source (eventhough it possibly came from another person)
                        # print("double data recieved")
            else:
                self.roadsReceivedFromOthers[recievedRoadSegment] = dataFromOtherVehicle[recievedRoadSegment]        
        self.roadsReceivedFromOthers = self.roadsReceivedFromOthers | dataFromOtherVehicle
    
    # this is what the bike will disseminate
    # algorithm for disseminating the data
    def getDisseminationData(self):
        # return self.drivenOnRoads # case 0 (no method)
        return self.scramble()
    
    def scramble(self):
        returnDict = {}
        for i in range(random.randint(1,5)):
            if random.randint(1,4) == 1:
                roadSegment = random.choice(list(self.drivenOnRoads))
                returnDict[roadSegment] = self.drivenOnRoads[str(roadSegment)]
            else:
                if len(self.roadsReceivedFromOthers) > 0:
                    roadSegment = random.choice(list(self.roadsReceivedFromOthers))
                    returnDict[roadSegment] = self.roadsReceivedFromOthers[str(roadSegment)]
        return returnDict 