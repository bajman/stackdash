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
    elif choice == "w" or choice == "W":
        containers_list()
        print("*** Container List **** ")
    elif choice == "c" or choice == "C":
        container_deploy()
        print("*** Deploy Containers **** ")
    elif choice == "t" or choice == "T":
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

def containers_list():
    print("""\n\n                                      
    
                                                                      Complete List of Images 
                                                                ===================================                                               
        ╔══════════════════════════════════════════════╦══════════════════════════════════════════════════════════════════════════════════════════════════╗
        ║             Image/Container Name             ║                                            Description                                           ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║    Airsonic  (Music & Podcast Management)    ║ Airsonic is a free, web-based media streamer, providing ubiquitous access to your                ║
        ║                                              ║ music. Use it to share your music with friends, or to listen to your own                         ║
        ║                                              ║ music while at work. You can stream to multiple players simultaneously, for                      ║
        ║                                              ║ instance to one player in your kitchen and another in your living room.                          ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║  Apache Guacamole  (Remote Desktop Gateway)  ║ Apache Guacamole is a clientless remote desktop gateway. It supports standard                    ║
        ║                                              ║ protocols like VNC, RDP, and SSH. This container is only the backend server                      ║
        ║                                              ║ component needed to use The official or 3rd party HTML5 frontends.                               ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║         Bitwarden  (Password Manager)        ║ Bitwarden is an open-source password management service that stores sensitive                    ║
        ║                                              ║ information such as website credentials in an encrypted vault. Bitwarden                         ║
        ║                                              ║ platform offers a variety of client applications including a web interface,                      ║
        ║                                              ║ desktop applications, browser extensions, mobile apps, and a CLI.                                ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║               Bookstack  (Wiki)              ║ BookStack is a simple, self-hosted, opinionated wiki system that provides a                      ║
        ║                                              ║ pleasant   and simple out of the box experience for organizing and storing information.          ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║          Calibre  (eBook Management)         ║ Calibre-web is a web app providing a clean interface for browsing, reading and                   ║
        ║                                              ║ downloading eBooks using an existing Calibre database. It is also possible to                    ║
        ║                                              ║ integrate google drive and edit metadata and your calibre library through the app itself.        ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║           Code-Server  (IDE Server)          ║ Visual Studio Code is a edit-build-debug code editor with comprehensive code                     ║
        ║                                              ║ editing, navigation, and understanding support along with lightweight                            ║
        ║                                              ║ debugging, a rich extensibility model, and lightweight integration with existing tools.          ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║ Duplicati  (Server and cloud backup service) ║ Duplicati is an automatic server backup service which backup options with                        ║
        ║                                              ║ local backup   options for most support standard protocols such as FTP,                          ║
        ║                                              ║ SSH, WebDAV and for   popular services like Microsoft OneDrive, Amazon Cloud                     ║
        ║                                              ║ Drive & S3, Google   Drive, box.com, Mega, hubiC and many others.                                ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║          Fresh RSS  (RSS Management)         ║ FreshRSS is a lightweight, multi-user application self-hosted RSS feed aggregator                ║
        ║                                              ║ like   Leed or Kriss Feed with support for custom tags, an API for (mobile) clients,             ║
        ║                                              ║ and a Command-Line Interface.                                                                    ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║   GitLab  (Private Source Code Repository)   ║ GitLab includes Git repository management, issue tracking, code review, an IDE,                  ║
        ║                                              ║ activity streams, and wikis. GitLab provides source collaboration and source                     ║
        ║                                              ║ control management to code, test, and deploy.                                                    ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║         Grocy  (Household Management)        ║ Grocey is a web-based self-hosted groceries & household management solution for                  ║
        ║                                              ║ your home. It allows you to track your purchases, automate & optimize                            ║
        ║                                              ║ your shopping list, waste less (by always knowing what is expiring next),                        ║
        ║                                              ║ lets you plan/manage meals, recipes, and household chores.                                       ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║  Jackett (Proxy Server -   Torrent Indexer)  ║ Jackett works as a proxy server: it translates queries from apps (Sonarr, SickRage,              ║
        ║                                              ║ CouchPotato, Mylar, etc) into tracker-site-specific http queries, parses the                     ║
        ║                                              ║ html response, then sends results back to the requesting software. This                          ║
        ║                                              ║ allows for getting recent uploads (like RSS) and performing searches.                            ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║         Netdata  (Server Monitoring)         ║ Netdata is distributed, real-time, performance and health monitoring for systems                 ║
        ║                                              ║ and applications. It is a highly optimized monitoring agent you install on                       ║
        ║                                              ║ all your systems and containers.                                                                 ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║         Nextcloud  (File Management)         ║ Nextcloud is a suite of client-server software for creating and using file hosting               ║
        ║                                              ║ services for. Similar to Dropbox, Office 365, or Google Drive, it can be used                    ║
        ║                                              ║ on home-local computers or for off-premises file storage. Nextcloud’s App                        ║
        ║                                              ║ Store contains over 200 extensions including calendars &  contacts (CardDAV),                    ║
        ║                                              ║ streaming media   (Ampache), document viewer tools, and external connections to                  ║
        ║                                              ║ Dropbox, Google   Drive, and Amazon.                                                             ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║          Piwigo  (Photo Management)          ║ Piwigo is a photo gallery software for the web that comes with powerful features                 ║
        ║                                              ║ to publish and manage your collection of pictures.                                               ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║           Plex  (Media Management)           ║ Plex organizes video, music and photos from personal media libraries and streams                 ║
        ║                                              ║ them to smart TVs, streaming boxes and mobile devices.                                           ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║       Portainer  (Docker Management UI)      ║ Portainer   allows you to manage your Docker stacks, containers, images, volumes, and            ║
        ║                                              ║ networks. It is compatible with the standalone Docker engine and with Docker Swarm.              ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║         QBittorrent  (Torrent Client)        ║ The   Qbittorrent project aims to provide an open-source software alternative to                 ║
        ║                                              ║ µTorrent. qBittorrent is based on the Qt toolkit and libtorrent-rasterbar library.               ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║              Radarr  (Movie PVR)             ║ Radarr   is a PVR for Usenet and BitTorrent users. It can monitor multiple RSS feeds             ║
        ║                                              ║ for movies and will grab, sort, and rename them. It can also be configured to                    ║
        ║                                              ║ automatically upgrade the quality of files already downloaded when a better-quality              ║
        ║                                              ║ format becomes available.                                                                        ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║         Tautulli  (Media Monitoring)         ║ Tautulli   is a 3rd party application that you can run alongside your Plex Media Server          ║
        ║                                              ║ to monitor activity and track various statistics. Most importantly, these statistics include     ║
        ║                                              ║ what has been watched, who watched it, when and where they   watched it, and how it was watched. ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║    Traefik  (Reverse Proxy & Loadbalencer)   ║ Traefik   is an edge router, meaning, it immediately and automatically, intercepts and           ║
        ║                                              ║ routes every incoming request to the appropriate running service.                                ║
        ╠══════════════════════════════════════════════╬══════════════════════════════════════════════════════════════════════════════════════════════════╣
        ║      Watchtower  (Docker Image Updater)      ║ Watchtower   is an application that will monitor your running Docker containers and watch        ║
        ║                                              ║ for changes to the images that those containers were originally started from.                    ║
        ║                                              ║ If watchtower detects that an image has changed, it will automatically restart                   ║
        ║                                              ║ the container using the new image.                                                               ║
        ╚══════════════════════════════════════════════╩══════════════════════════════════════════════════════════════════════════════════════════════════╝
    
    """)

def container_deploy():
    choice = input("""
    
                                           ==============================================================================
                                             __   ___  __        __          __   __       ___              ___  __   __  
                                            |  \ |__  |__) |    /  \ \ /    /  ` /  \ |\ |  |   /\  | |\ | |__  |__) /__` 
                                            |__/ |___ |    |___ \__/  |     \__, \__/ | \|  |  /~~\ | | \| |___ |  \ .__/ 
                                            ==============================================================================
    
                                                ╔══════════════════════════════════════════════╦══════════════════╗
                                                ║             Image/Container Name             ║ Container Number ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Airsonic  (Music & Podcast Management)       ║         1        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Apache Guacamole  (Remote Desktop Gateway)   ║         2        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Bitwarden  (Password Manager)                ║         3        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Bookstack  (Wiki)                            ║         4        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Calibre  (eBook Management)                  ║         5        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Code-Server  (IDE Server)                    ║         6        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Duplicati  (Server and cloud backup service) ║         7        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Fresh RSS  (RSS Management)                  ║         8        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ GitLab  (Private Source Code Repository)     ║         9        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Grocy  (Household Management)                ║        10        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Jackett (Proxy Server - Torrent Indexer)     ║        11        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Netdata  (Server Monitoring)                 ║        12        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Nextcloud  (File Management)                 ║        13        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Piwigo  (Photo Management)                   ║        14        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Plex  (Media Management)                     ║        15        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Portainer  (Docker Management UI)            ║        16        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ QBittorrent  (Torrent Client)                ║        17        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Radarr  (Movie PVR)                          ║        18        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Tautulli  (Media Monitoring)                 ║        19        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Traefik  (Reverse Proxy & Loadbalencer)      ║        20        ║
                                                ╠══════════════════════════════════════════════╬══════════════════╣
                                                ║ Watchtower  (Docker Image Updater)           ║        21        ║
                                                ╚══════════════════════════════════════════════╩══════════════════╝
                                                    
============================================================================================================================================================
                                                        Please enter your selection:                       """)
    if choice == "i" or choice == "I":
        docker_install()
        print("*** Install Docker Engine **** ")
    elif choice == "w" or choice == "W":
        containers_list()
        print("*** Container List **** ")
    elif choice == "c" or choice == "C":
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
    
                                                    ============================================================
                                                     __   ___  __        __          __  ___       __        __  
                                                    |  \ |__  |__) |    /  \ \ /    /__`  |   /\  /  ` |__/ /__` 
                                                    |__/ |___ |    |___ \__/  |     .__/  |  /~~\ \__, |  \ .__/ 
                                                    ============================================================
    
                                        ╔══════════════╦══════════════╦══════════════════╦═════════════════════════════════════╗
                                        ║ Stack Name   ║ Stack Number ║    Container     ║         Brief Description           ║
                                        ╠══════════════╬══════════════╬══════════════════╬═════════════════════════════════════╣
                                        ║    DevOps    ║     1        ║ Apache Guacamole ║ Clientless, remote desktop          ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ GitLab           ║ Private repo, CI/CD pipeline        ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Netdata          ║ Realtime server metrics             ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Portainer        ║ GUI Docker manager                  ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Traefik          ║ Reverse proxy & routing service     ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Watchtower       ║ Automatic Docker image updater      ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Code-Server      ║ Visual Studio IDE                   ║
                                        ╠══════════════╬══════════════╬══════════════════╬═════════════════════════════════════╣
                                        ║    Data      ║     2        ║ Duplicati        ║ Server backup service               ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Bitwarden        ║ Selfhosted password manager         ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Calibre          ║ eBooks library management           ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Grocy            ║ Grocery and household management    ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Nextcloud        ║ Cloud storage                       ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Bookstack        ║ Wiki                                ║
                                        ╠══════════════╬══════════════╬══════════════════╬═════════════════════════════════════╣
                                        ║    Media     ║     3        ║ Airsonic         ║ Music and podcast streaming service ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Fresh RSS        ║ RSS news reader                     ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Jackett          ║ Torrent indexer                     ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Piwigo           ║ Photo management                    ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Radarr           ║ Movie torrent search                ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Tautulli         ║ Media metrics                       ║
                                        ║              ║              ╠══════════════════╬═════════════════════════════════════╣
                                        ║              ║              ║ Qbittorrent      ║ Torrent client                      ║
                                        ╚══════════════╩══════════════╩══════════════════╩═════════════════════════════════════╝
                       
 ============================================================================================================================================================
                                                        Please enter your selection:                       """)

    if choice == "1":
        devops_env_write1()
    if choice == "2":
        data_stack()
    if choice == "3":
        media_stack()
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
    userdir = devops_env_file.write('USERDIR=/opt/stackdash\n')
    
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
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/", shell=True)
    print ("*** Corrected stackdash directory permissions. ***\n")
   
###CONTAINERS
#duplicati
def duplicati_env_write():
    duplicati_env_file = open("./containers/duplicati/.env", "w+")
    duplicati_env_file_data = duplicati_env_file.read()
    
    puid = duplicati_env_file.write('PUID=1000\n')
    pgid = duplicati_env_file.write('PGID=1000\n')
    userdir = duplicati_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Duplicati [e.g., duplicati-example.com]\n")
    user_domainname = duplicati_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the directory you would like to use for Duplicatis appdata\n")
    user_client_id = duplicati_env_file.write("DUPLICATI_DATA=" + input('Path for appdata: ') + "\n")

    duplicati_env_file.write(duplicati_env_file_data)
    duplicati_env_file.close()

    duplicati_env_migration()

def duplicati_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/duplicati', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/duplicati/', '/opt/stackdash/docker-appdata/duplicati', dirs_exist_ok=True)
    print ("*** Copied ./containers/duplicati/ from Git Clone to /opt/stackdash/docker-appdata/duplicati ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/duplicati", shell=True)
    print ("*** Corrected Duplicati directory permissions. ***\n")
    
def duplicati_compose():
    duplicati_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/duplicati/docker-compose.yml up -d', shell=True)
    print ("*** Duplicati is deployed! ***")
    
#airsonic

def airsonic_env_write():
    airsonic_env_file = open("./containers/airsonic/.env", "w+")
    airsonic_env_file_data = airsonic_env_file.read()
    
    puid = airsonic_env_file.write('PUID=1000\n')
    pgid = airsonic_env_file.write('PGID=1000\n')
    userdir = airsonic_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Airsonic [e.g., music-example.com]\n")
    user_domainname = airsonic_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the directory you would like to use for Airsonics appdata\n")
    user_client_id = airsonic_env_file.write("AIRSONIC_DATA=" + input('Path for appdata: ') + "\n")

    airsonic_env_file.write(airsonic_env_file_data)
    airsonic_env_file.close()

    airsonic_env_migration()

def airsonic_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/airsonic', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/airsonic/', '/opt/stackdash/docker-appdata/airsonic', dirs_exist_ok=True)
    print ("*** Copied ./containers/airsonic/ from Git Clone to /opt/stackdash/docker-appdata/airsonic ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/airsonic", shell=True)
    print ("*** Corrected airsonic directory permissions. ***\n")

    airsonic_compose()

def airsonic_compose():
    airsonic_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/airsonic/docker-compose.yml up -d', shell=True)
    print ("*** Airsonic is deployed! ***")

#apache guacamole

def guacamole_env_write():
    guacamole_env_file = open("./containers/guacamole/.env", "w+")
    guacamole_env_file_data = guacamole_env_file.read()
    
    puid = guacamole_env_file.write('PUID=1000\n')
    pgid = guacamole_env_file.write('PGID=1000\n')
    userdir = guacamole_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Apache Guacamole [e.g., remote-example.com]\n")
    user_domainname = guacamole_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the directory you would like to use for Apache Guacamoles appdata\n")
    user_client_id = guacamole_env_file.write("GUACAMOLE_DATA=" + input('Path for appdata: ') + "\n")

    print ("\nPlease enter a username for Apache Guacamoles MYSQL database\n")
    user_client_id = guacamole_env_file.write("GUACAMOLE_MYSQL_USERNAME=" + input('MYSQL Username: ') + "\n")

    print ("\nPlease enter a strong password for Apache Guacamoles MYSQL user\n")
    user_client_id = guacamole_env_file.write("GUACAMOLE_MYSQL_USER_PASSWORD=" + input('MYSQL User Password: ') + "\n")

    print ("\nPlease enter a strong password for Apache Guacamoles MYSQL root user\n")
    user_client_id = guacamole_env_file.write("GUACAMOLE_MYSQL_ROOT_PASSWORD=" + input('MYSQL Root Password: ') + "\n")

    guacamole_env_file.write(guacamole_env_file_data)
    guacamole_env_file.close()

    guacamole_env_migration()

def guacamole_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/guacamole', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/guacamole/', '/opt/stackdash/docker-appdata/guacamole', dirs_exist_ok=True)
    print ("*** Copied ./containers/guacamole/ from Git Clone to /opt/stackdash/docker-appdata/guacamole ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/guacamole", shell=True)
    print ("*** Corrected guacamole directory permissions. ***\n")

    guacamole_compose()

def guacamole_compose():
    guacamole_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/guacamole/docker-compose.yml up -d', shell=True)
    print ("*** guacamole is deployed! ***")
    
#Bitwarden


def bitwarden_env_write():
    bitwarden_env_file = open("./containers/bitwarden/.env", "w+")
    bitwarden_env_file_data = bitwarden_env_file.read()
    
    puid = bitwarden_env_file.write('PUID=1000\n')
    pgid = bitwarden_env_file.write('PGID=1000\n')
    userdir = bitwarden_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Bitwarden [e.g., pass-example.com]\n")
    user_domainname = bitwarden_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the directory you would like to use for Bitwardens appdata\n")
    user_client_id = bitwarden_env_file.write("BITWARDEN_DATA=" + input('Path for appdata: ') + "\n")

    bitwarden_env_file.write(bitwarden_env_file_data)
    bitwarden_env_file.close()

    bitwarden_env_migration()

def bitwarden_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/bitwarden', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/bitwarden/', '/opt/stackdash/docker-appdata/bitwarden', dirs_exist_ok=True)
    print ("*** Copied ./containers/bitwarden/ from Git Clone to /opt/stackdash/docker-appdata/bitwarden ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/bitwarden", shell=True)
    print ("*** Corrected Bitwarden directory permissions. ***\n")

    bitwarden_compose()

def bitwarden_compose():
    bitwarden_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/bitwarden/docker-compose.yml up -d', shell=True)
    print ("*** Bitwarden is deployed! ***")
    
 #Bookstack

def bookstack_env_write():
    bookstack_env_file = open("./containers/bookstack/.env", "w+")
    bookstack_env_file_data = bookstack_env_file.read()
    
    puid = bookstack_env_file.write('PUID=1000\n')
    pgid = bookstack_env_file.write('PGID=1000\n')
    userdir = bookstack_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Bookstack [e.g., wiki-example.com]\n")
    user_domainname = bookstack_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the directory you would like to use for Bookstacks appdata\n")
    user_client_id = bookstack_env_file.write("BOOKSTACK_DATA=" + input('Path for appdata: ') + "\n")

    print ("\nPlease enter a strong password for Bookstacks's MYSQL user\n")
    user_client_id = bookstack_env_file.write("BOOKSTACK_MYSQL_USER_PASSWORD=" + input('MYSQL User Password: ') + "\n")

    print ("\nPlease enter a strong password for Bookstacks's MYSQL root user\n")
    user_client_id = bookstack_env_file.write("BOOKSTACK_MYSQL_ROOT_PASSWORD=" + input('MYSQL Root Password: ') + "\n")

    bookstack_env_file.write(bookstack_env_file_data)
    bookstack_env_file.close()

    bookstack_env_migration()

def bookstack_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/bookstack', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/bookstack/', '/opt/stackdash/docker-appdata/bookstack', dirs_exist_ok=True)
    print ("*** Copied ./containers/bookstack/ from Git Clone to /opt/stackdash/docker-appdata/bookstack ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/bookstack", shell=True)
    print ("*** Corrected Bookstack directory permissions. ***\n")

    bookstack_compose()

def bookstack_compose():
    bookstack_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/bookstack/docker-compose.yml up -d', shell=True)
    print ("*** bookstack is deployed! ***")

 #calibre-web

def calibre_env_write():
    calibre_env_file = open("./containers/calibre/.env", "w+")
    calibre_env_file_data = calibre_env_file.read()
    
    puid = calibre_env_file.write('PUID=1000\n')
    pgid = calibre_env_file.write('PGID=1000\n')
    userdir = calibre_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Calibre-Web [e.g., books-example.com]\n")
    user_domainname = calibre_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the directory you would like to use for Calibre-Web's appdata\n")
    user_client_id = calibre_env_file.write("calibre_DATA=" + input('Path for appdata: ') + "\n")

    calibre_env_file.write(calibre_env_file_data)
    calibre_env_file.close()

    calibre_env_migration()

def calibre_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/calibre', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/calibre/', '/opt/stackdash/docker-appdata/calibre', dirs_exist_ok=True)
    print ("*** Copied ./containers/calibre/ from Git Clone to /opt/stackdash/docker-appdata/calibre ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/calibre", shell=True)
    print ("*** Corrected Calibre-Web's directory permissions. ***\n")

    calibre_compose()

def calibre_compose():
    calibre_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/calibre/docker-compose.yml up -d', shell=True)
    print ("*** Calibre-Wen is deployed! ***")
    
 #VS-Code Server

def codeserver_env_write():
    codeserver_env_file = open("./containers/codeserver/.env", "w+")
    codeserver_env_file_data = codeserver_env_file.read()
    
    puid = codeserver_env_file.write('PUID=1000\n')
    pgid = codeserver_env_file.write('PGID=1000\n')
    userdir = codeserver_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for VS Code-Server [e.g., codeexample.com]\n")
    user_domainname = codeserver_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the directory you would like to use for VS Code-Server's appdata\n")
    user_client_id = codeserver_env_file.write("CODE_SERVER_DATA=" + input('Path for appdata: ') + "\n")

    codeserver_env_file.write(codeserver_env_file_data)
    codeserver_env_file.close()

    codeserver_env_migration()

def codeserver_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/codeserver', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/codeserver/', '/opt/stackdash/docker-appdata/codeserver', dirs_exist_ok=True)
    print ("*** Copied ./containers/codeserver/ from Git Clone to /opt/stackdash/docker-appdata/codeserver ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/codeserver", shell=True)
    print ("*** Corrected VS Code-Server's directory permissions. ***\n")

    codeserver_compose()

def codeserver_compose():
    codeserver_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/codeserver/docker-compose.yml up -d', shell=True)
    print ("*** VS Code-Server is deployed! ***")
    
 #Fresh RSS

def freshrss_env_write():
    freshrss_env_file = open("./containers/freshrss/.env", "w+")
    freshrss_env_file_data = freshrss_env_file.read()
    
    puid = freshrss_env_file.write('PUID=1000\n')
    pgid = freshrss_env_file.write('PGID=1000\n')
    userdir = freshrss_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Fresh RSS [e.g., rss-example.com]\n")
    user_domainname = freshrss_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the directory you would like to use for Fresh RSS's appdata\n")
    user_client_id = freshrss_env_file.write("FRESH_RSS_DATA=" + input('Path for appdata: ') + "\n")

    freshrss_env_file.write(freshrss_env_file_data)
    freshrss_env_file.close()

    freshrss_env_migration()

def freshrss_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/freshrss', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/freshrss/', '/opt/stackdash/docker-appdata/freshrss', dirs_exist_ok=True)
    print ("*** Copied ./containers/freshrss/ from Git Clone to /opt/stackdash/docker-appdata/freshrss ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/freshrss", shell=True)
    print ("*** Corrected Fresh RSS's directory permissions. ***\n")

    freshrss_compose()

def freshrss_compose():
    freshrss_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/freshrss/docker-compose.yml up -d', shell=True)
    print ("*** Fresh RSS is deployed! ***")

#GitLab

def gitlab_env_write():
    gitlab_env_file = open("./containers/gitlab/.env", "w+")
    gitlab_env_file_data = gitlab_env_file.read()
    
    puid = gitlab_env_file.write('PUID=1000\n')
    pgid = gitlab_env_file.write('PGID=1000\n')
    userdir = gitlab_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for GitLab [e.g., gitlab-example.com]\n")
    user_domainname = gitlab_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the directory you would like to use for GitLabs appdata\n")
    user_client_id = gitlab_env_file.write("GITLAB_DATA=" + input('Path for appdata: ') + "\n")

    gitlab_env_file.write(gitlab_env_file_data)
    gitlab_env_file.close()

    gitlab_env_migration()

def gitlab_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/gitlab', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/gitlab/', '/opt/stackdash/docker-appdata/gitlab', dirs_exist_ok=True)
    print ("*** Copied ./containers/gitlab/ from Git Clone to /opt/stackdash/docker-appdata/gitlab ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/gitlab", shell=True)
    print ("*** Corrected GitLabs directory permissions. ***\n")

    gitlab_compose()

def gitlab_compose():
    gitlab_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/gitlab/docker-compose.yml up -d', shell=True)
    print ("*** GitLab is deployed! ***")
    
#Grocy

def grocy_env_write():
    grocy_env_file = open("./containers/grocy/.env", "w+")
    grocy_env_file_data = grocy_env_file.read()
    
    puid = grocy_env_file.write('PUID=1000\n')
    pgid = grocy_env_file.write('PGID=1000\n')
    userdir = grocy_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Grocy [e.g., grocy-example.com]\n")
    user_domainname = grocy_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the directory you would like to use for Grocys appdata\n")
    user_client_id = grocy_env_file.write("GROCY_DATA=" + input('Path for appdata: ') + "\n")

    grocy_env_file.write(grocy_env_file_data)
    grocy_env_file.close()

    grocy_env_migration()

def grocy_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/grocy', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/grocy/', '/opt/stackdash/docker-appdata/grocy', dirs_exist_ok=True)
    print ("*** Copied ./containers/grocy/ from Git Clone to /opt/stackdash/docker-appdata/grocy ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/grocy", shell=True)
    print ("*** Corrected Grocys directory permissions. ***\n")

    grocy_compose()

def grocy_compose():
    grocy_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/grocy/docker-compose.yml up -d', shell=True)
    print ("*** Grocy is deployed! ***")
    
 #Jackett

def jackett_env_write():
    jackett_env_file = open("./containers/jackett/.env", "w+")
    jackett_env_file_data = jackett_env_file.read()
    
    puid = jackett_env_file.write('PUID=1000\n')
    pgid = jackett_env_file.write('PGID=1000\n')
    userdir = jackett_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Jackett [e.g., jackett-example.com]\n")
    user_domainname = jackett_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the directory you would like to use for Jacketts appdata\n")
    user_client_id = jackett_env_file.write("JACKETT_DATA=" + input('Path for appdata: ') + "\n")

    print ("\nPlease enter the directory you would like to use for Jacketts download folder\n")
    user_client_id = jackett_env_file.write("JACKETT_DOWNLOAD=" + input('Path for downloads: ') + "\n")

    jackett_env_file.write(jackett_env_file_data)
    jackett_env_file.close()

    jackett_env_migration()

def jackett_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/jackett', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/jackett/', '/opt/stackdash/docker-appdata/jackett', dirs_exist_ok=True)
    print ("*** Copied ./containers/jackett/ from Git Clone to /opt/stackdash/docker-appdata/jackett ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/jackett", shell=True)
    print ("*** Corrected Jacketts directory permissions. ***\n")

    jackett_compose()

def jackett_compose():
    jackett_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/jackett/docker-compose.yml up -d', shell=True)
    print ("*** Jackett is deployed! ***")
    
#Netdata

def netdata_env_write():
    netdata_env_file = open("./containers/netdata/.env", "w+")
    netdata_env_file_data = netdata_env_file.read()
    
    puid = netdata_env_file.write('PUID=1000\n')
    pgid = netdata_env_file.write('PGID=1000\n')
    userdir = netdata_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Netdata [e.g., metrics-example.com]\n")
    user_domainname = netdata_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    netdata_env_file.write(netdata_env_file_data)
    netdata_env_file.close()

    netdata_env_migration()

def netdata_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/netdata', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/netdata/', '/opt/stackdash/docker-appdata/netdata', dirs_exist_ok=True)
    print ("*** Copied ./containers/netdata/ from Git Clone to /opt/stackdash/docker-appdata/netdata ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/netdata", shell=True)
    print ("*** Corrected Netdata's directory permissions. ***\n")

    netdata_compose()

def netdata_compose():
    netdata_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/netdata/docker-compose.yml up -d', shell=True)
    print ("*** Netdata is deployed! ***")
    
# Nextcloud

def nextcloud_env_write():
    nextcloud_env_file = open("./containers/nextcloud/.env", "w+")
    nextcloud_env_file_data = nextcloud_env_file.read()
    
    puid = nextcloud_env_file.write('PUID=1000\n')
    pgid = nextcloud_env_file.write('PGID=1000\n')
    userdir = nextcloud_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Nextcloud [e.g., metrics-example.com]\n")
    user_domainname = nextcloud_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the path you like to use to store Nextclouds appdata\n")
    user_domainname = nextcloud_env_file.write("NEXTCLOUD_DATA=" + input('Path to Nextcloud appdata: ') + "\n")

    print ("\nPlease enter the password you would like to use for Nextclouds MYSQL database\n")
    user_domainname = nextcloud_env_file.write("NEXTCLOUD_MYSQL_USER_PASSWORD=" + input('Nextcloud MYSQL Password: ') + "\n")

    print ("\nPlease enter the root password you would like to use for Nextclouds MYSQL database\n")
    user_domainname = nextcloud_env_file.write("NEXTCLOUD_MYSQL_ROOT_PASSWORD" + input('Nextcloud Root MYSQL Password: ') + "\n")

    print ("\nPlease enter a documents path you would like to use with Nextcloud\n")
    user_domainname = nextcloud_env_file.write("NEXTCLOUD_DOCUMENTS=" + input('Path to your documents: ') + "\n")

    print ("\nPlease enter a downloads path you would like to use with Nextcloud\n")
    user_domainname = nextcloud_env_file.write("NEXTCLOUD_DOWNLOADS=" + input('Path to your downloads: ') + "\n")

    print ("\nPlease enter a photos path you would like to use with Nextcloud\n")
    user_domainname = nextcloud_env_file.write("NEXTCLOUD_PHOTOS=" + input('Path to your photos: ') + "\n")

    nextcloud_env_file.write(nextcloud_env_file_data)
    nextcloud_env_file.close()

    nextcloud_env_migration()

def nextcloud_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/nextcloud', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/nextcloud/', '/opt/stackdash/docker-appdata/nextcloud', dirs_exist_ok=True)
    print ("*** Copied ./containers/nextcloud/ from Git Clone to /opt/stackdash/docker-appdata/nextcloud ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/nextcloud", shell=True)
    print ("*** Corrected Nextclouds directory permissions. ***\n")

    nextcloud_compose()

def nextcloud_compose():
    nextcloud_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/nextcloud/docker-compose.yml up -d', shell=True)
    print ("*** Nextcloud is deployed! ***")
    
    
## Piwigo


def piwigo_env_write():
    piwigo_env_file = open("./containers/piwigo/.env", "w+")
    piwigo_env_file_data = piwigo_env_file.read()
    
    puid = piwigo_env_file.write('PUID=1000\n')
    pgid = piwigo_env_file.write('PGID=1000\n')
    userdir = piwigo_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Piwigo [e.g., photos-example.com]\n")
    user_domainname = piwigo_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the path you like to use to store Piwigios appdata\n")
    user_domainname = piwigo_env_file.write("PIWIGO_DATA=" + input('Path to Piwigo appdata: ') + "\n")

    print ("\nPlease enter the password you would like to use for Piwigios MYSQL database\n")
    user_domainname = piwigo_env_file.write("PIWIGO_MYSQL_USER_PASSWORD=" + input('Piwigo MYSQL Password: ') + "\n")

    print ("\nPlease enter the root password you would like to use for Piwigios MYSQL database\n")
    user_domainname = piwigo_env_file.write("PIWIGO_MYSQL_ROOT_PASSWORD=" + input('piwigo Root MYSQL Password: ') + "\n")

    print ("\nPlease enter a photos path you would like to use with Piwigo\n")
    user_domainname = piwigo_env_file.write("PIWIGO_PHOTOS=" + input('Path to your photos: ') + "\n")

    piwigo_env_file.write(piwigo_env_file_data)
    piwigo_env_file.close()

    piwigo_env_migration()

def piwigo_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/piwigo', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/piwigo/', '/opt/stackdash/docker-appdata/piwigo', dirs_exist_ok=True)
    print ("*** Copied ./containers/piwigo/ from Git Clone to /opt/stackdash/docker-appdata/piwigo ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/piwigo", shell=True)
    print ("*** Corrected Piwigios directory permissions. ***\n")

    piwigo_compose()

def piwigo_compose():
    piwigo_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/piwigo/docker-compose.yml up -d', shell=True)
    print ("*** piwigo is deployed! ***")
 
#Plex

def plex_env_write():
    plex_env_file = open("./containers/plex/.env", "w+")
    plex_env_file_data = plex_env_file.read()
    
    puid = plex_env_file.write('PUID=1000\n')
    pgid = plex_env_file.write('PGID=1000\n')
    userdir = plex_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for plex [e.g., plex-example.com]\n")
    user_domainname = plex_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the path you like to use to store Plexs appdata\n")
    user_domainname = plex_env_file.write("PLEX_DATA=" + input('Path to Plex Appdata: ') + "\n")

    print ("\nPlease enter your Plex Claim Token [see plex.tv/claim]\n")
    user_domainname = plex_env_file.write("PLEX_CLAIM_TOKEN=" + input('Plex Claim Token: ') + "\n")

    print ("\nPlease enter the path you would like Plex to use for movie collection\n")
    user_domainname = plex_env_file.write("PLEX_MOVIES=" + input('Plex Movie Path: ') + "\n")

    print ("\nPlease enter the path you would like Plex to use for tv-show collection\n")
    user_domainname = plex_env_file.write("PLEX_TV=" + input('Plex TV Path: ') + "\n")

    print ("\nPlease enter the path you would like Plex to use for your photo collection\n")
    user_domainname = plex_env_file.write("PLEX_PHOTOS=" + input('Plex Photos Path: ') + "\n")

    print ("\nPlease enter the path you would like Plex to use for your music collection\n")
    user_domainname = plex_env_file.write("PLEX_MUSIC=" + input('Plex Music Path: ') + "\n")

    plex_env_file.write(plex_env_file_data)
    plex_env_file.close()

    plex_env_migration()

def plex_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/plex', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/plex/', '/opt/stackdash/docker-appdata/plex', dirs_exist_ok=True)
    print ("*** Copied ./containers/plex/ from Git Clone to /opt/stackdash/docker-appdata/plex ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/plex", shell=True)
    print ("*** Corrected Plexs directory permissions. ***\n")

    plex_compose()

def plex_compose():
    plex_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/plex/docker-compose.yml up -d', shell=True)
    print ("*** Plex is deployed! ***")
    
#Portainer

def portainer_env_write():
    portainer_env_file = open("./containers/portainer/.env", "w+")
    portainer_env_file_data = portainer_env_file.read()
    
    puid = portainer_env_file.write('PUID=1000\n')
    pgid = portainer_env_file.write('PGID=1000\n')
    userdir = portainer_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Portainer [e.g., portainer-example.com]\n")
    user_domainname = portainer_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the path you like to use to store Portainers appdata\n")
    user_domainname = portainer_env_file.write("PORTAINER_DATA=" + input('Path to Portainer Appdata: ') + "\n")

    portainer_env_file.write(portainer_env_file_data)
    portainer_env_file.close()

    portainer_env_migration()

def portainer_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/portainer', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/portainer/', '/opt/stackdash/docker-appdata/portainer', dirs_exist_ok=True)
    print ("*** Copied ./containers/portainer/ from Git Clone to /opt/stackdash/docker-appdata/portainer ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/portainer", shell=True)
    print ("*** Corrected Portainers directory permissions. ***\n")

    portainer_compose()

def portainer_compose():
    portainer_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/portainer/docker-compose.yml up -d', shell=True)
    print ("*** Portainer is deployed! ***")

#Qbittorrent

def qbit_env_write():
    qbit_env_file = open("./containers/qbit/.env", "w+")
    qbit_env_file_data = qbit_env_file.read()
    
    puid = qbit_env_file.write('PUID=1000\n')
    pgid = qbit_env_file.write('PGID=1000\n')
    userdir = qbit_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for QBittorrent [e.g., qbit-example.com]\n")
    user_domainname = qbit_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the path you like to use to store QBittorents appdata\n")
    user_domainname = qbit_env_file.write("QBIT_DATA=" + input('Path to QBittorrent appdata: ') + "\n")

    print ("\nPlease enter the path you like to use to for QBittorents main download directory\n")
    user_domainname = qbit_env_file.write("QBIT_DOWNLOADS=" + input('Path to QBittorents Download Path: ') + "\n")

    print ("\nPlease enter the path you would like QBittorrent to use for movie collection\n")
    user_domainname = qbit_env_file.write("QBIT_MOVIES=" + input('QBittorents Movie Path: ') + "\n")

    print ("\nPlease enter the path you would like QBittorrent to use for TV-show collection\n")
    user_domainname = qbit_env_file.write("QBIT_TV=" + input('QBittorents TV Path: ') + "\n")

    print ("\nPlease enter the path you would like QBittorrent to use for eBook collection\n")
    user_domainname = qbit_env_file.write("QBIT_BOOKS=" + input('QBittorents eBook Path: ') + "\n")

    qbit_env_file.write(qbit_env_file_data)
    qbit_env_file.close()

    qbit_env_migration()

def qbit_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/qbit', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/qbit/', '/opt/stackdash/docker-appdata/qbit', dirs_exist_ok=True)
    print ("*** Copied ./containers/qbit/ from Git Clone to /opt/stackdash/docker-appdata/qbit ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/qbit", shell=True)
    print ("*** Corrected QBittorents directory permissions. ***\n")

    qbit_compose()

def qbit_compose():
    qbit_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/qbit/docker-compose.yml up -d', shell=True)
    print ("*** qbit is deployed! ***")
                                                                                                                              
# Radarr
                                                                
def radarr_env_write():
    radarr_env_file = open("./containers/radarr/.env", "w+")
    radarr_env_file_data = radarr_env_file.read()
    
    puid = radarr_env_file.write('PUID=1000\n')
    pgid = radarr_env_file.write('PGID=1000\n')
    userdir = radarr_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Radarr [e.g., radarr-example.com]\n")
    user_domainname = radarr_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the path you like to use to store Radarrs appdata\n")
    user_domainname = radarr_env_file.write("RADARR_DATA=" + input('Path to Radarrs appdata: ') + "\n")

    print ("\nPlease enter the path you like to use to for Radarrs main download directory\n")
    user_domainname = radarr_env_file.write("RADARR_DOWNLOADS=" + input('Radarrs Download Path: ') + "\n")

    print ("\nPlease enter the path you would like Radarr to use for movie collection\n")
    user_domainname = radarr_env_file.write("RADARR_MOVIES=" + input('Radarrs Movie Path: ') + "\n")

    radarr_env_file.write(radarr_env_file_data)
    radarr_env_file.close()

    radarr_env_migration()

def radarr_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/radarr', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/radarr/', '/opt/stackdash/docker-appdata/radarr', dirs_exist_ok=True)
    print ("*** Copied ./containers/radarr/ from Git Clone to /opt/stackdash/docker-appdata/radarr ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/radarr", shell=True)
    print ("*** Corrected Radarrs directory permissions. ***\n")

    radarr_compose()

def radarr_compose():
    radarr_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/radarr/docker-compose.yml up -d', shell=True)
    print ("*** radarr is deployed! ***")
                                                                
## Tautulli
                                                                     
def tautulli_env_write():
    tautulli_env_file = open("./containers/tautulli/.env", "w+")
    tautulli_env_file_data = tautulli_env_file.read()
    
    puid = tautulli_env_file.write('PUID=1000\n')
    pgid = tautulli_env_file.write('PGID=1000\n')
    userdir = tautulli_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Tautulli [e.g., tautulli-example.com]\n")
    user_domainname = tautulli_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the path you like to use to store Tautullis appdata\n")
    user_domainname = tautulli_env_file.write("TAUTULLI_DATA=" + input('Tautullis appdata path: ') + "\n")

    tautulli_env_file.write(tautulli_env_file_data)
    tautulli_env_file.close()

    tautulli_env_migration()

def tautulli_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/tautulli', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/tautulli/', '/opt/stackdash/docker-appdata/tautulli', dirs_exist_ok=True)
    print ("*** Copied ./containers/tautulli/ from Git Clone to /opt/stackdash/docker-appdata/tautulli ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/tautulli", shell=True)
    print ("*** Corrected Tautullis directory permissions. ***\n")
                                                                       
    tautulli_compose()

def tautulli_compose():
    tautulli_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/tautulli/docker-compose.yml up -d', shell=True)
    print ("*** tautulli is deployed! ***")
                                                                     
# Traefik
                                                                       
def traefik_env_write():
    traefik_env_file = open("./containers/traefik/.env", "w+")
    traefik_env_file_data = traefik_env_file.read()
    
    puid = traefik_env_file.write('PUID=1000\n')
    pgid = traefik_env_file.write('PGID=1000\n')
    userdir = traefik_env_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Traefik [e.g., traefik-example.com]\n")
    user_domainname = traefik_env_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\nPlease enter the path you like to use to store Traefiks appdata\n")
    user_domainname = traefik_env_file.write("TRAEFIK_DATA=" + input('Traefiks appdata path: ') + "\n")

    print ("\nPlease enter your Cloudflare Email Address, [Email address associated with your Cloudflare account, see https://dash.cloudflare.com, e.g., mail@example.com]\n")
    user_domainname = traefik_env_file.write("TRAEFIK_CLOUDFLARE_EMAIL=" + input('Your Cloudflare email address: ') + "\n")

    print ("\nPlease enter your Cloudflare Global API Key, see dash.cloudflare.com: My Profile >  API Tokens > API Keys, e.g., bLa1boPhZL0VCerk35XWmbPCaCyWjDaCVx4cM]: Tokens > API Keys, e.g., bLa1boPhZL0VCerk35XWmbPCaCyWjDaCVx4cM]\n")
    user_domainname = traefik_env_file.write("TRAEFIK_CLOUDFLARE_API_KEY=" + input('Your Cloudflare API Key: ') + "\n")

    traefik_env_file.write(traefik_env_file_data)
    traefik_env_file.close()

    traefik_env_migration()

def traefik_env_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/traefik', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/traefik/', '/opt/stackdash/docker-appdata/traefik', dirs_exist_ok=True)
    print ("*** Copied ./containers/traefik/ from Git Clone to /opt/stackdash/docker-appdata/traefik ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/traefik", shell=True)
    print ("*** Corrected Traefiks directory permissions. ***\n")

    traefik_compose()

def traefik_compose():
    traefik_compose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/traefik/docker-compose.yml up -d', shell=True)
    print ("*** Traefik is deployed! ***")
                                                                     

# Google OAUTH
                                                                     
def oauthenv_write():
    oauthenv_file = open("./containers/traefik/.env", "w+")
    oauthenv_file_data = oauthenv_file.read()
    
    puid = oauthenv_file.write('PUID=1000\n')
    pgid = oauthenv_file.write('PGID=1000\n')
    userdir = oauthenv_file.write('USERDIR=/opt/stackdash\n')
    
    print ("\nPlease enter the subdomain you would like to use for Google OAuth 2.0 [e.g., oauth-example.com]\n")
    user_domainname = oauthenv_file.write("DOMAINNAME=" + input('Your Domain Name: ') + "\n")

    print ("\n[Google OAuth 2.0: 1/4]\nPlease enter your Google APIs Client-ID [e.g., MaCcXoD05h7EmkGXqN07G6TJjcTKJYMmpp8tXsdIsILYSp1IqrX.apps.googleusercontent.com]\n")
    user_client_id = devops_env_file.write("OAUTH_CLIENT_ID=" + input('Your Google API Client ID: ') + "\n")

    print ("\n[Google OAuth 2.0: 2/4]\nPlease enter your Google APIs Client-Secret [E.g., XB6RDMRDrcGAwi3hwdPIPKSr]\n")
    user_client_secret = devops_env_file.write("OAUTH_CLIENT_SECRET=" + input('Your Google API Client Secret: ') + "\n")

    print ("\n[Google OAuth 2.0: 3/4]\nPlease enter your Google APIs Secret [E.g., rKyKKgVl9IlzxUfg1CJmjZwj5zk5LMzo]\n")
    user_secret = devops_env_file.write("OAUTH_SECRET=" + input('Your Google API Secret: ') + "\n")
    
    print ("\n[Google OAuth 2.0: 4/4]\nPlease enter the Gmail address you used to sign-up with Google APIs, aka: the Whitelist Email Address [e.g., example@gmail.com]\n")
    user_whitelist = devops_env_file.write("OAUTH_WHITELIST=" + input('Your Google API Gmail Address: ') + "\n")

    oauthenv_file.write(oauthenv_file_data)
    oauthenv_file.close()

    oauthenv_migration()

def oauthenv_migration():   
    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")

    mkdir_stack_dash = subprocess.run('sudo mkdir /opt/stackdash/docker-appdata/traefik', shell=True)
    print ("*** Created /opt/stackdash/docker-appdata directory ***\n")
        
    stack_dash_dir_copy = shutil.copytree('./containers/traefik/', '/opt/stackdash/docker-appdata/traefik', dirs_exist_ok=True)
    print ("*** Copied ./containers/traefik/ from Git Clone to /opt/stackdash/docker-appdata/traefik ***\n")
      
    stack_dash_permissions = subprocess.run("sudo chmod 777 -R /opt/stackdash/docker-appdata/traefik", shell=True)
    print ("*** Corrected Traefiks directory permissions. ***\n")

    oauthcompose()

def oauthcompose():
    oauthcompose = subprocess.run('sudo docker-compose -f /opt/stackdash/docker-appdata/traefik/docker-compose.yml up -d', shell=True)
    print ("*** Traefik is deployed! ***")
                                                                     
main()
