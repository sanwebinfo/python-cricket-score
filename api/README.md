# Python Cricket API

Free Cricket API - Scrape the data using `BeautifulSoup` and export a output via JSON using Flask micro web framework  

You can Free Deploy it on `Vercel`

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https%3A%2F%2Fgithub.com%2Fsanwebinfo%2Fpython-cricket-score%2Ftree%2Fmain%2Fapi)  

## Requirements 📑

- Python 3
- Required Modules
- Virtual Environment for Running Flask server
- CORS Header
- Self-hosting support with gunicorn

## Setup and Development

```sh
## install python env
sudo apt install python3-venv

## Clone the Repo
git clone https://github.com/sanwebinfo/python-cricket-score.git
cd python-cricket-score
cd api

## Create Virtual Env
python3 -m venv venv

## Activate Virtual Env
source venv/bin/activate

## install Modules
pip install -r requirements.txt

## verify
python -m flask --version

## start the dev server 
flask --app index.py --debug run --host=0.0.0.0 --port=5000
```

## Exit from Virtual Env

```sh
deactivate
```

- Edit and Modification in `index.py`

- `index.py` - for Vercel Hosting

## Usage

- API Home Page

```sh
http://127.0.0.1:5000/
```

- Get Live Cricket Score

```sh
# Copy the 5 digit code from cricbuzz Current Live Match URL 
http://127.0.0.1:5000/score?id=<Match ID>
```

```json
{
  "title": "Limpopo vs South Western Districts, 12th Match - Live Cricket Score",
  "update": "Day 2: Stumps - South Western Districts trail by 245 runs",
  "livescore": "SWD 200/5 (61)",
  "runrate": "3.28",
  "batterone": "Pheko Moletsane",
  "batsmanonerun": "17",
  "batsmanoneball": "(38)",
  "batsmanonesr": "44.74",
  "battertwo": "Jean du Plessis",
  "batsmantworun": "54",
  "batsmantwoball": "(128)",
  "batsmantwosr": "42.19",
  "bowlerone": "Morne Venter",
  "bowleroneover": "10",
  "bowleronerun": "18",
  "bowleronewickers": "0",
  "bowleroneeconomy": "1.8",
  "bowlertwo": "Ruan Haasbroek",
  "bowlertwoover": "11",
  "bowlertworun": "26",
  "bowlertwowickers": "2",
  "bowlertwoeconomy": "2.36"
}
```

## Self-hosting

- Replace `app.run()` with `app.run(host="0.0.0.0")` to run in production server

```py
if __name__ == '__main__':
    app.run(host="0.0.0.0")
    # app.run(
    #    host="0.0.0.0",
    #    port=int("5000")
    # )
```

- Create `wsgi.py` file and add the below code

```py
from index import app

if __name__ == "__main__":
    app.run()
```

- Run the API with gunicorn and systemd service
- Use APache2 or Nginx for proxy server

## Disclaimer 🗃

- This is not an Offical API from Cricbuzz - it's an Unofficial API
- This is for Education Purpose only - use at your own risk on Production Site

All Credits Goes to <https://www.cricbuzz.com/>

## LICENSE

MIT
