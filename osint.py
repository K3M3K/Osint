import subprocess
from colorama import Fore, Style
import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Style
import socket
import urllib.parse
import os
import ssl
import netifaces

def osint_tools_menu():
    print("Menu:")
    print("1. Osint Tools")
    print("2. Exit")

def create_banner():
    banner = f'''
{Fore.RED}    
 ███▄ ▄███▓ ██▀███        ▒█████   █     █░ ██▓    
▓██▒▀█▀ ██▒▓██ ▒ ██▒     ▒██▒  ██▒▓█░ █ ░█░▓██▒    
▓██    ▓██░▓██ ░▄█ ▒     ▒██░  ██▒▒█░ █ ░█ ▒██░    
▒██    ▒██ ▒██▀▀█▄       ▒██   ██░░█░ █ ░█ ▒██░    
▒██▒   ░██▒░██▓ ▒██▒ ██▓ ░ ████▓▒░░░██▒██▓ ░██████▒
░ ▒░   ░  ░░ ▒▓ ░▒▓░ ▒▓▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒  ░ ▒░▓  ░ 
░  ░      ░  ░▒ ░ ▒░ ░▒    ░ ▒ ▒░   ▒ ░ ░  ░ ░ ▒  ░
░      ░     ░░   ░  ░   ░ ░ ░ ▒    ░   ░    ░ ░   
       ░      ░       ░      ░ ░      ░        ░  ░ 
{Style.RESET_ALL} 
Osint Tools Script | This code was created with MR.0WL|
Author : MR.0WL
''' 
    return banner

def call_osint():
    try:
        osint_tools()
    except Exception as e:
        print(f"Failed to run osint tools: {e}")

def osint_tools():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(create_banner())
        osint_tools_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("Launching osint tools...")
            break
        elif choice == "2":
            print("Exiting program...")
            sys.exit()  
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    call_osint()


def create_banner():
    banner = f'''
{Fore.RED}    
 ███▄ ▄███▓ ██▀███        ▒█████   █     █░ ██▓    
▓██▒▀█▀ ██▒▓██ ▒ ██▒     ▒██▒  ██▒▓█░ █ ░█░▓██▒    
▓██    ▓██░▓██ ░▄█ ▒     ▒██░  ██▒▒█░ █ ░█ ▒██░    
▒██    ▒██ ▒██▀▀█▄       ▒██   ██░░█░ █ ░█ ▒██░    
▒██▒   ░██▒░██▓ ▒██▒ ██▓ ░ ████▓▒░░░██▒██▓ ░██████▒
░ ▒░   ░  ░░ ▒▓ ░▒▓░ ▒▓▒ ░ ▒░▒░▒░ ░ ▓░▒ ▒  ░ ▒░▓  ░ 
░  ░      ░  ░▒ ░ ▒░ ░▒    ░ ▒ ▒░   ▒ ░ ░  ░ ░ ▒  ░
░      ░     ░░   ░  ░   ░ ░ ░ ▒    ░   ░    ░ ░   
       ░      ░       ░      ░ ░      ░        ░  ░ 
{Style.RESET_ALL} 
Osint Tools Script | This code was created with MR.0WL|
Author : MR.0WL
'''
    return banner

def clean_and_format_url(url):
    
    url_components = urllib.parse.urlparse(url)
    cleaned_url = urllib.parse.urlunparse(url_components)
    return cleaned_url


def get_ssl_info(domain_name):
    context = ssl.create_default_context()
    with socket.create_connection((domain_name, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=domain_name) as ssock:
            return ssock.version(), ssock.cipher()

def check_security(domain_name):
    try:
        response = requests.get("https://" + domain_name)
        if response.status_code == 200:
            print("Security Information:")
            print("SSL/TLS Protocol:", response.connection.version)
            print("SSL Certificate:", response.connection.cipher)
        else:
            print("Security Information: Unable to retrieve security details")
    except Exception as e:
        print("Security Information: Unable to retrieve security details")


def search_google(query, num_results=25):
    url = "https://www.google.com/search"
    params = {"q": query, "num": num_results}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    try:
        response = requests.get(url, params=params, headers=headers)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Failed to make request: {e}")
        return None

    soup = BeautifulSoup(response.text, "html.parser")
    results = []
    for g in soup.find_all('div', class_='g'):
        title = g.find('h3').text
        link = g.find('a')['href']
        snippet_tag = g.find(class_='VwiC3b')
        snippet = snippet_tag.text if snippet_tag else ""
        results.append({"title": title, "link": link, "snippet": snippet})
        
    return results

def search_by_name():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(create_banner())
        print("\nOptions:")
        print("[1] Continue searching by name")
        print("[2] Return to main menu")

        choice = input("Choose an option: ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(create_banner())  
            query = input("\nSearch By Name: ")
            print("Searching...")

            results = search_google(query)

            if results:
                print("\nResults:")
                for i, item in enumerate(results, start=1):
                    print(f"\nResult #{i}:")
                    print(f"Title: {item['title']}")
                    print(f"Link: {item['link']}")
                    print(f"Snippet: {item['snippet']}")
                    cleaned_url = clean_and_format_url(item['link'])
                    print(f"Cleaned URL: {cleaned_url}")

            else:
                print("No results found.")

            input("Press Enter to continue...")
        elif choice == '2':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice. Please try again.")

            
def search_social_media():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(create_banner())
        print("\nOptions:")
        print("[1] Continue searching social media")
        print("[2] Return to main menu")

        choice = input("Choose an option: ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(create_banner()) 
            query = input("\nSearch Social Media: ")
            print("Searching...")

            results = search_google(query)

            if results:
                print("\nResults:")
                for i, item in enumerate(results, start=1):
                    print(f"\nResult #{i}:")
                    print(f"Title: {item['title']}")
                    print(f"Link: {item['link']}")
                    print(f"Snippet: {item['snippet']}")
            else:
                print("No results found for social media accounts.")

            input("Press Enter to continue...")
        elif choice == '2':
            print("Returning to the main menu...")
            break
        else:
            print("Invalid choice. Please try again.")
            
def search_with_operator():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(create_banner())
        print("\nOptions:")
        print("[1] Continue scanning")
        print("[2] Return to recognition menu")

        choice = input("Choose an option: ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(create_banner())
            print("Continuing scanning...")
        elif choice == '2':
            print("Returning to recognition menu...")
            break
        else:
            print("Invalid choice. Please try again.")

        query = input("\nEnter search query:\n")
        operator = input("Enter operator (e.g., site:example.com): ")
        full_query = f"{query} {operator}"
        print("Searching...")

        results = search_google(full_query)

        if results:
            print("\nResults:")
            for i, item in enumerate(results, start=1):
                print(f"\nResult #{i}:")
                print(f"Title: {item['title']}")
                print(f"Link: {item['link']}")
                print(f"Snippet: {item['snippet']}")

            input("Press Enter to return to the recognition menu...")
        else:
            print("Failed to perform search.")


def dns_lookup():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(create_banner())
        print("\nOptions:")
        print("[1] Continue DNS lookup")
        print("[2] Return to main menu")

        choice = input("Choose an option: ")

        if choice == '1':
            os.system('cls' if os.name == 'nt' else 'clear')
            print(create_banner())
            domain_name = input("\nEnter domain name to lookup: ")
            try:
                ip_address = socket.gethostbyname(domain_name)
                print(f"\nDNS lookup for {domain_name}:\nIP Address: {ip_address}")
                print("\nAdditional Information:")
                print(f"Local IP Address: {socket.gethostbyname(socket.gethostname())}")
                print("Server IP Address:", socket.gethostbyname(socket.gethostname()))
                
               
                interfaces = netifaces.interfaces()
                for interface in interfaces:
                    if interface != "lo":
                        addresses = netifaces.ifaddresses(interface)
                        if netifaces.AF_INET in addresses:
                            print("Network Address:", addresses[netifaces.AF_INET][0]['addr'])
                            break
                print("Network Type:", netifaces.gateways()['default'][netifaces.AF_INET][1])
                
                check_security(domain_name)
            except socket.gaierror as e:
                print(f"\nDNS lookup failed for {domain_name}: {e}")
            input("\nPress Enter to continue...")
        elif choice == '2':
            print("\nReturning to the main menu...")
            break
        else:
            print("\nInvalid choice. Please try again.")
            
def home_menu():
    print(create_banner())
    print("\nMenu:")
    print("[1] Search By Name")
    print("[2] Search Social Media")
    print("[3] Web Analytics")
    print("[4] DNS Lookup")
    print("[5] Back To Menu")

def main():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        home_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            search_by_name()
        elif choice == "2":
            search_social_media()
        elif choice == "3":
            search_with_operator()
        elif choice == "4":
            dns_lookup()
        elif choice == "5":
            print("Returning to main menu...")

            osint_tools()  
        else:
            print("Invalid choice. Please try again.")
def osint_tools_menu():
    print("Menu:")
    print("1. Osint Tools")
    print("2. Exit")
def call_osint():
    try:
        osint_tools()
    except Exception as e:
        print(f"Failed to run osint tools: {e}")
def osint_tools():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')  
        print(create_banner())
        osint_tools_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            print("Launching osint tools...")
            break
        elif choice == "2":
            print("Exiting program...")
            sys.exit() 
        else:
            print("Invalid choice. Please try again.")
            
if __name__ == "__main__":
    main()
