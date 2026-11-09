# Backend

## Routes

All routes are under `/api`.

Routes marked with a '~' are not urgent for the MVP.

Interactive docs for whatever is implemented are at http://localhost:8000/docs while the backend is running.

Auth will be done via Google Auth.

### Prompts

| Method | Route | Description |
|---|---|---|
| GET | `/api/prompts/today` | Today's prompt, its phase (`snapping` / `voting` / `closed`) and close times |
| ~GET | `/api/prompts` | Past prompts, for a history page |

### Snaps

| Method | Route | Description |
|---|---|---|
|  POST | `/api/snaps` | Upload today's photo and caption. Rejected if you already posted or snapping is closed |
|  GET | `/api/snaps/me/today` | Your snap for today, so Home can show "already posted" |
| ~DELETE | `/api/snaps/me/today` | Delete and retake, before snapping closes |
| ~GET | `/api/prompts/{id}/snaps` | All photos for a prompt, one per user. Names are shown only after voting ends |

### Voting

| Method | Route | Description |
|---|---|---|
| GET | `/api/prompts/today/ballot` | Today's snaps to vote on, anonymous and excluding your own |
| POST | `/api/votes` | Vote for a snap (`snap_id`). Checks the vote limit, no self-votes, and that voting is open |
| GET | `/api/votes/me/today` | Your votes today, to show which you picked and how many you have left |
| DELETE | `/api/votes/{snap_id}` | Remove a vote while voting is open |

### Leaderboard

| Method | Route | Description |
|---|---|---|
| GET | `/api/leaderboard/today` | Today's ranking (podium + list) after voting closes |
| ~GET | `/api/leaderboard/week` | Total votes this week |
| ~GET | `/api/prompts/{id}/results` | Results for a past prompt, for "yesterday's winner" |

### Users

| Method | Route | Description |
|---|---|---|
| GET | `/api/users/{username}` | Profile with past snaps and wins |
| PATCH | `/api/users/me` | Edit your profile |

## Code layout

One router file per feature, each included in `main.py`:
