#!/usr/bin/env python3.8
import sys #this allows you to use the sys.exit command to quit/logout of the application
import subprocess
import time
import sys
import shutil


def main():
    print("\n\n\n\n StackDash v.1.0 \n")
    #time.sleep(1)
    print(" ")

    choice = input("""                           Main Menu


    Supported 64-bit versions of Ubuntu:
     -Ubuntu Focal 20.04 LTS
     -Ubuntu Eoan 19.10
     -Ubuntu Bionic 18.04 LTS
     -Ubuntu Xenial 16.04 LTS
    
    
    
                                            1.   Install Docker Engine
                        
                                            2.   Deploy Docker Stacks (multiple containers)

                                            3.   Deploy Docker Containers (individual containers)

                                            4.   Quit
                        

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
                                 
            Enter "yes" or "no" [enter "m" to return to main menu; enter "q" to quit]:  """)
            
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
    
    traefik_env_copy = shutil.copy('./stacks/devops/traefik/.env', '/opt/stack_dash/devops/traefik')
    print ("*** Copied Traefik .env fie to /opt/stack_dash/devops/traefik. ***\n")
    
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
    
#env. variable inputs
devops_env = open("/opt/stack_dash/devops/traefik/.env" "a")
devops_env.write((input("CF_API_EMAIL=mail@example.com  "  )))
devops_env.write((input("CF_API_KEY=1234  "  )))
devops_env.write((input("DOMAINNAME=example.com  "  )))
devops_env.write((input("CLIENT_ID=912941924  "  )))
devops_env.write((input("CLIENT_SECRET=12315415  "  )))
devops_env.write((input("SECRET= " )))
devops_env.write((input("WHITELIST= " )))

# Docker Compose
devops_traefik_compose = subprocess.run("docker-compose -f /opt/stack_dash/devops/traefik/docker-compose.yml up -d", capture_output=True, shell=True)
print ("*** Deployed DevOps with Traefik! ***\n")

main()
