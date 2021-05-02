# About FairGame Instance Generator
I created this program in order to make creating multiple instances of FairGame easier. I was tired of copying multiple config files and folders. With FairGame Instance Creator you can easily create multiple instances from a single JSON file. I hope that by publishing this on GitHub, others will be able to enjoy its benefits. Please read through this document in order to learn how to properly setup your JSON file and utilize the program.

This program was developed and tested using Windows 10, I do not know if it works on other operating systems. If the OS supports Python then it should work but I have no way to test it personally.

## Requirements

 - [FairGame](https://github.com/Hari-Nagarajan/fairgame) by [Hari-Nagarajan](https://github.com/Hari-Nagarajan) 
 - The ability to read this document and properly configure your JSON file / FairGame reference folder
 - [Python](https://www.python.org/downloads/release/python-388/) (Was developed with 3.8.8, maybe works with other versions?)

## Current Limitations
- The current version can only create instances that use one `asin_list`
- The current version can only create instances that use one `amazon_website` domain

These features are not useful for me so I have not implemented them yet. 

In regards to multiple `asin_list`'s, I do not see the need to use more than 2-3 ASIN's per instances and you can easily find 2-3 ASIN's within the same price range. 

In regards to multiple `amazon website` domains, I just do not have a need for this but might implement in the future if there is enough demand. As of right now I feel adding these features would only complicate the JSON more than it needs to be.

## Known errors
![Permission error](https://i.postimg.cc/XqgzzY4q/error.png)
- Permission error: Make sure that there are no chrome processes running in task manager. Kill them if there are and try to make the instances again. This can be avoided by always killing your instance with ctrl + c when setting up the reference folder.

### Disclaimer
*I will copy and paste the disclaimer located in the FairGame read me. Increasing the amount of instances only further increases the chance of the following:*

WARNING: The use of this software can result in a Amazon restricting access to your account and make it difficult for you to purchase products, with or without the bot. By using this software, you acknowledge these risks. These restrictions cannot and will not be resolved by the developer(s), nor can they be detected/resolved by the standard Amazon Customer Support, as far as we are aware. If this happens, the only resolution is to stop all Amazon monitors (e.g., FairGame, Distill.io, or other bots, etc.), wait, and hope the limits are lifted within a few days. If this is a major issue you should consider avoiding use of this software. 

Account restrictions may be triggered by any of the following: 1) running multiple instances on one device, 2) running multiple instances on different devices, using the same account, regardless of their IP, proxy, or location, 3) configuring an instance to check stock too frequently/aggressively (default settings not guaranteed to be safe). 

Symptoms of account restrictions include: 1) Fly-out (offers) window is missing/completely blank, even if there are listings for the ASIN, 2) frequent CAPTCHA checks, 3) inability to access the My Account page, add items to your cart, or complete purchases; usually displayed as a 503 error (Amazon Dogs & “SORRY we couldn’t find that page” message). You’ll likely have to sit-out a few days of drops to resolve the throttle.

# Quick Start:

 **Download your desired branch of [FairGame](https://github.com/Hari-Nagarajan/fairgame) to use as a reference for your instances.**
 
  - [Master Branch](https://github.com/Hari-Nagarajan/fairgame): Uses selenium and buy now checkout flow to attempt purchases on Amazon.
  - [Dev Branch](https://github.com/Hari-Nagarajan/fairgame/tree/development): Uses requests through Python to check stock and attempts to utilize turbo checkout when it finds stock
  - [Alpha Branch](https://github.com/Hari-Nagarajan/fairgame/tree/alpha): Uses asyncio through Python to check all ASINs simultaneously (Thus only needing one instance). 1 proxy is assigned to 1 ASIN. So if you have 10 ASINs but only 5 proxies, then 5 ASIN's will be running on your home IP.

Click any of the above links and then click "Code" ---> "Download Zip"; you can then extract this folder into the root directory of this project and rename accordingly.
 
 1. **For alpha branch you can likely skip this step since we are only creating one instance!** Configure your reference folder like you normally would. Add any flags you want to use to the `_Amazon.bat` file in your reference folder so that it gets copied to all instances. For dev branch you will need to add any flags to the `_Amazonrequests.bat` file. **Read the FairGame readme, do not ask me how to configure FairGame. If you don't already know how, then maybe multiple instances is not for you. It is highly recommended that you set up at least 1 config file so that you can fully install and configure your reference folder. Login to account, activate 1 click settings, etc.**
 
 Also, in order to make mass installation of your instances easier rename `__INSTALL (RUN FIRST).bat` to `INSTALL.bat` and remove the first `pause` in the batch file.
 
 2. Now that you have a fully configured and working FairGame reference folder name it `fairgame` for master branch, `fairgame-dev` for dev branch, or `fairgame-alpha` for alpha branch. Place the reference folder in the ROOT directory of this project:
 
![Root directory with reference folder](https://i.postimg.cc/yxh7ybnK/image.png)

3. Now we will configure the JSON file which is located in the `config` directory. Alpha jsons can be found within the `alpha` directory which you will find in the `config` directory. Rename whichever json you will be using by changing the file extension from `.json_template` to `.json`. **IF YOU ARE USING ALPHA BRANCH YOU MUST HAVE BOTH A `alpha.json` AND `proxies.json` FILE. IT CANNOT BE RUN WITHOUT PROXIES USING THIS PROGRAM**

4. Check the JSON Configuration sections below for your desired branch, configure your jsons, and then you are ready to run the program! 

## Master Branch JSON Configuration

![JSON reference for 2 instances.](https://i.postimg.cc/43XQmDqg/JSON-ref.png)

The above images shows how the instances will be created if using 2 ASIN's per instance if you use 10 ASIN's and 5 reserve prices (2 instances per asin). The amount of reserves determines how many instances will be created. You can see from the picture how the reserve price and asins are linked.

Setting up the JSON is pretty self explanatory. Put in all the ASIN's you want your instances to check, and setup the reserve prices accordingly. When setting up the JSON it might be helpful to go in with a plan...For example if you want to check 30 ASIN's using 2 ASIN's per instance, you will need to have 15 reserve prices in the `reserves` list.


## Dev Branch JSON Configuration

![30 ASIN JSON](https://i.postimg.cc/7hSHR7W4/requests-json.jpg)

**Make sure you either delete or rename `master.json` if you want to run the dev branch. If both JSONS are present the program will default to master branch**

**If you are not using proxies (which I don't recommend), you can leave all the proxy data at their default values in the default JSON**

The above image represents a `dev.json` file configured for 30 ASIN's using 15 reserve prices. This means that I want 2 ASIN's per instance (30 / 2 = 15 instance). I would not recommend anyone to use this many instances unless you are also using proxies. Note that proxies is `true` (lowercase) which means that I have enabled proxies. More on proxies below..

### Merchant ID

- Use `"amazon"` to buy only from Amazon
- Use `"all"` to buy from any merchant on Amazon (Potential scam offers)

### Condition
![Condition List](https://i.postimg.cc/1zRK5rGW/image.png)

Any of these condition variables can be used for condition. If you use `Used` the bot will try to buy any items that are within your price range with the condition marked as Used or anything above it.

## Proxy JSON Configuration
![Proxies Config](https://i.postimg.cc/RFB4Hq0b/image.png)

- To enable proxies change `'"proxies":false` to `"proxies":true`
- Change any of the other flags to true (lowercase) if your proxies use ip auth or SOCKS5
- Change the user and pass strings to the username and password for your proxies.
- Enter the IP:PORT where you see `"XXX.XXX.XXX.XXX:XXXX"`
- Each dictionary contains two keys (http and https), enter the same IP:PORT for both keys. So each proxy should have 2 keys.
- Copy the dictionaries and fill in a different IP:PORT to add more proxies. The default JSON is setup to allow 2 proxies.

Make sure that you have enough proxies to support your instances if you are going to be running multiple instances of dev, it uses requests rather than selenium and running many instances without proxies will have a HIGH CHANCE OF GETTING SOFTBANS. Also, keep in mind that proxies are not foolproof and you could still get softbans regardless of proxies.

## Alpha Branch JSON Configuration
![Alpha JSON](https://i.postimg.cc/0j9JzpQN/image.png)

Each dictionary in the "items" list contains a value for "asins", "min-price", "max-price", "condition", and "merchant_id". You can create multiple dictionaries like the above image in order to use seperate values per asin, or you can place them all into one dictionary. **smile.amazon.com is the only working domain on alpha branch at the moment**

Condition and merchant_id values can be entered the same as they are described in the dev.json configuration instructions above. Proxies also use the same concept as above, the only difference is that proxies.json is its own file while using dev branch and there is no need to enable it with "true" as it is enabled by default.

Just remember that each ASIN is only assigned one proxy, so if you are going to have a large amount of ASIN's it is a good idea to also have a large amount of proxies. As a reference, I am only able to run 3 ASIN's on my home IP without getting softbans so I run 13 ASIN's with 10 proxies.

# Running the program
1. Now that your reference folder and JSON files are properly configured, you are ready to run the program: 
	
 - Run the `create_instances.bat` file in your ROOT directory. 	
 - Enter a name for your instances (This is what the folder for your instances will be called).
 - Enter how many ASIN's you want each instance to have, remembering how many asins you entered and how many reserve prices you entered.

Here is a picture showing what a successful run of the program will look like:
![Successful output. ](https://i.postimg.cc/KvHnZKrt/image.png)

2. Navigate to your new instance directory and you will see a `mass_install.bat` and `start_all.bat` file in your directory. Run  `mass_install.bat` to install all instances, run  `start_all.bat` to start all instances. These can take time to process if you have a lot of instances so be patient. If you did not rename  `__INSTALL (RUN FIRST).bat` to `INSTALL.bat` the `mass_install.bat` file will not work, so either start again or manually install all the instances.

3. Congratulations you have successfully used this program to create multiple instances of FairGame! :)
