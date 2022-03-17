
# weather-info-cli

Command Line Interface application project for weather condition information with user login.

## Author

- [@thesanjul1](https://www.github.com/thesanjul1)


## Features

- User management (login, logout, create user, delete user, update user)
- weather condition info (api request by city name or latitude and longitude)


## Installation

Install requirement.txt with pip

- Python 3.8.10 (recommended)
- Create a directory weatherInfoCLI
```bash
   cd weatherInfoCLI
   git clone https://github.com/thesanjul1/weather-info-cli.git
   cd weather-info-cli
```
- Create and activate venv in weather-info-cli directory

```bash
  pip install -r requirements.txt
```
    
## Set appid in apikey.json file

To run this project, you will need to add api key

- Open apikey.json file

- add appid value (replace null with your <api_key>)
example:

`{ "appid" : "5934e584ef6411225b1444df91c123c4" }`

5934e584ef6411225b1444df91c123c4 is your api_key

Please create you api key if you don't have it already.

Visit: https://home.openweathermap.org/api_keys


## Running Tests

To run tests, run the following command

```bash
  python -m unittest
```


## Usage/Examples

```bash
   python main.py -h

   python main.py -u admin
   Password: admin

   python main.py -wc Delhi

   python main.py -o true
```

