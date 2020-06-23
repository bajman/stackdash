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
                ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ \n\n\n
StackDash is a python3 script, designed to automate Docker installation on Ubunutu and deploy container stacks 
with subdomain hosting. StackDash feautes include a docker-engine install script, docker containers/stack 
deployment wizard, and preconfigured container subdomain external access using HTTPS/TLS/OAuth 2.0.  \n\n\n
  +----------------------------------------------------------------------------------------------+
  |                                        StackDack Network                                     |
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
\n\n
           ==============================================================================
             __   ___  __        __          __   __       ___              ___  __   __  
            |  \ |__  |__) |    /  \ \ /    /  ` /  \ |\ |  |   /\  | |\ | |__  |__) /__` 
            |__/ |___ |    |___ \__/  |     \__, \__/ | \|  |  /~~\ | | \| |___ |  \ .__/ 
                                                                                                                                                          
            ==============================================================================
\n                                                                                                           
Type [w] for a complete list of web apps you can deploy with StackDash. 
Type [c] to deploy individual containers.
\n
                              
                    ============================================================
                     __   ___  __        __          __  ___       __        __  
                    |  \ |__  |__) |    /  \ \ /    /__`  |   /\  /  ` |__/ /__` 
                    |__/ |___ |    |___ \__/  |     .__/  |  /~~\ \__, |  \ .__/ 

                    ============================================================
\n
Type [u] for a complete list of stacks you can deploy with StackDash.
Type [s] for a complete list of web app subdomain aliases used by StackDash. 
Type [t] to deploy the Data, DevOps, or Media StackDash Stacks. 
\n\n
                                ============================== \n
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

print (""" 
============================================================================================================================================================
NOTE: CLOUDFARE DNS ONLY
-----------------------------------------------------------------------------------------------------------------------------------------------------------
This version of StackDash is configured to support only Cloudflare DNS-managed domains. Additional domain/hosting providers will be made available in future 
releases of StackDash. For a full list of planned DNS providers see: https://docs.traefik.io/https/acme/#providers.\n

If you have domain name (e.g., example.com hosted by GoDaddy or Google Cloud) and would like to make Cloudflare your default DNS manager, you need to add 
two DNS domain records to your a newly created Cloudflare account. For more information on adding vendor-specific records to your Cloudflare account, 
see: https://support.cloudflare.com/hc/en-us/articles/360020991331-Adding-vendor-specific-DNS-records-to-Cloudflare. Cloudflare can manage the DNS of 
domains hosted by Google Cloud, Amazon S3, Microsoft Azure, ClickFunnels, WPEngine, and Zoho. \n

If you do not have a domain, you can purchase one through Cloudflare (approx. $8.XX per year) at https://www.cloudflare.com/products/registrar/
============================================================================================================================================================
\n\n\n""")

def docker_install():
    remove_old_docker = subprocess.check_call("sudo apt-get remove docker docker-engine docker.io containerd runc", shell=True)
    print("\n\n\n\n\n\n\n\n*** Removed older versions of Docker. *** \n")

    update = subprocess.check_call("sudo apt-get update", shell=True)
    print ("*** Downloaded package information from all configured resources. *** \n")
    
    https_repo = subprocess.check_call("sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y", shell=True)
    print ("*** Updated the apt index and install packages to allow apt to use a repository over HTTPS. ***\n")

    gpg_key = subprocess.check_call("curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -", shell=True)
    print ("*** Added Docker's official GPG key. *** \n")

    docker_repo = subprocess.check_call("sudo add-apt-repository 'deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable'", shell=True)
    print ("*** Set up Docker's stable repository. *** \n")

    install = subprocess.check_call("sudo apt-get install docker-ce docker-ce-cli containerd.io", shell=True)
    print ("*** Installed the latest version of Docker Engine. *** \n")

    docker_status = subprocess.check_call("sudo systemctl status docker", shell=True)
    print ("*** Docker installation completed! *** \n")
    main()

def stacks_main():
    print("\n Stack Deploy Menu \n")
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
    mkdir_stack_dash = subprocess.run("sudo mkdir /opt/stack_dash/", shell=True)
    print("\n\n\n\n\n\n\n\n*** Created stack_dash root folder in /opt/ directory. *** \n")

    mkdir_devops = subprocess.run("sudo mkdir /opt/stack_dash/devops", shell=True)
    print ("*** Created DevOps folder in /opt/stack_dash directory. *** \n")
    
    dir_permissions = subprocess.check_call("sudo chmod 777 -R /opt/stack_dash/devops", shell=True)
    print ("*** Corrected DevOps folder permissions. ***\n")
    
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

def devops_dir():
    make_proxy = subprocess.run("sudo docker network create proxy", shell=True)
    print("\n\n\n\n\n\n\n\n*** Created Docker network: proxy. *** \n")

    mkdir_traefik = subprocess.run("sudo mkdir /opt/stack_dash/devops/traefik", shell=True)
    print ("*** Created Traefik folder in /opt/stack_dash directory. *** \n")
    
    traefik_dir_permissions = subprocess.check_call("sudo chmod 777 -R /opt/stack_dash/devops/traefik", shell=True)
    print ("*** Corrected Traefik folder permissions. ***\n")
    
    mkdir_traefik_rules = subprocess.run("sudo mkdir /opt/stack_dash/devops/traefik/rules", shell=True)
    print ("*** Created Traefik Rules folder in /opt/stack_dash directory. *** \n")
    
    traefik_rules_permissions = subprocess.check_call("sudo chmod 777 -R /opt/stack_dash/devops/traefik/rules", shell=True)
    print ("*** Corrected Traefik Rules folder permissions. ***\n")
    
    traefik_rules1_copy = shutil.copy('./stacks/devops/traefik/data/rules/middleware-chains.toml', '/opt/stack_dash/devops/traefik/rules')
    print ("*** Copied Traefik middleware-chain.toml to /opt/stack_dash/devops/traefik/rules. ***\n")
    
    traefik_rules2_copy = shutil.copy('./stacks/devops/traefik/data/rules/middlewares.toml', '/opt/stack_dash/devops/traefik/rules')
    print ("*** Copied Traefik data and middlewares.toml to /opt/stack_dash/devops/traefik/rules. ***\n")
    
    mkdir_gitlab = subprocess.run("sudo mkdir /opt/stack_dash/devops/gitlab", shell=True)
    print ("*** Created GitLab folder in /opt/stack_dash directory. *** \n")
    
    gitlab_dir_permissions = subprocess.check_call("sudo chmod 777 -R /opt/stack_dash/devops/gitlab", shell=True)
    print ("*** Corrected GitLab folder permissions. ***\n")
    
    mkdir_coder = subprocess.run("sudo mkdir /opt/stack_dash/devops/coder", shell=True)
    print ("*** Created coder folder in /opt/stack_dash directory. *** \n")
    
    coder_dir_permissions = subprocess.check_call("sudo chmod 777 -R /opt/stack_dash/devops/coder", shell=True)
    print ("*** Corrected coder folder permissions. ***\n")

    mkdir_portainer = subprocess.run("sudo mkdir /opt/stack_dash/devops/portainer", shell=True)
    print ("*** Created Portainer folder in /opt/stack_dash directory. *** \n")
    
    portainer_dir_permissions = subprocess.check_call("sudo chmod 777 -R /opt/stack_dash/devops/portainer", shell=True)
    print ("*** Corrected Portainer folder permissions. ***\n")
    
    mkdir_apache_guacamole = subprocess.run("sudo mkdir /opt/stack_dash/devops/apache_guacamole", shell=True)
    print ("*** Created Apache Guacamole folder in /opt/stack_dash directory. *** \n")
    
    guacamole_dir_permissions = subprocess.check_call("sudo chmod 777 -R /opt/stack_dash/devops/apache_guacamole", shell=True)
    print ("*** Corrected Portainer folder permissions. ***\n")
    
def devops_traefik():
    traefik_env_copy = shutil.copy('./stacks/devops/traefik/.env', '/opt/stack_dash/devops/traefik')
    print ("*** Copied Traefik .env fie to /opt/stack_dash/devops/traefik. ***\n")
    devops_env = open("/opt/stack_dash/devops/traefik/.env", "a+")
    c_email = devops_env.write((input("[Cloudflare – 1/3] \n Please enter your Cloudflare Email Address, [Email address for Cloudflare account, located at https://dash.cloudflare.com, e.g., mail@example.com]:  "  )))
   
    new_lines = []
    with open('devops_env', 'a+') as f:
        for line in f:
            if 'CF_API_EMAIL=' in line:
                new_lines.append(line.replace('C_EMAIL', 'c_email'))

    with open('devops_env', 'a+') as f:
        f.write('\n'.join(new_lines))

    devops_env.close()
   

main()
