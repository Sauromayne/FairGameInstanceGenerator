import shutil
import os
import json


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
        json.dump(fairgame_dict, json_file, indent=6)

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


if __name__ == "__main__":
    # set a variable for the root directory
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CONFIG_DIR = os.path.join(ROOT_DIR, "config")
    invalid_json = False

    print('Welcome to the Fairgame Instance Creator')
    print('-' * 80)
    print(f'Root directory = "{ROOT_DIR}"')
    print(f'!*!*MAKE SURE YOUR ROOT DIRECTORY CONTAINS A FAIRGAME REFERENCE FOLDER!*!*')
    print(f'!*!*YOUR REFERENCE FOLDER SHOULD BE NAMED "fairgame" FOR MASTER BRANCH!*!*')
    print(f'!*!*YOUR REFERENCE FOLDER SHOULD BE NAMED "fairgame-dev" FOR DEV BRANCH!*!*')
    print('-' * 80)
    instance_name = input('Enter a name for your instances: ')
    asins_per = input('Enter the amount of ASINs you want to check per instance: ')
    print('-' * 80)

    # create the instance directory if it doesn't already exist
    if not os.path.exists(instance_name):
        os.makedirs(instance_name)

    # set a variable for the instance directory
    INSTANCE_DIR = os.path.join(ROOT_DIR, instance_name)

    print(f'Instance Directory = {INSTANCE_DIR}')

    # if else branches to detect if a valid JSON is present
    print('Detecting if valid JSON is present...')
    if os.path.exists(os.path.join(CONFIG_DIR, 'master.json')):
        print('Found master.json; Let\'s create your master instances :)')
        print('Creating instances can take time depending on your PC\'s specs, so have patience...')
        with open(os.path.join(CONFIG_DIR, 'master.json')) as f:
            master_dict = json.load(f)
            create_master_instances(master_dict, INSTANCE_DIR, int(asins_per))
    elif os.path.exists(os.path.join(CONFIG_DIR, 'dev.json')):
        print('Found dev.json; Let\'s create your dev instances...')
        # FIXME: create function for dev json
    else:
        print('No valid JSON file is present. Please close the program and look in your config folder. '
              'Make sure that your config file is spelled correctly ("master.json" or "dev.json")')
        invalid_json = True

    if not invalid_json:
        print('-' * 80)
        print('DONE! Run the mass_install.bat file in your instance directory to install all instances.')
        print('Run the start_all.bat in your instance directory to start all instances.')
        print('Starting many instances at once can take some time, have patience!')
        print('When closing your instances, use Ctrl + C to kill the instances before closing them.')


