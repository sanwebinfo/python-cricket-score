# Python Cricket Score

[![os-file-test](https://github.com/sanwebinfo/python-cricket-score/actions/workflows/os.yml/badge.svg)](https://github.com/sanwebinfo/python-cricket-score/actions/workflows/os.yml) [![get-score](https://github.com/sanwebinfo/python-cricket-score/actions/workflows/test.yml/badge.svg)](https://github.com/sanwebinfo/python-cricket-score/actions/workflows/test.yml)  

Get Live Cricket Score on your Terminal - A Simple Live Score Data Scraper Created using Python.  

> A Simple Python Script to Get Live Cricket Score on your Terminal and CMD  

unofficial API Data Fetched from Cricbuzz.com **(This is for Education Purpose Only)**  

This is an unofficial API and not Linked or Partnered with Any Brands/Company.  

## How it Works? 🤔

We are just fetching and Scrape the data from Cricbuzz using Python `BeautifulSoup` Module It's kind of data scraping but we are not storing any data or link in our end.  

Everything is scraped live and shown to end users in realtime.  

I maily build the Live Cricket Score Python Script for my Galaxy watch 4 Automation via MacroDroid and KDE Connect.  

I use **Kitty Terminal** for my Watch Automation  

```sh
kitty --hold python3 $HOME/your-directory/python-criket-score/score.py
```

https://user-images.githubusercontent.com/10300271/227778482-391dcb78-93a9-4b8a-8230-3b75335f7ba5.mp4

## Requirements 📑

- Python 3
- Required Modules

## Installation 🍯

- Download or Clone Repo to your Server

```sh
git clone https://github.com/sanwebinfo/python-cricket-score.git
cd python-cricket-score
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- Test the Script

```sh
## IPL SCore
python3 ipl.py

## Get Score the Match URL you Provided
python3 score.py
```

- it will automatically Generate a App folder on your OS Home directory Named as `python-cricket-score` with the `score.yaml` file
- Update Cricbuzz Live Match URL on `score.yaml` file

## JSON API

Free Python Cricket API - Scrape the data using `BeautifulSoup` and export a output via JSON using Flask micro web framework  

Check - <https://github.com/sanwebinfo/python-cricket-score/tree/main/api>  

## World Cup Cricket Score

- Just run the below command to get score

```sh
curl -sL https://dub.sh/pyscore | python3
```

## Contributing 🙌

Your PR's are Welcome

## Lint and Formatting

```sh
## Check Lint Errors
python3 -m pip install flake8
python3 -m flake8
```

```sh
## Auto Formatting the Code
pip install --upgrade autopep8
python3 -m autopep8 score.py ## Dry Run
python3 -m autopep8 -i score.py ## Format the Code

# Autofix
python3 -m autopep8 --select E1,E2,E3,E401,W2,W3 --ignore E226,E24,E26 --in-place --recursive --verbose .
```

```sh
## Check Lint Errors
pylint score.py
```

## Disclaimer 🗃

- This is not an Offical API from Cricbuzz - it's an Unofficial API
- This is for Education Purpose only - use at your own risk on Production Site

All Credits Goes to <https://www.cricbuzz.com/>

## LICENSE 📕

MIT
