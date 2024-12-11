import functions
import inspect

def getNodes(card, game, Node):

    NODES = []
    # Loop through all functions in the module
    for name, obj in inspect.getmembers(functions):
        if inspect.isfunction(obj):
            # Get function signature (inputs)
            signature = inspect.signature(obj)
            print(f"Function name: {name}, Signature: {signature}")

            print(signature.parameters)
            
            inputs = {}
            for x in signature.parameters:
                inputs[x] = str(signature.parameters[x])

            output = signature.return_annotation
            
            card.nodes.append(Node(game, card, name, inputs, output, obj))


if __name__ == "__main__":
    getNodes()
