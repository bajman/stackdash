#!/usr/bin/env python3.8
import sys #this allows you to use the sys.exit command to quit/logout of the application
import subprocess
import time
import sys
import shutil
import os
import string


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
with subdomain hosting. StackDash feautes a docker-engine install script, a docker containers/stack 
deployment wizard, and preconfigured external access using HTTPS/TLS/OAuth 2.0.  \n\n\n
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
        devops_env()
    if choice == "2":
        data_stack()
    if choice == "3":
        media_stack()
    if choice == "M" or choice == "m":
        main()
    elif choice == "Q" or choice =="q":
        sys.exit

def devops_env():
    
    choice = input("""
    
Do you want to include Traefik with your DevOps deployment?
              
   Type "YES" if you want to deploy the DevOps Stack with Traefik 2
                                               
   Type "NO" if you already have a proxy running and don't need to deploy the DevOps Stack with Traefik 2 
                                 
[Or enter "m" to return to the main menu or enter "q" to quit]: """)
            
    if choice == "yes" or choice == "Yes":
        devops_env_write1()
    if choice == "no" or choice == "No":
        devops_stand()
    if choice == "M" or choice == "m":
        main()
    elif choice == "Q" or choice =="q":
        sys.exit
    
def devops_env_write1():

#writing base variables
    devops_env_file = open("./stacks/devops/traefik/devops.env", "w+")
    devops_env_file_data = devops_env_file.read()
    
    puid = devops_env_file.write('PUID=1000\n')
    pgid = devops_env_file.write('PGID=1000\n')
    userdir = devops_env_file.write('USERDIR=/opt/stack_dash\n')
    
    print ("\n\n\n[Cloudflare: 1/3]\nPlease enter your Cloudflare Email Address, [Email address for Cloudflare account, located at https://dash.cloudflare.com, e.g., mail@example.com]\n")
    user_c_email = devops_env_file.write("CF_API_EMAIL=" + input('Your Cloudflare Email: ') + "\n")
    
    print ("\n[Cloudflare: 2/3]\nPlease enter your Cloudflare Global API Key, [See dash.cloudflare.com: My Profile >  API Tokens > API Keys, e.g., bLa1boPhZL0VCerk35XWmbPCaCyWjDaCVx4cM]: Tokens > API Keys, e.g., bLa1boPhZL0VCerk35XWmbPCaCyWjDaCVx4cM]\n")
    user_c_api = devops_env_file.write("CF_API_KEY=" + input('Your Cloudflare Global API Key: ') + "\n")

    print ("\n[Cloudflare: 3/3]\nPlease enter the domain name you would like to use for the DevOps Stack [e.g., devops-example.com]\n")
    user_domainname = devops_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\n[Google OAuth 2.0: 1/4]\nPlease enter your Google APIs Client-ID [e.g., MaCcXoD05h7EmkGXqN07G6TJjcTKJYMmpp8tXsdIsILYSp1IqrX.apps.googleusercontent.com]\n")
    user_client_id = devops_env_file.write("CLIENT_ID=" + input('Your Google API Client ID: ') + "\n")

    print ("\n[Google OAuth 2.0: 2/4]\nPlease enter your Google APIs Client-Secret [E.g., XB6RDMRDrcGAwi3hwdPIPKSr]\n")
    user_client_secret = devops_env_file.write("CLIENT_SECRET=" + input('Your Google API Client Secret: ') + "\n")

    print ("\n[Google OAuth 2.0: 3/4]\nPlease enter your Google APIs Secret [E.g., rKyKKgVl9IlzxUfg1CJmjZwj5zk5LMzo]\n")
    user_secret = devops_env_file.write("SECRET=" + input('Your Google API Secret: ') + "\n")
    
    print ("\n[Google OAuth 2.0: 4/4]\nPlease enter the Gmail address you used to sign-up with Google APIs, aka: the Whitelist Email Address [e.g., example@gmail.com]\n")
    user_whitelist = devops_env_file.write("WHITELIST=" + input('Your Google API Gmail Address: ') + "\n")

    devops_env_file.write(devops_env_file_data)
    devops_env_file.close()

    devops_env_migration()

def devops_env_migration():
    make_proxy = subprocess.run("sudo docker network create proxy", shell=True)
    print("\n\n*** Created Docker network: proxy. *** \n")
    
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/', shell=True)
    print ("*** Created /opt/stackdash/ directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./stacks/', '/opt/stackdash/', dirs_exist_ok=True)
    print ("*** Copied ./stacks/ from Git Clone to /opt/stackdash/ ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stack_dash/", shell=True)
    print ("*** Corrected stackdash directory permissions. ***\n")

main()
