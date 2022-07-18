# script

# build project
## add project to config.ini
[alexandrite_daily]  
project_name = alexandrite  
code_path = /home/cn1396/workspace/code/alexandrite_daily  
release_path = /var/www/html/share/daily_build/alexandrite  
notify_email = jinping.wu@verisilicon.com  
repo_cmd = repo init -u ssh://gerrit-spsd.verisilicon.com:29418/manifest --repo-url=ssh://gerrit-spsd.verisilicon.com:29418/git-repo \  
    -b spsd/master -m Alexandrite/freertossdk.xml  
  
## call project build
from build import project_build  
project_build('alexandrite_daily')  
  