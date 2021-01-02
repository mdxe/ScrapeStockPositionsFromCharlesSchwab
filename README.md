# Get Charles Schwab's Positions

Get your current stock positions from Charles Schwab along with current price and your cost basis.  Heavily inspired from https://github.com/bakerqb/CharlesSchwab2.0.

## Installation

After cloning this repo, you may have an incorrect version of the chromedriver, go to https://chromedriver.chromium.org/downloads to download the correct version and replace the one in this repo.

## Usage

First create credentials.json and replace the dummy user and password with your information and then run the script.

```bash
cp credentials.json.example credentials.json
vim credentials.json
python3 getPositions.py
```

