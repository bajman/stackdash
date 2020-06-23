#!/usr/bin/env python3.8
import sys #this allows you to use the sys.exit command to quit/logout of the application
import subprocess
import time
import sys
import shutil
import os
import string


def main():
    choice = input("""                           
                                              ███████╗████████╗ █████╗  ██████╗██╗  ██╗    ██████╗  █████╗ ███████╗██╗  ██╗
                                              ██╔════╝╚══██╔══╝██╔══██╗██╔════╝██║ ██╔╝    ██╔══██╗██╔══██╗██╔════╝██║  ██║
                                              ███████╗   ██║   ███████║██║     █████╔╝     ██║  ██║███████║███████╗███████║
                                              ╚════██║   ██║   ██╔══██║██║     ██╔═██╗     ██║  ██║██╔══██║╚════██║██╔══██║
                                              ███████║   ██║   ██║  ██║╚██████╗██║  ██╗    ██████╔╝██║  ██║███████║██║  ██║
                                              ╚══════╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ v0.13 \n\n\n
StackDash is a python3 script designed to automate Docker installation on Ubuntu and deploy container stacks with subdomain hosting. StackDash features a 
Docker-Engine install script and Docker web-app containers/stack deployment wizards. All StackDash containers/stacks are preconfigured for external, subdomain 
access, using LetsEncrypt HTTPS/TLS and OAuth 2.0 SSO via the Google Cloud Platform. See the Documentation for installation instructions. \n

This version of StackDash is configured to support only Cloudflare DNS-managed domains. Additional domain/hosting providers will be made available in future 
releases of StackDash. For a full list of planned DNS providers see: https://docs.traefik.io/https/acme/#providers.\n
\n
                                                        Type [i] to install Docker-Engine CE via HTTPS. \n
                                           ==============================================================================
                                             __   ___  __        __          __   __       ___              ___  __   __  
                                            |  \ |__  |__) |    /  \ \ /    /  ` /  \ |\ |  |   /\  | |\ | |__  |__) /__` 
                                            |__/ |___ |    |___ \__/  |     \__, \__/ | \|  |  /~~\ | | \| |___ |  \ .__/ 

                                            ==============================================================================
                                        \n                                                                                                           
                                                Type [c] to deploy individual StackDash Containers.
                                                Type [w] for a complete list of web apps you can deploy with StackDash. 
                                        \n
                                                    ============================================================
                                                     __   ___  __        __          __  ___       __        __  
                                                    |  \ |__  |__) |    /  \ \ /    /__`  |   /\  /  ` |__/ /__` 
                                                    |__/ |___ |    |___ \__/  |     .__/  |  /~~\ \__, |  \ .__/ 

                                                    ============================================================
                                        \n
                                                Type [t] to deploy StackDash Stacks. 
                                                Type [u] for a complete list of stacks you can deploy with StackDash.
                                        \n

                                                                          StackDack Network
                                                                ===================================

                                                                       +----------------------------------------------------+   
                                                                       |                                                    |   
                                      +------------+     OAuth 2.0     | +-----------------+   HTTPS/TLS  +---------------+ |   
                                      |            |    Google API     | |                | | LetsEncrypt |               | |   
                                      |            +-------------------> |    TRAEFIK 2   +--------------->     SERVER    | |   
                                      |  INTERNET  <-------------------| |     (Proxy)    <--------------+     (Docker)   | |   
                                      |            | Exposed Port Nos: | |                | Proxy Routing |               | |   
                                      |            |       80;443      | |                | Rules-Traefik |               | |   
                                      +------------+                   | +-----------------+              +---------------+ |   
                                                                       |                                                    |   
                                                                       +----------------------------------------------------+   
                                                                                         INTERNAL NETWORK         
                                        \n
                                                Type [s] for a complete list of web app subdomain aliases used by StackDash. 
                                        \n

============================================================================================================================================================
                                                        Please enter your choice:                       """)
    if choice == "i" or choice == "I":
        docker_install()
        print("*** Install Docker Engine **** ")
    if choice == "w" or choice "W":
        containers_list()
        print("*** Container List **** ")
    elif choice == "c" or choice "C":
        container_deploy()
        print("*** Deploy Containers **** ")
    elif choice == "3":
        containers_main()
        print("*** Deploy Containers **** ")
    elif choice == "4":
        sys.exit
    else:
        print("You must only select either 1, 2, 3, or 4.")
        print("Please try again")

def containers_list():
    print(""""                                              List of supported Web Apps StackDash (v0.13)
    
Airsonic  (Music & Podcast Management)

    Airsonic is a free, web-based media streamer, providing ubiquitous access to your music. Use it to share your music with friends, or to listen to your own 
    music while at work. You can stream to multiple players simultaneously, for instance to one player in your kitchen and another in your living room.
    
Apache Guacamole  (Remote Desktop Gateway)

    Apache Guacamole is a clientless remote desktop gateway. It supports standard protocols like VNC, RDP, and SSH. This container is only the backend 
    server component needed to use The official or 3rd party HTML5 frontends.
    
Bitwarden  (Password Manager)

    Bitwarden is an open-source password management service that stores sensitive information such as website credentials in an encrypted vault. 
    The Bitwarden platform offers a variety of client applications including a web interface, desktop applications, browser extensions, mobile apps, and a CLI.
    
Bookstack  (Wiki)

    BookStack is a simple, self-hosted, opinionated wiki system that provides a pleasant and simple out of the box experience for organizing 
    and storing information. 
    
Calibre  (eBooks Management)

    Calibre-web is a web app providing a clean interface for browsing, reading and downloading eBooks using an existing Calibre database. 
    It is also possible to integrate google drive and edit metadata and your calibre library through the app itself.
    
Code-Server  (IDE Server)

    Virtual Studio Code is a edit-build-debug code editor with comprehensive code editing, navigation, and understanding support along with 
    lightweight debugging, a rich extensibility model, and lightweight integration with existing tools.
    
Duplicati  (Server and cloud backup service)

    Duplicati is an automatic server backup service which backup options with local backup options for most support standard protocols 
    such as FTP, SSH, WebDAV and for popular services like Microsoft OneDrive, Amazon Cloud Drive & S3, Google Drive, box.com, Mega, hubiC and many others.
    
Fresh RSS  (RSS Management)

    FreshRSS is a lightweight, multi-user application self-hosted RSS feed aggregator like Leed or Kriss Feed with support for custom tags, an API 
    for (mobile) clients, and a Command-Line Interface.
    
GitLab  (Private Code Repository)

    GitLab includes Git repository management, issue tracking, code review, an IDE, activity streams, and wikis. GitLab provides source collaboration 
    and source control management to code, test, and deploy. More details on features can be found on https://about.gitlab.com/features/.
    
Grocy  (Household Management)

    Grocey is a web-based self-hosted groceries & household management solution for your home. It allows you to track your purchases, automate & optimize 
    your shopping list, waste less (by always knowing what is expiring next), lets you plan/manage meals, recipes, and household chores.
    
Jackett (Proxy Server - Torrent Indexer)

    Jackett works as a proxy server: it translates queries from apps (Sonarr, SickRage, CouchPotato, Mylar, etc) into tracker-site-specific http queries, 
    parses the html response, then sends results back to the requesting software. This allows for getting recent uploads (like RSS) and performing searches. 
    Jackett is a single repository of maintained indexer scraping & translation logic - removing the burden from other apps.
    
Netdata  (Server Monitoring)

    Netdata is distributed, real-time, performance and health monitoring for systems and applications. It is a highly optimized monitoring agent 
    you install on all your systems and containers.
    
Nextcloud  (File Management)

    Nextcloud is a suite of client-server software for creating and using file hosting services for. Similar to Dropbox, Office 365, or Google Drive, 
    it can be used on home-local computers or for off-premises file storage. Nextcloud’s App Store contains over 200 extensions including calendars & 
    contacts (CardDAV), streaming media (Ampache), document viewer tools, and external connections to Dropbox, Google Drive, and Amazon. 
    
Piwigo  (Photo Management)

    Piwigo is a photo gallery software for the web that comes with powerful features to publish and manage your collection of pictures.
    
Plex  (Media Management)

    Plex organizes video, music and photos from personal media libraries and streams them to smart TVs, streaming boxes and mobile devices. 
    This container is packaged as a standalone Plex Media Server.
    
Portainer  (Docker Management UI)

    Portainer allows you to manage your Docker stacks, containers, images, volumes, and networks. It is compatible with the standalone 
    Docker engine and with Docker Swarm.
    
QBittorrent  (Torrent Client)

    The Qbittorrent project aims to provide an open-source software alternative to µTorrent. qBittorrent is based on the Qt toolkit and 
    libtorrent-rasterbar library.
    
Radarr  (Movie PVR)

    Radarr is a PVR for Usenet and BitTorrent users. It can monitor multiple RSS feeds for movies and will grab, sort, and rename them. 
    It can also be configured to automatically upgrade the quality of files already downloaded when a better-quality format becomes available.
    
Tautulli  (Media Monitoring)

    Tautulli is a 3rd party application that you can run alongside your Plex Media Server to monitor activity and track various statistics. 
    Most importantly, these statistics include what has been watched, who watched it, when and where they watched it, and how it was watched.
    
Traefik  (Reverse Proxy & Loadbalencer)

    Traefik is an edge router, meaning, it immediately and automatically, intercepts and routes every incoming request to the appropriate running service. 
    
Watchtower  (Docker Image Updater)

    Watchtower is an application that will monitor your running Docker containers and watch for changes to the images that those containers were 
    originally started from. If watchtower detects that an image has changed, it will automatically restart the container using the new image.
    
    """)

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
