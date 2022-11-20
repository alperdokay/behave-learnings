
class Door():

    # Constructor of a door, it is closed by default
    def __init__(self, status="Close"):
        self.status = status
    
    def open(self):
        print("Opening the door..")
        self.status = "Open"
        print("The door is now open")
    
    def close(self):
        print("Closing the door..")
        self.status = "Close"
        print("The door is now closed")

    def break_door(self):
        print("There is a thief around!")
        self.status = "Alarm"
        exit()
