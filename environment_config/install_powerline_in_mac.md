# Install powerline via pip (python package manager)
-  pip install powerline-status

# Find the location

$ pip show powerline-status

It shows that the powerline-status is installed at
```shell script
 /Users/admin/anaconda/lib/python3.6/site-packages
``` 

Step 2: Configuration
To activate powerline, you need to source powerline.sh in your .bash_profile
Open up your .bash_profile in Vim or any editor

$ vim ~/.bash_profile

Paste this code into your .bash_profile
``
# Powerline
powerline-daemon -q
POWERLINE_BASH_CONTINUATION=1
POWERLINE_BASH_SELECT=1
source /Users/admin/anaconda/lib/python3.6/site-packages/powerline/bindings/bash/powerline.sh
``
Now, create a configuration directory for powerline in your home directory and copy the config_files/ directory from the powerline direcory.

$ mkdir ~/.config/powerline
$ cp -r /Users/admin/anaconda/lib/python3.6/site-packages/powerline/ ~/.config/powerline/