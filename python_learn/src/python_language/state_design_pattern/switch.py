from typing import Protocol

class LightState(Protocol):
    def switch(self, bulb) -> None:
        ...
        
class OnState:
    def switch(self, bulb) -> None:
        bulb.state = OffState()
        print('Light turned off')

class OffState:
    def switch(self, bulb) -> None:
        bulb.state = OnState()
        print('Light turned on')

class Bulb:
    def __init__(self) -> None:
        self.state:LightState|  = OnState()
        
    def switch(self) -> None:
        self.state.switch(self)
        

def main() -> None:
    bulb = Bulb()
    bulb.switch()
    bulb.switch()

if __name__ == "__main__":
    main()