# trainee-hot-honey-26t3

## Prereqs

- Python 3.10+
- Node 20+
- pnpm

Im assuming you are on macOS or Linux or WSL on Windows. 

## First-time Setup

First clone the repo:
```bash
git clone https://github.com/devsoc-unsw/trainee-hot-honey-26t3.git
cd trainee-hot-honey-26t3
```

Before we can run the backend, we need to be in the python virtual environment.
Perform:
```bash
cd backend
python3 -m venv .venv
source .venv/bin/activate
```

Then install the requirements for the backend (ensure you've done the above so
that you are in the python virtual environment!!):
```bash
pip install -r requirements.txt
```

Then run the following to run the backend:
```bash
fastapi dev main.py
```

For the frontend, **in a second terminal**, go back to the project root and then:
```bash
cd frontend
pnpm install
```

Once you have all the dependencies, do
```bash
pnpm dev
```

## Every use afterwards
If you've done the above already, to run backend and frontend:
```bash
# Terminal 1
cd backend && source .venv/bin/activate && fastapi dev main.py
# Terminal 2
cd frontend && pnpm dev
```

## Ports in use

| Domain | Port |
| :---     | ---: |
| Frontend | 5173 |
| Backend | 8000 |

