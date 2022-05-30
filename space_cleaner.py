#Example: Hi!   How  are       you?
message = input('Enter message: ')

message_list = message.split()
result = ' '.join(message_list)

print(result)