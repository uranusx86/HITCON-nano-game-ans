def game0(line):
    if line == 'Nano$ enter your answer:':
        # enter you answer here
        # https://www.wikiwand.com/en/Morse_code
        answer = 'HITCONNANOGAMEMORSE'
        port.write('%s\n' % answer)
        port.flush()