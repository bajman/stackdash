#!/usr/bin/env python3.8
import sys #this allows you to use the sys.exit command to quit/logout of the application
import subprocess
import time
import sys
import shutil


def main():
    print("\n\n\n\n StackDash v0.12 \n")
    #time.sleep(1)
    print(" ")

    choice = input("""                           

███████╗████████╗ █████╗  ██████╗██╗  ██╗    ██████╗  █████╗ ███████╗██╗  ██╗
██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██╔════╝██║  ██║
███████╗   ██║   ███████║██║     █████╔╝     ██║  ██║███████║███████╗███████║
╚════██║   ██║   ██╔══██║██║     ██╔═██╗     ██║  ██║██╔══██║╚════██║██╔══██║
███████║   ██║   ██║  ██║╚██████╗██║  ██╗    ██████╔╝██║  ██║███████║██║  ██║
╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ \n
StackDash is a python3 script, designed to automate Docker installation, container deployment, and subdomain hosting. \n
==============================================================================================================================================================
 ___  ___      ___       __   ___  __  
|__  |__   /\   |  |  | |__) |__  /__` 
|    |___ /~~\  |  \__/ |  \ |___ .__/ 

==============================================================================================================================================================

-- Docker Install Script
	  Removes old versions of Dockers and the installs of the lastest version of Docker Engine on Ubunutu over HTTPS
      (supported versions: 20.04 LTS, 19.10, 18.04 LTS, and 16.04 LTS) \n

-- Docker Containers/Stack Deployment Wizard
	  Deploys stacks and individual Docker web app containers
      [Type [w] for a complete list of containers that can be depoyed with StackDash] \n

-- Preconfigured Subdomains
	  Dedicated container subdomains (e.g., portainer.example.com or bookstack.example.com) \n 
      [Type [s] for a  list of subdomains that must be added as CNAME records to your DNS service (see Documenation for additional information)] \n

-- Automated Dashboard Deployment
      Deploys web dashboard/homepage for quick access to your Docker & server assets \n

-- HTTPS/TLS/OAuth 2 Supported
	  Traefik 2 routes external subdomain requests to the appropriate, internal server/container address.\n 

==============================================================================================================================================================
      ___ ___       __   __           __          __   __             
|\ | |__   |  |  | /  \ |__) |__/    |  \ |  /\  / _` |__)  /\   |\/| 
| \| |___  |  |/\| \__/ |  \ |  \    |__/ | /~~\ \__> |  \ /~~\  |  | 
                                                                      
==============================================================================================================================================================

  +----------------------------------------------------------------------------------------------+
  |                                                                                              |
  |                                                                                              |
  |                                     +----------------------------------------------------+   |
  |                                     |                                                    |   |
  |    +------------+     OAuth 2.0     | +-----------------+   HTTPS/TLS  +---------------+ |   |
  |    |            |    Google API     | |                | | LetsEncrypt |               | |   |
  |    |            +-------------------> |    TRAEFIK 2   +--------------->     SERVER    | |   |
  |    |  INTERNET  <-------------------| |     (Proxy)    <--------------+     (Docker)   | |   |
  |    |            | Exposed Port Nos: | |                | Proxy Routing |               | |   |
  |    |            |       80;443      | |                | Rules-Traefik |               | |   |
  |    +------------+                   | +-----------------+              +---------------+ |   |
  |                                     |                                                    |   |
  |                                     +----------------------------------------------------+   |
  |                                                       INTERNAL NETWORK                       |
  |                                                                                              |
  +----------------------------------------------------------------------------------------------+

==============================================================================================================================================================
 __   ___  __        __          __   __       ___              ___  __   __  
|  \ |__  |__) |    /  \ \ /    /  ` /  \ |\ |  |   /\  | |\ | |__  |__) /__` 
|__/ |___ |    |___ \__/  |     \__, \__/ | \|  |  /~~\ | | \| |___ |  \ .__/ 
                                                                                                                                                          
==============================================================================================================================================================
                                                                                                                      
Type [w] for a complete list of web apps you can deploy with StackDash. 
Type [c] to deploy individual containers. 

==============================================================================================================================================================
 __   ___  __        __          __  ___       __        __  
|  \ |__  |__) |    /  \ \ /    /__`  |   /\  /  ` |__/ /__` 
|__/ |___ |    |___ \__/  |     .__/  |  /~~\ \__, |  \ .__/ 
                                                                                                                        
==============================================================================================================================================================

Type [u] for a complete list of stacks you can deploy with StackDash.
Type [s] for a complete list of web app subdomain aliases used by StackDash. 
Type [t] to deploy the Data, DevOps, or Media StackDash Stacks. \n\n\n

==============================================================================================================================================================
      __  ___  ___ 
|\ | /  \  |  |__  
| \| \__/  |  |___                  
                                                                                      
==============================================================================================================================================================

---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬--- 
\n StackDash v. 0.1 is configured to support HTTPS & TLS only for domains managed by Cloudflare. Additional domain/hosting providers will be made available in future releases of StackDash. For a full list of planned DNS providers see: https://docs.traefik.io/https/acme/#providers. \n
---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬--- 
\n If you have domain name (e.g., example.com hosted by GoDaddy or Google Cloud) and would like to make Cloudflare your free, default DNS record manager: \n  
You simply need to add two DNS records to your Cloudflare account. For more information on adding vendor-specific records to your free Cloudflare account, see: https://support.cloudflare.com/hc/en-us/articles/360020991331-Adding-vendor-specific-DNS-records-to-Cloudflare. Cloudflare can manage DNS records on domains hosted by Google Cloud, Amazon S3, Microsoft Azure, ClickFunnels, WPEngine, and Zoho. \n
---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬---¬--- 
\n If you do not have a domain, you can purchase one through Cloudflare (about $8.XX per year) at https://www.cloudflare.com/products/registrar/  

    Please enter your choice:  """)
    if choice == "1" or choice =="1.":
        docker_install()
        print("*** Install Docker Engine **** ")
    elif choice == "2":
        stacks_main()
        print("*** Deploy Stacks **** ")
    elif choice == "3":
        containers_main()
        print("*** Deploy Containers **** ")
    elif choice == "4":
        sys.exit
    else:
        print("You must only select either 1, 2, 3, or 4.")
        print("Please try again")
        
def docker_install():
    remove_old_docker = subprocess.run("sudo apt-get remove docker docker-engine docker.io containerd runc", capture_output=True, shell=True)
    print("\n\n\n\n\n\n\n\n*** Removed older versions of Docker. *** \n")
    time.sleep(2)

    update = subprocess.run("sudo apt-get update", capture_output=True, shell=True)
    print ("*** Downloaded package information from all configured resources. *** \n")
    
    https_repo = subprocess.run("sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y", capture_output=True, shell=True)
    print ("*** Updated the apt index and install packages to allow apt to use a repository over HTTPS. ***\n")
    time.sleep(2)

    gpg_key = subprocess.run("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -", capture_output=True, shell=True)
    print ("*** Added Docker's official GPG key. *** \n")
    time.sleep(2)

    docker_repo = subprocess.run("sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable'", capture_output=True, shell=True)
    print ("*** Set up Docker's stable repository. *** \n")
    time.sleep(2)

    install = subprocess.run("sudo apt-get install docker-ce docker-ce-cli containerd.io", capture_output=True, shell=True)
    print ("*** Installed the latest version of Docker Engine. *** \n")
    time.sleep(2)

    docker_status = subprocess.run("sudo systemctl status docker", shell=True)
    print ("*** Docker installation completed! *** \n")
    main()

def stacks_main():
    print("\n Stack Deploy Menu \n")
    #time.sleep(1)
    print()

    choice = input("""                           
    
                                            1.   DevOps Stack
                                                    
                                                    Apache Guacamole        (clientless remote desktop)
                                                    GitLab                  (private repo, CI/CD pipeline)
                                                    Netdata                 (realtime server metrics)
                                                    Portainer               (GUI Docker manager)
                                                    Traefik                 (Reverse proxy & routing service)
                                                    Watchtower              (Keeps Docker images up-to-date)
                                                    Code-Server             (VS Code source code editor)
                                                    
                        
                                            2.   Data Stack
                                            
                                                    Duplicati               (Server and cloud backup service)
                                                    Bitwarden               (Selfhosted password manager)
                                                    Bookstack               (Wiki)
                                                    Calibre                 (eBooks library management)
                                                    Grocy                   (Grocery and household management)
                                                    Nextcloud               (cloud storage account)
                                                    

                                            3.   Media Stack
                                            
                                                    Airsonic                (music & podcast streaming service)
                                                    Fresh RSS               (RSS news reader)
                                                    Jackett                 (Torrent indexer)
                                                    Piwigo                  (Photo management)
                                                    Radarr                  (Movie torrent search)
                                                    Tautulli                (Media monitor)
                                                    QBittorrent             (Torrent client)
                                                    

                                            4.   Main Menu
                                            
                                            
                                            5.   Quit
                       
        Enter Stack No. : """)

    if choice == "1":
        devops_stack()
        print ("*** Deploying DevOps Stack *** \n")
    if choice == "2":
        data_stack()
        print ("*** Deploying Data Stack *** \n")
    if choice == "3":
        media_stack()
        print ("*** Deploying Media Stack *** \n")
    if choice == "M" or choice == "m":
        main()
    elif choice == "Q" or choice =="q":
        sys.exit

def devops_stack():
    mkdir_stack_dash = subprocess.run("sudo mkdir /opt/stack_dash/", capture_output=True, shell=True)
    print("\n\n\n\n\n\n\n\n*** Created stack_dash root folder in /opt/ directory. *** \n")
    time.sleep(2)

    mkdir_devops = subprocess.run("sudo mkdir /opt/stack_dash/devops", capture_output=True, shell=True)
    print ("*** Created DevOps folder in /opt/stack_dash directory. *** \n")
    
    dir_permissions = subprocess.run("sudo chmod 777 -R /opt/stack_dash/devops", capture_output=True, shell=True)
    print ("*** Corrected DevOps folder permissions. ***\n")
    time.sleep(2)
    
    print("\n DevOps Stack: Reverse Proxy by Traefik 2 \n")
    #time.sleep(1)
    choice = input(""" 
    
Do you want to include Traefik with your DevOps deployment?
              
   Type "yes" if you don't have Traefik and wish to deploy it with the DevOps Stack, or 
                                               
   Type "no" if you already have Traefik running and don't need to deploy it with DevOps Stack
                                 
Enter "yes" or "no" [or "m" to return to main menu; enter "q" to quit]:  """)
            
    if choice == "yes" or choice == "Yes":
        devops_traefik()
        print ("*** Deploying DevOps Standard Stack *** \n")
    if choice == "no" or choice == "No":
        devops_stand()
        print ("*** Deploying DevOps Stack with Traefik *** \n")
    if choice == "M" or choice == "m":
        main()
    elif choice == "Q" or choice =="q":
        sys.exit

def devops_traefik():
    make_proxy = subprocess.run("sudo docker network create proxy", capture_output=True, shell=True)
    print("\n\n\n\n\n\n\n\n*** Created Docker network: proxy. *** \n")
    time.sleep(2)

    mkdir_traefik = subprocess.run("sudo mkdir /opt/stack_dash/devops/traefik", capture_output=True, shell=True)
    print ("*** Created Traefik folder in /opt/stack_dash directory. *** \n")
    
    traefik_dir_permissions = subprocess.run("sudo chmod 777 -R /opt/stack_dash/devops/traefik", capture_output=True, shell=True)
    print ("*** Corrected Traefik folder permissions. ***\n")
    
    mkdir_traefik_rules = subprocess.run("sudo mkdir /opt/stack_dash/devops/traefik/rules", capture_output=True, shell=True)
    print ("*** Created Traefik Rules folder in /opt/stack_dash directory. *** \n")
    
    traefik_rules_permissions = subprocess.run("sudo chmod 777 -R /opt/stack_dash/devops/traefik/rules", capture_output=True, shell=True)
    print ("*** Corrected Traefik Rules folder permissions. ***\n")
    
    traefik_compose_copy = shutil.copy('./stacks/devops/traefik/docker-compose.yml', '/opt/stack_dash/devops/traefik')
    print ("*** Copied Traefik Docker Compose file to /opt/stack_dash/devops/traefik. ***\n")
    
    traefik_rules1_copy = shutil.copy('./stacks/devops/traefik/data/rules/middleware-chains.toml', '/opt/stack_dash/devops/traefik/rules')
    print ("*** Copied Traefik middleware-chain.toml to /opt/stack_dash/devops/traefik/rules. ***\n")
    
    traefik_rules2_copy = shutil.copy('./stacks/devops/traefik/data/rules/middlewares.toml', '/opt/stack_dash/devops/traefik/rules')
    print ("*** Copied Traefik data and middlewares.toml to /opt/stack_dash/devops/traefik/rules. ***\n")
    
    mkdir_gitlab = subprocess.run("sudo mkdir /opt/stack_dash/devops/gitlab", capture_output=True, shell=True)
    print ("*** Created GitLab folder in /opt/stack_dash directory. *** \n")
    
    gitlab_dir_permissions = subprocess.run("sudo chmod 777 -R /opt/stack_dash/devops/gitlab", capture_output=True, shell=True)
    print ("*** Corrected GitLab folder permissions. ***\n")
    
    mkdir_coder = subprocess.run("sudo mkdir /opt/stack_dash/devops/coder", capture_output=True, shell=True)
    print ("*** Created coder folder in /opt/stack_dash directory. *** \n")
    
    coder_dir_permissions = subprocess.run("sudo chmod 777 -R /opt/stack_dash/devops/coder", capture_output=True, shell=True)
    print ("*** Corrected coder folder permissions. ***\n")

    mkdir_portainer = subprocess.run("sudo mkdir /opt/stack_dash/devops/portainer", capture_output=True, shell=True)
    print ("*** Created Portainer folder in /opt/stack_dash directory. *** \n")
    
    portainer_dir_permissions = subprocess.run("sudo chmod 777 -R /opt/stack_dash/devops/portainer", capture_output=True, shell=True)
    print ("*** Corrected Portainer folder permissions. ***\n")
    
    mkdir_apache_guacamole = subprocess.run("sudo mkdir /opt/stack_dash/devops/apache_guacamole", capture_output=True, shell=True)
    print ("*** Created Apache Guacamole folder in /opt/stack_dash directory. *** \n")
    
    guacamole_dir_permissions = subprocess.run("sudo chmod 777 -R /opt/stack_dash/devops/apache_guacamole", capture_output=True, shell=True)
    print ("*** Corrected Portainer folder permissions. ***\n")
    
f = open('./stackdash/stacks/devops/traefik/.env', 'a+')
filedata = f.read()
c_email = filedata.replace("$C_EMAIL", input("[Cloudflare: 1/3] \n Please enter your Cloudflare Email Address, [Email address for Cloudflare account, located at https://dash.cloudflare.com, e.g., mail@example.com]:  ")
f.write(c_mail)
f.close() 

traefik_env_copy = shutil.copy('./stacks/devops/traefik/.env', '/opt/stack_dash/devops/traefik')
print ("*** Copied Traefik .env fie to /opt/stack_dash/devops/traefik. ***\n")

devops_traefik_compose = subprocess.run("docker-compose -f /opt/stack_dash/devops/traefik/docker-compose.yml up -d", capture_output=True, shell=True)
print ("*** Deployed DevOps with Traefik! ***\n")

main()
