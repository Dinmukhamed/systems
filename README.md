# Productivity Tool for Developers
## Git
### gitroutine

This is a line to be added to either:

1. /etc/gitconfig
2. ~/.gitconfig
3. config file in the Git directory (that is, .git/config) of whatever repository you’re currently using.

Where c overwrites b overwrites a.

It is suggested you put this line inside the config file specific to the local git repo.

Once you did that, you can use:

``git routine``

and it will do these three things in one go:

1. ``git add .``
2. ``git commit``
3. ``git push``

Upon git commit, you will get a pop up window where you can write your commit message, if you save then step 3. is executed automatically.

This will save a lot of time when you have to commit often.

### post-receive

This is a git post-receive hook that does two things:

1. Sends Slack notifications that something has been pushed to the git repository on your remote server.
2. Deploys the code on a specific branch to a specific path on your remote server everytime you push.

Please refer to the comments to make custom changes to the code so it will work for your case.

For 1. please follow the instructions on: https://github.com/chriseldredge/git-slack-hook

For 2. please change the following in the code before you use it:

Instead of:

``if [ "$refname" == "refs/heads/yourchosenbranch" ]``

change the yourchosenbranch to the actual name of the branch where you wish to implement push-to-deploy.

Instead of:

``GIT_WORK_TREE="/home/your/test/environment/remotely/" git checkout yourchosenbranch -f``

Change the path again as before and also change yourchosenbranch to the same branch you wish to implement the hook.

Then you put this script with the same name as post-receive to the hooks directory on your git bare repo on the remote.

After that in the terminal and in the directory where post-receive is stored type:

``chmod +x post-receive``

This will make post-receive executable. Refer to this tutorial if you need more help: 

[http://krisjordan.com/essays/setting-up-push-to-deploy-with-git](http://krisjordan.com/essays/setting-up-push-to-deploy-with-git)

## Automation
### backup.py

This script automates the back up of individual branches on your git. If you have lots of branches and you wish
to back them up individually, it is a good idea not to manually back up each branch but use this script to do it automatically.

Please put this script outside of the git repo you wish to back up since it will change branches and make the script disappear 
while it is running. Put it on your desktop and run:

``python backup.py``

If you leave the file as it is you get input prompts to state where your local git repo and backup path are. Type them in with / at the 
end. The only thing you need to customise is to update the ``branchname`` variable with the actual names of your branches 
as a Python list. Feel free to automate this one as well for general use cases.

### filecopy.py
Ever had the experience where you need to update one file and then copy paste it across all your git branches? Like .gitignore
you wish to populate on every single branch or some of the branches in your git and you cannot use the global .gitignore configuration 
to do that? This file may solve the problem by automatically copying your changes file to all git branches.

Before running the script, make sure that your git is up to date with your remote. Also make sure that you change ``branchname`` variable to the appropriate list
of your local git repo's branches to which you wish to paste your file. This will give you freedom to choose which branch you 
wish to copy the file into.

Run this script outside your git repo. Place the file that you wish to paste to your git branches also outside the git repo. 
run this script with Python and input the paths. The script also will git push all your changes on each branch.

##Apache
###domain_redirection.config
Using this file you can redirect many domains to the same server and host different websites on the same remote.

The general principles of multi-domain management is to let many different domains and subdomains point to the same remote server, each of which displaying only the content of a specific folder in the var/www/html public directory.

This can be achieved by:

1. Change the DNS zones, the A records, to point towards the public IP address of the remote server
2. If a subdomain is required, then name host to be the name of the subdomain without anything after, say subdomain1 just subdomain1 and not subdomain1.yourdomain.com
3. If the actual domain should point to the remote then state in the host of the A record: @
4. After changing the DNS, everything else is handled on the remote
5. Go to the remote and ssh into it
6. Then find the folder /etc/apache2
7. There are two folders of interest: sites-available, sites-enabled
8. In both are files and they may already be a common file, same name for each directory: domain_redirection.conf
9. If not then use the template that is supplied in this repository
10. Then change the ServerName to the new subdomain created
11. Change the DocumentRoot in each of the sections to the appropriate directory into which the subdomain or domain should point to
12. Place this file in the directory /etc/apache2/site-available and NOT site-enabled
13. Run this command: ``a2ensite example.com.conf``
14. Restart apache2 by: ``service apache2 restart``

Please read this tutorial for more information on domain redirection:

[https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-14-04-lts](https://www.digitalocean.com/community/tutorials/how-to-set-up-apache-virtual-hosts-on-ubuntu-14-04-lts)

Thank you for your patience of reading this documentation and please provide some feedback if you get the chance.

Happy Coding!
