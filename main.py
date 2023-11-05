from requests_html import HTMLSession
import random
import json

with open('yes_no_check.txt', 'r') as file:
    data = file.read()  # Reads the txt file (stored as a string)
    data_js = json.loads(data)  # Convert the string into a json (dictionary)
    yes_list = data_js["yes"]  # Stores each value into a variable to make sure the file only gets opend once
    no_list = data_js["no"]
    sarcastic_list = data_js["sarcastic"]

with open('temp_responses.txt', 'r') as file:  # note I still need to add a feature to check if the file exists and if not, adds it
    data = file.read()  # Reads the txt file (stored as a string)
    data_js = json.loads(data)  # Convert the string into a json (dictionary)
    hot_list = data_js["Hot"]  # Stores each value into a variable to make sure the file only gets opend once
    warm_list = data_js["Warm"]
    cool_list = data_js["Cool"]
    chilly_list = data_js["Chilly"]
    cold_list = data_js["Cold"]

def only_alpha(raw_input):  # Takes in an input and converts it into only alphabetical letters, discarding the rest such as 1-9, #, etc
    raw_input = raw_input.lower()
    cleaned_input = ''
    for i in raw_input:
        if i >= 'a' and i <= 'z' or i == ' ':
            cleaned_input = cleaned_input + i
    return cleaned_input

def random_number(start_num, end_num):
    return random.randint(start_num, end_num)

def loading_phrase(robot_tomfoolery_request):  # I will store this in a txt file soon, just I have it here for now, picks a loading text by random
    with open('loading_phrases.txt', 'r') as file:
        data = file.readlines()
        return print(data[robot_tomfoolery_request - 1])

def yes_no(input_decider):
    if input_decider in yes_list:
        return 'yes'
    elif input_decider in no_list:
        return 'no'
    elif input_decider in sarcastic_list:
        return 'sarcastic'
    else:
        return 'put y/yes, n/no or something like that dummy'

def query_area(query):  # Sends the query through google to retrieve page info - reference: https://www.youtube.com/watch?v=cta1yCb3vA8
    query.strip()
    query = query.lower()
    url = f'https://www.google.com/search?q=weather+{query}'

    s = HTMLSession()
    r = s.get(url, headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'})  # The header is for google to not recognise this as a bot as to make this work

    return r

def inputted_place():
    query = input('what area u want: ')
    query = only_alpha(query)
    return query

def temp():
    def temp_phrase(temp):  # Reads the txt file located, stores the information as a json (dictionary) and outputs depending on the argument given through the function


            if temp >= 25:
                return print(random.choice(hot_list), str(temp) + str("°C"))
            elif temp >= 20:
                return print(random.choice(warm_list), str(temp) + str("°C"))
            elif temp >= 15:
                return print(random.choice(cool_list), str(temp) + str("°C"))
            elif temp >= 10:
                return print(random.choice(chilly_list), str(temp) + str("°C"))
            else:
                return print(random.choice(cold_list), str(temp) + str("°C"))

    while True:

        robot_tomfoolery_request = random_number(1, 10)  # Selects a random number between 1 and 10 for the loading text

        query = inputted_place()

        loading_phrase(robot_tomfoolery_request)

        if robot_tomfoolery_request == 9 or robot_tomfoolery_request == 10:
            return 'stop'  # Angsty of this bot just doesn't wanna do it :)

        try:
            r = query_area(query)  # Searches the information of the inputted area
            temperature = int(r.html.find('span#wob_tm', first=True).text)  # Finds the ID within the HTML of the page equal to the first argument and stores it as temperature
            temp_phrase(temperature)  # Uses a phrases correlating to the temperature
            while True:
                restart = input("u wanna search up another place's temp?: ")  # requests if they want to search another place's temp
                restart = only_alpha(restart)
                yes_or_no = yes_no(restart)

                if yes_or_no == 'yes':
                    break
                elif yes_or_no == 'no':
                    return 'no'
                elif yes_or_no == 'sarcastic':
                    return 'sarcastic'
                else:
                    print(yes_or_no)

        except:
            print("that ain't a place -_- put a real one")  # If the place doesn't exist, loop back

def weather():
    while True:
        robot_tomfoolery_request = random_number(1, 10)
        query = inputted_place()

        loading_phrase(robot_tomfoolery_request)

        if robot_tomfoolery_request == 9 or robot_tomfoolery_request == 10:
            return 'stop'  # Angsty of this bot just doesn't wanna do it :)

        try:
            r = query_area(query)
            weather_info = r.html.find('span#wob_dc', first=True).text

            print("weather:", weather_info)

            while True:
                restart = input("u wanna search up another place's weather?: ")  # requests if they want to search another place's temp
                restart = only_alpha(restart)
                yes_or_no = yes_no(restart)

                if yes_or_no == 'yes':
                    break
                elif yes_or_no == 'no':
                    return 'no'
                elif yes_or_no == 'sarcastic':
                    return 'sarcastic'
                else:
                    print(yes_or_no)
        except:
            print("that ain't a place -_- put a real one")  # If the place doesn't exist, use recursion

# ------------------------------------- MAIN LOOP -------------------------------------

while True:  # Angsty Bot :)
    choice = input("1. Temp\n2. Weather\n3. News\n4. Stop\nYour choice: ")
    if choice == '1':
        restart = temp()  # Check if they want to find a new place for the temperature
    elif choice == '2':
        restart = weather()  # Check if they want to find a new place for the temperature
    elif choice == '4':
        break

    if restart == 'no':
        pass
    elif restart == 'sarcastic':
        print('screw u too ig')
        robot_tomfoolery_restart = random_number(1, 2)

        if robot_tomfoolery_restart == 1:  # don't be rude :)
            break
        else:
            print('u better switch up that attitude')
    else:
        break