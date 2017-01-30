# IntroMessage
### This file greets the user at the start of your Linux system. Pretty cool! :wink:
### Messages have been hardcoded using Google's TTS. You can create your own custom message.

## Installation
1. Clone the repository.
2. Fire up your terminal and type ```crontab -e```.
3. Type ```sleep 20 && python /path/to/the/script/location/intro.py &```.
4. Take care of that ```&``` at the end of command. The sleep command is so that the script doesn't run very early. So it waits for 20 seconds after the startup. You can change this according to your requirement.
5. Now go to the location of script and type ```chmod a+x intro.py``` to make the script executable.
6. Reboot and check :grinning:.
