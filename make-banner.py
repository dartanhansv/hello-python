def banner(message, border='-'):
    line = border * len(message)
    print(line)
    print(message)
    print(line)

def main():
    message = input('Type your message: ')
    banner(message)
main()
