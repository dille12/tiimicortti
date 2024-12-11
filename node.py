import functions
import inspect
import pygame
import random
import time
#from pygame.math import Vector2 as v2
import traceback


class InputNode:
    def __init__(self, parent, inputName, typeC, isOutput = False):
        self.h = parent.height - 30
        parent.height += 30
        self.parent = parent
        self.input = inputName
        self.isOutput = isOutput
        self.game = parent.game
        self.selfInput = False

        self.outputIndex = 0

        print("TYPE:", typeC)

        if str(typeC) == "<class 'int'>" or str(typeC) == "<class 'float'>" or str(typeC) == "int":
            self.typeC = "Number"
        elif str(typeC) == "<class 'bool'>":
            self.typeC = "Boolean"

        else:
            self.typeC = typeC


        print("Creating input node for:", self.input)
        if self.input == "PARENT":
            self.selfInput = self.parent.cardParent
            print("Set as auto input: PARENT")

        if self.input == "NODE":
            self.selfInput = self.parent
            print("Set as auto input: NODE")

        if self.input == "GAME":
            self.selfInput = self.game

        

        self.CONNECTION = None

        if self.isOutput:
            self.x = 90
            self.parent.outputs.append(self)

            self.outputIndex = self.parent.outputs.index(self)

            print("IS OUTPUT")
        else:
            self.x = 10
            self.parent.inputs.append(self)

        self.pos = parent.game.v2(self.x, self.h)

        

    def getValue(self):

        if self.selfInput:
            return self.selfInput
        
        if not self.CONNECTION:
            return "ERROR"
        try:
            RESULT = self.CONNECTION.parent.calc()

            if self.CONNECTION.parent.hasMultipleOutputs:
                RESULT = RESULT[self.CONNECTION.outputIndex]


        except:
            return "ERROR"
        return RESULT
    
    def connect(self, node):
        self.disconnect()

        if self.typeC != node.typeC and self.typeC != "ANY" and node.typeC != "ANY":
            print("WRONG TYPE")
            return

        node.disconnect()

        self.CONNECTION = node
        node.CONNECTION = self


    def disconnect(self):

        if self.CONNECTION:
            self.CONNECTION.CONNECTION = None

        self.CONNECTION = None
        

    def render(self):

        if self.selfInput:
            return

        POS = self.pos + self.parent.pos

        r = pygame.Rect(POS, [0,0])
        r.inflate_ip(8,8)

        if r.collidepoint(self.game.mouse_pos):
            w = 3

            if "mouse2" in self.game.keypress:
                self.disconnect()

            elif "mouse0" in self.game.keypress:
                if not self.game.activeNode:
                    self.game.activeNode = self 


                elif self.game.activeNode.isOutput != self.isOutput:

                    if self is self.game.activeNode:
                        self.disconnect()

                    else:
                        
                        self.connect(self.game.activeNode)

                        
                        self.game.activeNode = None
                else:
                    self.game.activeNode = None
        else:
            w = 1

        if self.CONNECTION:
            COLOR = [255,255,255]
        elif self.isOutput:
            COLOR = [0,255,0]
        else:
            COLOR = [0,255,255]


        pygame.draw.circle(self.game.screen, COLOR, POS, 8, width = w)

        t = self.game.font.render(str(self.typeC), True, [255,255,255])
        self.game.screen.blit(t, self.pos + self.parent.pos + [8, -12])

        if self.CONNECTION and self.isOutput:
            pygame.draw.line(self.game.screen, [255,255,255], POS, self.CONNECTION.pos + self.CONNECTION.parent.pos)




class DropDown:
    def __init__(self, parent, game, selections):
        self.game = game
        self.parent = parent

        self.dropDownSelections = selections #["attack", "health", "mana"]
        self.dropDownIndex = 0

        self.selected = False

    def render(self):

        POS = self.parent.pos + [4, 50]
        r = pygame.Rect([POS, [90, 20]])


        if not self.selected:

            t = self.game.font.render(self.dropDownSelections[self.dropDownIndex], True, [255,255,255])
            self.game.screen.blit(t, POS + [2, -4])

            if r.collidepoint(self.game.mouse_pos):
                w = 2

                if "mouse0" in self.game.keypress:
                    self.selected = True

            else:
                w = 1

            pygame.draw.rect(self.game.screen, [255,255,255], r, width=w)

        else:

            r.height = len(self.dropDownSelections) * 20

            for i, x in enumerate(self.dropDownSelections):
                
                if i == self.dropDownIndex:
                    c = [255,255,255]
                else:
                    c = [100,100,100]

                TPOS = POS + [2, -4 + i*20]

                r2 = pygame.Rect(TPOS - [2, -4], [90, 20])

                if r2.collidepoint(self.game.mouse_pos):
                    c = [255,0,0]
                    
                    if "mouse0" in self.game.keypress:
                        self.selected = False
                        self.dropDownIndex = i


                pygame.draw.rect(self.game.screen, c, r2, width=1)

                t = self.game.font.render(x, True, c)
                self.game.screen.blit(t, TPOS)

            pygame.draw.rect(self.game.screen, [255,255,255], r, width=1)



class Node:
    def __init__(self, game, cardParent, name, inputs, output, f, needs_dropdown = False, selections = []):
        self.name = name

        self.height = 100

        self.inputs = []
        self.outputs = []
        self.needs_dropdown = needs_dropdown

        if needs_dropdown:
            self.dropDown = DropDown(self, game, selections)
        else:
            self.dropDown = False

        self.f = f
        self.game = game
        self.cardParent = cardParent

        self.hasMultipleOutputs = False

        


        self.disp = ""

        self.pos = game.v2([random.randint(0, 1000), 0])

        for x in inputs:
            
            try:
                typeC = eval(inputs[x].split(":")[-1])
            except:
                typeC = "ANY"

            InputNode(self, x, typeC, False)

        if output:

            print("Creating the output")

            typeC =  output

            if "typing.Tuple" in str(typeC):
                print("MULTIPLE OUTPUTS")
                self.hasMultipleOutputs = True

                typeC = str(typeC).split("[")[1].split("]")[0]

                for x in typeC.split(","):
                    x = x.replace(" ", "")
                    InputNode(self, x, x, True)

            else:


                if str(typeC) == "<class 'inspect._empty'>":
                    print("IS EMPTY")
                    typeC = "ANY"

                InputNode(self, output, typeC, True)

            self.godNode = False
        else:
            self.godNode = True

        print("NODE:", name)
        print("INPUTS:", inputs)
        print("OUTPUTS", output)

        self.highLightNode = None

        self.errored = True

    def render(self):

        self.highLightNode = None

        r = pygame.Rect((self.pos, (100, self.height)))
        if r.collidepoint(self.game.mouse_pos):
            self.game.active = self
            w = 3
        else:
            w = 1


        pygame.draw.rect(self.game.screen, [255,0,0] if self.errored else [255,255,255], r, w)

        t = self.game.font.render(self.name, True, [255,255,255])
        self.game.screen.blit(t, self.pos)

        for x in self.inputs + self.outputs:
            x.render()

        if self.godNode:
            #print("\n\n\nGOD NODE", self.name, "BEGINS CALC")
            DISP = self.calc()
            #if DISP:
            #    print("SUCCESFUL!", DISP)

        if self.disp != "ERROR":

            if isinstance(self.disp, self.game.cardInstance):
                self.disp = self.disp.name
            elif not isinstance(self.disp, str):
                self.disp = str(self.disp)

            t = self.game.font.render(f"{self.disp}", True, [100,100,100] if not self.godNode else [255,255,255])
            self.game.screen.blit(t, self.pos + [10,20])

        if self.dropDown:
            self.dropDown.render()

            



    def calc(self):

        try:
            F_INPUTS = []

            for x in self.inputs:
                
                i = x.getValue()
                if i == "ERROR" or str(i) == "None":
                    self.errored = True
                    return

                F_INPUTS += [i]

            #print(self.name, "INPUTS:", F_INPUTS)

            RESULT = self.f(*F_INPUTS)
            #print("Returned", RESULT)
            if str(RESULT) != "None":
                self.disp = RESULT
            self.errored = False
            return RESULT
        


        except:
            print("FAIL CALCING", self.name)
            traceback.print_exc()
            self.errored = True
            self.disp = "ERROR"
            return ""

        


# Function to call and capture output
def track_function(func, *args, **kwargs):
    print(f"Calling {func.__name__} with arguments: {args} {kwargs}")
    result = func(*args, **kwargs)
    print(f"Output of {func.__name__}: {result}")
    return result

def getNodes(card, game):
    # Loop through all functions in the module

    NODES = []

    for name, obj in inspect.getmembers(functions):
        if inspect.isfunction(obj):
            # Get function signature (inputs)
            signature = inspect.signature(obj)
            print(f"\n\nFunction name: {name}, Signature: {signature}")

            print(signature.parameters)

            # Retrieve and check the docstring for the "DROPDOWN" marker
            docstring = obj.__doc__ if obj.__doc__ else "No docstring available"
            print(f"Docstring: {docstring}")
            needs_dropdown = "DROPDOWN" in docstring.upper()  # Check for dropdown marker

            selections = []
            if needs_dropdown:
                for x in docstring.split("\n"):
                    print(x)

                    y = x.replace(" ", "")

                    if y in card.__dict__:

                        print("IS IN CARD DICT")
                        selections.append(y)

            inputs = {}
            for x in signature.parameters:
                inputs[x] = str(signature.parameters[x])

            output = signature.return_annotation
            print("OUTPUT RETURNED:", output)

            # Create the Node and pass the dropdown flag
            node = Node(game, card, name, inputs, output, obj, needs_dropdown, selections = selections)
            #node.needs_dropdown = needs_dropdown  # Add a custom attribute to Node
            NODES.append(node)

            # Debugging output for dropdown detection
            if needs_dropdown:
                print(f"Function {name} requires a dropdown.")

    return NODES
if __name__ == "__main__":
    getNodes()
