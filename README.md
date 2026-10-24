# Task Implementation

## Current state of things
The code successfully receives all of the feed from sensors and servos. Simple logging is implemented. Rocket and proxy work in docker container.


## Usage

Get python enviroment going: 

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start the rocket and proxy setup:
```bash
docker compose up --build
```

start the code
```bash
python main.py
```
