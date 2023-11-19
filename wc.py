import time
import requests
from bs4 import BeautifulSoup as bs
from halo import Halo
import importlib.util
import sys

spinner = Halo(text='World Cup Score...', color='green', spinner='dots')
modeules = Halo(text='Loading...', spinner='dots', color='cyan')
url_data = "https://www.cricbuzz.com/cricket-match/live-scores"
recent_data = "https://www.cricbuzz.com/cricket-match/live-scores/recent-matches"
package_one = 'requests'
package_two = 'bs4'
package_three = 'halo'

try:

    if importlib.util.find_spec(package_one) is None:
       print(package_two +" is not installed \n")
       sys.exit()
    elif importlib.util.find_spec(package_two) is None:
       print(package_two +" is not installed \n")
       sys.exit()
    elif importlib.util.find_spec(package_three) is None:
       print(package_three +" is not installed \n")
       sys.exit()
    else:
       modeules.start()
       time.sleep(2)
       modeules.stop()
       print("> Verify Module and Getting Score Data...", end="\r")
       time.sleep(2)

    spinner.start()
    time.sleep(1)
    spinner.stop()
    r = requests.get(url_data)
    soup = bs(r.content, 'html.parser')
    div = soup.find(
        "div", attrs={"ng-show": "active_match_type == 'international-tab'"})

    matches = div.find_all(class_="cb-mtch-lst cb-col cb-col-100 cb-tms-itm")
    for match in matches:
        team_names = match.find("h3").text.strip().replace(",", "")
        status = match.find(
            "div", attrs={"class": "cb-text-live"}).text.strip()
        score = match.find_all(
            "div", attrs={"style": "display:inline-block; width:140px"})[0].text.strip() if match.find_all(
            "div", attrs={"style": "display:inline-block; width:140px"})[0].text.strip() else 'Not yet Started'
        score_two = match.find_all(
            "div", attrs={"style": "display:inline-block; width:140px"})[1].text.strip() if match.find_all(
            "div", attrs={"style": "display:inline-block; width:140px"})[1].text.strip() else 'Not yet Started'
        team_one = match.find_all(
            "div", attrs={"class": "cb-ovr-flo cb-hmscg-tm-nm"})[0].text.strip()
        team_two = match.find_all(
            "div", attrs={"class": "cb-ovr-flo cb-hmscg-tm-nm"})[1].text.strip()

        print("\n")
        print(">", team_names, "-", status, "\n")
        print(">", team_one, "-", score, "\n")
        print(">", team_two, "-", score_two, "\n")

except IndexError:
    spinner.stop()
    r = requests.get(recent_data)
    soup = bs(r.content, 'html.parser')
    div = soup.find(
        "div", attrs={"ng-show": "active_match_type == 'international-tab'"})

    matches = div.find_all(class_="cb-mtch-lst cb-col cb-col-100 cb-tms-itm")
    for match in matches:
        team_names = match.find("h3").text.strip().replace(",", "") if match.find(
            "h3").text.strip().replace(",", "") else 'NO World cup Live Match at the Moment'
        status = match.find(
            "div", attrs={"class": "cb-text-complete"}).text.strip() if match.find("div", attrs={"class": "cb-text-complete"}) else 'NO World cup Live Match at the Moment'
        print("\n")
        print(">", team_names, "-", status, "\n")
except AttributeError:
    spinner.stop()
    r = requests.get(recent_data)
    soup = bs(r.content, 'html.parser')
    div = soup.find(
        "div", attrs={"ng-show": "active_match_type == 'international-tab'"})

    matches = div.find_all(class_="cb-mtch-lst cb-col cb-col-100 cb-tms-itm")
    for match in matches:
        team_names = match.find("h3").text.strip().replace(",", "") if match.find(
            "h3").text.strip().replace(",", "") else 'NO World cup Live Match at the Moment'
        status = match.find(
            "div", attrs={"class": "cb-text-complete"}).text.strip() if match.find("div", attrs={"class": "cb-text-complete"}) else 'NO World cup Live Match at the Moment'
        print("\n")
        print(">", team_names, "-", status, "\n")
except requests.ConnectionError as e:
    spinner.stop()
    print("OOPS!! Connection Error")
except requests.Timeout as e:
    spinner.stop()
    print("OOPS!! Timeout Error")
except requests.RequestException as e:
    spinner.stop()
    print("API Error")
except ImportError:
    spinner.stop()
    print('Modules not Found - install request, beautifulsoup4, halo')
except (KeyboardInterrupt, SystemExit):
    spinner.stop()
    print("i am quitting")
