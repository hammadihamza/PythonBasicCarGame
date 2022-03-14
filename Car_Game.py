command = ""
i = 0
j = 0
while True:
    command = input("> ").lower()
    if command == "start" and i == 0:
        print('car starting...')
        i += 1
        j = 0
    elif command == "stop" and j == 0 and i > 0:
        print('car stopping...')
        j += 1
        i = 0
    elif command == "quit":
        break
    elif command == "help":
        print("""start 
stop
quit""")
    else:
        print("Error")


