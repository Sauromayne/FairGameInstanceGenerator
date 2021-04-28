# About FairGame Instance Creator
I created this program in order to make creating multiple instances of FairGame easier. I was tired of copying multiple config files and folders. With FairGame Instance Creator you can easily create multiple instances from a single JSON file. I hope that by publishing this on GitHub, others will be able to enjoy its benefits. Please read through this document in order to learn how to properly setup your JSON file and utilize the program.

This program was developed and tested using Windows 10, I do not know if it works on other operating systems. If the OS supports Python then it should work but I have no way to test it personally.

## Requirements

 - [FairGame](https://github.com/Hari-Nagarajan/fairgame) by [Hari-Nagarajan](https://github.com/Hari-Nagarajan) 
 - The ability to read this document and properly configure your JSON file / FairGame reference folder
 - [Python](https://www.python.org/downloads/release/python-388/) (Was developed with 3.8.8, maybe works with other versions?)

## Current Limitations
- The current version can only create instances that use one `asin_list`
- The current version can only create instances that use one `amazon_website` domain

**Currently only supports master branch but dev branch will be added very soon!**

These features are not useful for me so I have not implemented them yet. 

In regards to multiple `asin_list`'s, I do not see the need to use more than 2-3 ASIN's per instances and you can easily find 2-3 ASIN's within the same price range. 

In regards to multiple `amazon website` domains, I just do not have a need for this but might implement in the future if there is enough demand. As of right now I feel adding these features would only complicate the JSON more than it needs to be.

### Disclaimer
*I will copy and paste the disclaimer located in the FairGame read me. Increasing the amount of instances only further increases the chance of the following:*

WARNING: The use of this software can result in a Amazon restricting access to your account and make it difficult for you to purchase products, with or without the bot. By using this software, you acknowledge these risks. These restrictions cannot and will not be resolved by the developer(s), nor can they be detected/resolved by the standard Amazon Customer Support, as far as we are aware. If this happens, the only resolution is to stop all Amazon monitors (e.g., FairGame, Distill.io, or other bots, etc.), wait, and hope the limits are lifted within a few days. If this is a major issue you should consider avoiding use of this software. 

Account restrictions may be triggered by any of the following: 1) running multiple instances on one device, 2) running multiple instances on different devices, using the same account, regardless of their IP, proxy, or location, 3) configuring an instance to check stock too frequently/aggressively (default settings not guaranteed to be safe). 

Symptoms of account restrictions include: 1) Fly-out (offers) window is missing/completely blank, even if there are listings for the ASIN, 2) frequent CAPTCHA checks, 3) inability to access the My Account page, add items to your cart, or complete purchases; usually displayed as a 503 error (Amazon Dogs & “SORRY we couldn’t find that page” message). You’ll likely have to sit-out a few days of drops to resolve the throttle.

# HOW TO:

 1. Download your desired branch of [FairGame](https://github.com/Hari-Nagarajan/fairgame) to use as a reference for your instances.
 
 2. Configure your reference folder like you normally would. Add any flags you want to use to the `_Amazon.bat` file in your reference folder so that it gets copied to all instances. **Read the FairGame readme, do not ask me how to configure FairGame. If you don't already know how, then maybe multiple instances is not for you.** It is highly recommended that you set up at least 1 config file so that you can fully install and configure your reference folder. Login to account, activate 1 click settings, etc. 
 
 Also, in order to make mass installation of your instances easier rename `__INSTALL (RUN FIRST).bat` to `INSTALL.bat` and remove the first `pause` in the batch file.
 
 3. Now that you have a fully configured and working FairGame reference folder name it `fairgame` for master branch, or `fairgame-dev` for dev branch **(DEV BRANCH TO BE ADDED SOON)**. Place the reference folder in the ROOT directory of this project:
 ![Root directory with reference folder](https://lh3.googleusercontent.com/EYiTosS2ii7ihzwOwmtp_QhE9dy1cIq-ylO5_yPyATWWounMuNPb5fgnag0oqpriLZYCXo7LPnHgAnZzw56Xzo1pxt97kEWKcmNDCS_lR9XaxSIp2Eh8nS2avgm3c7s4q7JpWi_zXshpE173dnt8YlrNb2Ot3ApOSb6qKOj_IByrUr4yxhFuGNchqRcmCNYueoctoxj_duiuNNcS8ntgksSMyIlIHQlzg8UNQf-xOPwl_D6rXHsJDWkrkfj_uZim3LrAbGz-RuOPGfCrs2o6KnM8bw7tPVsMUz4Y16lDHCHmEZTSRL_M6Sja4oTdj6ZdCE8fVVhuoQcSkSoHcqyHOFUCKUb7SM7gOuofjb2KkRcJFdFEyarQbHGfzwUgw7Fcx281B3z8VFY8EdfwtjMHwFzHAm5mx1k1q7Y_cw1nJDiR2yTbIaOdxr2x6wo1L9o_hhJI5uet2-_0RJxs29hX_qXzCCxVzbxhtt9vnSM0sfvouOZ2HmLw6CClqeFJipd49b4Rc4-TXGwh91YSjUGU1c86AUPxTM5qLlInO45R3hcj_DPRJdfGLsaUSIUAy7qMvW3q8ABoreXdgclGSRgPc5v0oznbYgki9K11FhQex4bTUesmWSh00eNoQjUsxc6L9qguAptAIdWu1J9DZIkLKUr11E5iinla5lLXC-50mM1YVPDToBGq0o4tg80w2IJDYmhxqofT7PyrGG7NwLqpBQlC=w619-h177-no?authuser=0)

4. Now we will configure the JSON file which is located in the `config` directory. Right click and edit either the master.json or dev.json files (Dev branch support will be added soon)

**MASTER BRANCH JSON CONFIGURATION**

![JSON reference for 2 instances.](https://i.postimg.cc/43XQmDqg/JSON-ref.png)
The above images shows how the instances will be created if using 2 ASIN's per instance with the default JSON file. The amount of reserves determines how many instances will be created. I setup the default JSON with the idea of creating 5 instances using 2 ASIN's each. You can see from the picture how the reserve price and asins are linked.

Setting up the JSON is pretty self explanatory. Put in all the ASIN's you want your instances to check, and setup the reserve prices accordingly. When setting up the JSON it might be helpful to go in with a plan...For example if you want to check 30 ASIN's using 2 ASIN's per instance, you will need to have 15 reserve prices in the `reserves` list.

5. Now that your reference folder and JSON files are properly configured, you are ready to run the program: 

	

 - Run the `create_instances.bat` file in your ROOT directory. 	
 - Enter a name for your instances (This is what the folder for your instances will be called).
 - Enter how many ASIN's you want each instance to have.

Here is a picture showing what a successful run of the program will look like:
![Successful output. ](https://i.postimg.cc/KvHnZKrt/image.png)

6. Navigate to your new instance directory and you will see a `mass_install.bat` and `start_all.bat` file in your directory. Run  `mass_install.bat` to install all instances, run  `start_all.bat` to start all instances.
7. Congratulations you have successfully used this program to create multiple instances of FairGame!

**DEV BRANCH JSON CONFIGURATION**

To be added soon!