my_name = '''
  _______           _                     _____                                  
 |__   __|         | |                   / ____|                                 
    | | _   _  ___ | |__    __ _  _ __  | |  __   __ _  _   _  _ __  __ _ __   __
    | || | | |/ __|| '_ \  / _` || '__| | | |_ | / _` || | | || '__|/ _` |\ \ / /
    | || |_| |\__ \| | | || (_| || |    | |__| || (_| || |_| || |  | (_| | \ V / 
    |_| \__,_||___/|_| |_| \__,_||_|     \_____| \__,_| \__,_||_|   \__,_|  \_/  
'''
end = "A program by -"
ending_msg = end+my_name

welcome_text = "Welcome to the SpeechSynth "
version_no = "v1.0"
welcome_msg = welcome_text+version_no

def welcome():
    print(welcome_msg)

def name():
    print(my_name)

def ending():
    print(ending_msg)
