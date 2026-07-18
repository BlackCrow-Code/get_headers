import requests
import argparse
from rich.rule import Rule
from rich.console import Console
import pyfiglet
import json

console = Console()

#-------------------------------------------------------
pares = argparse.ArgumentParser(description="Get Headers BlackCrow-Code")
pares.add_argument("-t", "--target", required=True, help="Url && Ip address")
pares.add_argument("-he", "--header", type=str, help="Send Header in server like this in \"\" put key and the values what you want to put it  key:value ")
pares.add_argument("-s",  "--json_save", type=str, help="If you want to save the information in json file")
args = pares.parse_args()


target_url = args.target
if not target_url.startswith(("http://", "https://")):
    target_url = "http://" + target_url

#--------------Beginner stailyer--------------------
console.print(Rule(style="bold yellow")) 
get_headers = pyfiglet.figlet_format("Get Headers", font="slant")
console.print(f"[bold cyan]{get_headers}[/]")
console.print(f"[cyan]Target:[/] {target_url}")
console.print(Rule("[bold cyan].[/]"))

json_file = []
custom_headers = {}

if args.header:
    try:
        
        key, value = args.header.split(":", 1)
        custom_headers[key.strip()] = value.strip()
    except ValueError:
        pass

def scan_headers(target):
    try:
        r = requests.get(target, headers=custom_headers, timeout=5)
        for key, value in r.headers.items():
            console.print(f"[+][green1]Found[/]: [bright_yellow]{key}[/] : [grey89]{value}[/]")
            json_file.append({key: value})
    except requests.RequestException as e:
        console.print(f"[bold red][X] Connection failed: {e}[/bold red]")

scan_headers(target_url)  

if args.json_save:
    try:
        
        file_name = args.json_save if args.json_save.endswith(".json") else f"{args.json_save}.json"
        
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(json_file, f, indent=4, ensure_ascii=False)
        console.print(f"[bold green][+] Results successfully saved to '{file_name}'[/]")
        
    except Exception as e:
        console.print(f"\n[red][!] Failed to save JSON file: {e}[/]")

console.print("[blue][^1^]Completed...[/]")
