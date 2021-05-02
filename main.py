import shutil
import os
import json
import random


# called within create_master_instances() in order to build and insert the JSON
def create_master_json(directory, asins, reserves, domain, num_asins):
    fairgame_dict = {'asin_groups': 1, 'amazon_website': domain}

    count = 0
    new_list = []
    # adds asins to the new list
    while count < num_asins and asins:
        new_list.append(asins.pop(0))
        count += 1

    fairgame_dict['asin_list_1'] = new_list

    # asins added to dict, work on adding reserve values
    new_list = [reserves.pop(0)]

    # split the min/max price into seperate variables
    reserve_tokens = new_list[0].split(':')
    min_price = int(reserve_tokens[0])
    max_price = int(reserve_tokens[1])

    # assign the min/max values to the dict
    fairgame_dict['reserve_min_1'] = min_price
    fairgame_dict['reserve_max_1'] = max_price

    # dump fairgame_dict into a json file that Fairgame can utilize
    # insert the json file into the config directory for this current instance
    with open(os.path.join(directory, 'amazon_config.json'), 'w') as json_file:
        json.dump(fairgame_dict, json_file, indent=2)

    # return the new asins and reserves list with used values removed
    return asins, reserves


# function that creates instances using the master.json file
def create_master_instances(json_dict, directory, num_asins):
    # create list variables to manipulate while building instances
    asin_list = json_dict['asins']
    reserves_list = json_dict['reserves']

    # determine how many instances to create
    num_instances = len(reserves_list)

    # copy the Fairgame reference folder and insert new jsons
    current_instance = 1
    while current_instance <= num_instances:
        new_path = os.path.join(directory, f'{current_instance}')
        shutil.copytree('fairgame', new_path)

        # folder copied, insert new json into the correct Fairgame directory
        current_fg_dir = os.path.join(directory, f'{current_instance}', 'config')
        return_list = create_master_json(current_fg_dir, asin_list, reserves_list, json_dict['domain'], int(num_asins))

        # get our new lists back with used values removed
        asin_list = return_list[0]
        reserves_list = return_list[1]

        # create the install bat file if one doesn't exist
        if not os.path.exists(os.path.join(directory, 'mass_install.bat')):
            install_bat = open(os.path.join(directory, 'mass_install.bat'), 'a')

        # add to the install bat file for this instance
        install_bat.write(f'cd "{new_path}"\n')
        install_bat.write('start INSTALL.bat\n')

        # create the start bat file if one doesn't exist
        if not os.path.exists(os.path.join(directory, f'start_all_{instance_name}.bat')):
            start_bat = open(os.path.join(directory, f'start_all_{instance_name}.bat'), 'a')

        # add to the start bat file for this instance
        start_bat.write(f'cd "{new_path}"\n')
        start_bat.write('start _Amazon.bat\n')

        print(f'Created new instance at: {new_path}')

        # increment instance
        current_instance += 1


# creates the dev json and inserts into the correct instance directory
def create_dev_json(directory, asins, reserves, json_dict, num_asins):
    fairgame_dict = {}

    # create a list called items that will be used in the fairgame_dict
    items = []
    # create a dictionary to go inside the items list
    items_dict = {}

    # get the asins
    count = 0
    new_list = []
    # adds asins to the new list
    while count < num_asins and asins:
        new_list.append(asins.pop(0))
        count += 1

    items_dict['asins'] = new_list

    # asins added to dict, work on adding reserve values
    new_list = [reserves.pop(0)]

    # split the min/max price into seperate variables
    reserve_tokens = new_list[0].split(':')
    min_price = int(reserve_tokens[0])
    max_price = int(reserve_tokens[1])

    # assign reserve prices to the items dictionary
    items_dict['min-price'] = min_price
    items_dict['max-price'] = max_price

    items_dict['condition'] = json_dict['condition']
    items_dict['merchant_id'] = json_dict['merchant_id']

    # add the items dictionary as a list to the fairgame_dict
    items.append(items_dict)
    fairgame_dict['items'] = items

    # add domain to the dictionary
    fairgame_dict['amazon_domain'] = json_dict['domain']

    # dump fairgame_dict into a json file that Fairgame can utilize
    # insert the json file into the config directory for this current instance
    with open(os.path.join(directory, 'amazon_requests_config.json'), 'w') as json_file:
        json.dump(fairgame_dict, json_file, indent=2)

    # return the new asins and reserves list with used values removed
    return asins, reserves


# function to create dev instances
def create_dev_instances(json_dict, directory, num_asins):
    # create list variables to manipulate while building instances
    asin_list = json_dict['asins']
    reserves_list = json_dict['reserves']

    # determine how many instances to create
    num_instances = len(reserves_list)

    # copy the Fairgame reference folder and insert new jsons
    current_instance = 1
    while current_instance <= num_instances:
        new_path = os.path.join(directory, f'{current_instance}')
        shutil.copytree('fairgame-dev', new_path)

        # folder copied, insert new json into the correct Fairgame directory
        current_fg_dir = os.path.join(directory, f'{current_instance}', 'config')
        return_list = create_dev_json(current_fg_dir, asin_list, reserves_list, json_dict, int(num_asins))

        # get our new lists back with used values removed
        asin_list = return_list[0]
        reserves_list = return_list[1]

        # check if user has enabled proxies
        if json_dict['proxies']:
            create_proxy_json(current_fg_dir, json_dict)

        # create the install bat file if one doesn't exist
        if not os.path.exists(os.path.join(directory, 'mass_install.bat')):
            install_bat = open(os.path.join(directory, 'mass_install.bat'), 'a')

        # add to the install bat file for this instance
        install_bat.write(f'cd "{new_path}"\n')
        install_bat.write('start INSTALL.bat\n')

        # create the start bat file if one doesn't exist
        if not os.path.exists(os.path.join(directory, f'start_all_{instance_name}.bat')):
            start_bat = open(os.path.join(directory, f'start_all_{instance_name}.bat'), 'a')

        # add to the start bat file for this instance
        start_bat.write(f'cd "{new_path}"\n')
        start_bat.write('start _Amazonrequests.bat\n')

        print(f'Created new instance at: {new_path}')

        # increment instance
        current_instance += 1


# Create an instance of Amazon AIO using alpha branch
def create_alpha_instance(alpha_json, proxy_json, directory):
    new_path = os.path.join(directory, 'amazon_aio')
    shutil.copytree('fairgame-alpha', new_path)

    fg_config_dir = os.path.join(directory, 'amazon_aio', 'config')

    # dump the aio json
    with open(os.path.join(fg_config_dir, 'amazon_aio_config.json'), 'w') as json_file:
        json.dump(alpha_json, json_file, indent=2)

    # create and dump proxies json
    create_proxy_json(fg_config_dir, proxy_json)

    print(f'New instance created at: {new_path}')


# function that creates proxies if the user enters them in the json
def create_proxy_json(directory, json_dict):
    proxies = []
    username = json_dict['user']
    password = json_dict['pass']

    # check how the users proxies should be set up depending on their selected options in the json
    if json_dict["ip_auth"]:
        # build proxies list using ip_auth format
        for i in json_dict["ip_port"]:
            proxies.append(
                {
                    "http": f"http://{i['http']}",
                    "https": f"http://{i['https']}",
                }
            )
    elif json_dict["socks5"]:
        # build the proxies list using socks5
        for i in json_dict["ip_port"]:
            proxies.append(
                {
                    "http": f"socks5://{username}:{password}@{i['http']}",
                    "https": f"socks5://{username}:{password}@{i['https']}",
                }
            )
    elif json_dict["socks5h"]:
        # build the proxies list using socks5h
        for i in json_dict["ip_port"]:
            proxies.append(
                {
                    "http": f"socks5h://{username}:{password}@{i['http']}",
                    "https": f"socks5h://{username}:{password}@{i['https']}",
                }
            )
    else:
        # build the proxies list using user/pass format
        for i in json_dict["ip_port"]:
            proxies.append(
                {
                    "http": f"http://{username}:{password}@{i['http']}",
                    "https": f"http://{username}:{password}@{i['https']}",
                }
            )

    # randomize the proxy lists
    random.shuffle(proxies)

    # add the list of dictionaries to a dictionary fairgame can use
    proxy_dict = {'proxies': proxies}

    # dump the dictionary into a json
    with open(os.path.join(directory, 'proxies.json'), 'w') as json_file:
        json.dump(proxy_dict, json_file, indent=2)


if __name__ == "__main__":
    # set a variable for the root directory
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_DIR = os.path.join(ROOT_DIR, "config")
    invalid_json = False
    alpha_instance = False

    print('Welcome to the Fairgame Instance Creator')
    print('-' * 80)
    print(f'Root directory = "{ROOT_DIR}"')
    print(f'!*!*MAKE SURE YOUR ROOT DIRECTORY CONTAINS A FAIRGAME REFERENCE FOLDER!*!*')
    print(f'!*!*YOUR REFERENCE FOLDER SHOULD BE NAMED "fairgame" FOR MASTER BRANCH!*!*')
    print(f'!*!*YOUR REFERENCE FOLDER SHOULD BE NAMED "fairgame-dev" FOR DEV BRANCH!*!*')
    print(f'!*!*YOUR REFERENCE FOLDER SHOULD BE NAMED "fairgame-alpha" FOR ALPHA BRANCH!*!*')
    print('-' * 80)
    instance_name = input('Enter a name for your instances: ')
    alpha = input('Using Alpha branch? (y/n): ')
    if alpha == 'y':
        alpha_instance = True
    if not alpha_instance:
        asins_per = input('Enter the amount of ASINs you want to check per instance: ')
    print('-' * 80)

    # create the instance directory if it doesn't already exist
    if not os.path.exists(instance_name):
        os.makedirs(instance_name)

    # set a variable for the instance directory
    INSTANCE_DIR = os.path.join(ROOT_DIR, instance_name)

    print(f'Instance Directory = {INSTANCE_DIR}')
    print('Detecting if valid JSON is present...')
    # create alpha instance if json files are present
    if alpha_instance and os.path.exists(os.path.join(CONFIG_DIR, 'alpha', 'alpha.json')):
        print('Lets create an instance using alpha.json')
        with open(os.path.join(CONFIG_DIR, 'alpha', 'alpha.json')) as f:
            alpha_dict = json.load(f)
            with open(os.path.join(CONFIG_DIR, 'alpha', 'proxies.json')) as k:
                proxy_dict = json.load(k)
                create_alpha_instance(alpha_dict, proxy_dict, INSTANCE_DIR)
    else:
        print('No valid alpha JSON file is present. Please close the program and look in your config/alpha folder. '
              'Make sure that your config files are spelled correctly ("alpha.json" or "proxies.json")')

    # if else branches to detect if a valid master or dev JSON is present
    if os.path.exists(os.path.join(CONFIG_DIR, 'master.json')):
        print('Found master.json; Let\'s create your master instances :)')
        print('Creating instances can take time depending on your PC\'s specs, so have patience...')
        with open(os.path.join(CONFIG_DIR, 'master.json')) as f:
            master_dict = json.load(f)
            create_master_instances(master_dict, INSTANCE_DIR, int(asins_per))
    elif os.path.exists(os.path.join(CONFIG_DIR, 'dev.json')):
        print('Found dev.json; Let\'s create your dev instances...')
        print('Creating instances can take time depending on your PC\'s specs, so have patience...')
        with open(os.path.join(CONFIG_DIR, 'dev.json')) as f:
            dev_dict = json.load(f)
            create_dev_instances(dev_dict, INSTANCE_DIR, int(asins_per))
    elif not alpha_instance:
        print('No valid JSON file is present. Please close the program and look in your config folder. '
              'Make sure that your config file is spelled correctly ("master.json" or "dev.json")')
        invalid_json = True

    if not invalid_json and not alpha_instance:
        print('-' * 80)
        print('DONE! Run the mass_install.bat file in your instance directory to install all instances.')
        print('Run the start_all.bat in your instance directory to start all instances.')
        print('Starting many instances at once can take some time, have patience!')
        print('When closing your instances, use Ctrl + C to kill the instances before closing them.')

    if alpha_instance:
        print('Make sure to run the INSTALL.bat file in your new instance directory in order to install it.')
        print('Once you have completed installation your instance is ready to run with _Amazon_aio.bat')
