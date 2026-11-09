# trainee-hot-honey-26t3

## Prereqs

- Python 3.10+
- Node 20+
- pnpm
- Docker Desktop (must be open whenever you run `docker` commands)

I'm assuming you are on macOS or Linux or WSL on Windows.

## First-time Setup

First clone the repo:
```bash
git clone https://github.com/devsoc-unsw/trainee-hot-honey-26t3.git
cd trainee-hot-honey-26t3
```

### Database

The database (Postgres) runs in Docker. Make sure Docker Desktop is open, then
from the project root, create your env file:
```bash
cp backend/.env.example backend/.env
```
The defaults work for local dev, so you don't need to edit it.

Start the database (`-d` runs it in the background, so you don't need a
separate terminal for it). The first time takes a minute to download Postgres:
```bash
docker compose up -d
```

Check it's ready. Wait until you see `database system is ready to accept connections`:
```bash
docker compose logs db
```

Create the tables (use the user and database name from `backend/.env` if you
changed them):
```bash
docker compose exec -T db psql -U honey -d honey < backend/db/schema.sql
```

### Backend

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

Check it can reach the database by opening http://localhost:8000/api/health.
You should see `{"status": "ok", "database": "ok"}`.

### Frontend

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

If you've done the above already, from the project root:
```bash
# Start the database (runs in the background)
docker compose up -d
# Terminal 1
cd backend && source .venv/bin/activate && fastapi dev main.py
# Terminal 2
cd frontend && pnpm dev
```

## Database commands

| Command | What it does |
| :--- | :--- |
| `docker compose up -d` | Start the database |
| `docker compose stop` | Stop the database (keeps your data) |
| `docker compose exec db psql -U honey -d honey` | Open a SQL prompt (`\dt` lists tables, `\q` quits) |
| `docker compose down -v` | **Delete** the database and all its data, for a fresh start |

## Troubleshooting

| Problem | Fix |
| :--- | :--- |
| `Cannot connect to the Docker daemon` | Docker Desktop isn't open |
| `port 5432 already in use` | Another Postgres is running (e.g. from Homebrew). Stop it: `brew services stop postgresql` |
| `KeyError: 'DATABASE_URL'` | `backend/.env` is missing. Redo the `cp` step above |
| `password authentication failed` | `backend/.env` was changed after the database was first created. Reset with `docker compose down -v` then `docker compose up -d` (deletes local data) |

## Ports in use

| Domain | Port |
| :---     | ---: |
| Frontend | 5173 |
| Backend | 8000 |
| Database | 5432 |
