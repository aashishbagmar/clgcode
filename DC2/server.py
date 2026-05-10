from xmlrpc.server import SimpleXMLRPCServer

def concatenate_strings(str1, str2):
    print(f"\n[Server] Received String 1: '{str1}'")
    print(f"[Server] Received String 2: '{str2}'")

    result = str1 + " " + str2

    print(f"[Server] Concatenated Result: '{result}'")

    return result

print("RMI Server Started on port 8000...")

server = SimpleXMLRPCServer(("localhost", 8000), logRequests=False)

server.register_function(concatenate_strings, "concatenate_strings")

print("Waiting for client requests...\n")

server.serve_forever()