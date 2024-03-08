import requests
from bs4 import BeautifulSoup
import subprocess

URL = "https://secure.onreg.com/onreg2/bibexchange/?eventid=6087"

def check_tickets():
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    containers = soup.find_all("b")

    for container in containers:
        if "Der er ikke nogen startnumre til salg i øjeblikket. Prøv igen lidt senere." not in container.text:
            return True
    return False

def send_notification():
    applescript_command = 'tell app "System Events" to display dialog "Tickets are available for the CPH Marathon. Go to the website and buy them now!" with title "Tickets are available!"'
    subprocess.run(["osascript", "-e", applescript_command])

    # send_email("Tickets are available!", "Tickets are available for the CPH Marathon. Go to the website and buy them now!")


def main():
    if check_tickets():
        send_notification()

if __name__ == "__main__":
    main()
    print(1)
