import xmlrpc.client

print("=== RMI String Concatenation Client ===\n")

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

str1 = input("Enter First String : ")
str2 = input("Enter Second String : ")

print("\n[Client] Sending strings to server for concatenation...")

result = proxy.concatenate_strings(str1, str2)

print(f"\n[Client] Result received from Server: '{result}'")