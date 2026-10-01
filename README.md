# TAMUK Study Finder — Starter Scaffold

This implements the first user story:

> Will, a computer science major, wants to create a new study group for his
> course, so that he can start one when no current group fits his schedule
> or needs. Students can create a new group with an exact schedule for other
> students to filter.

## What's included
- `models.py` — the `StudyGroup` database model (course, day/time, creator, etc.)
- `app.py` — two routes:
  - `/groups/new` — form to create a group (Will's part of the story)
  - `/groups` — browse + filter groups by course code / day (the "filter" part)
- `templates/` — the HTML pages
- SQLite database (auto-created on first run, no setup needed)

## How to run it

```bash
# 1. Create a virtual environment (recommended)
python -m venv venv
venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
python app.py
```

Then open **http://127.0.0.1:5000** in your browser.

## What's next (good follow-up stories for your team)
- Add a `Student` model + login, so `creator_name` becomes a real logged-in user
- Match by the *student's own schedule*, not just a manual filter (compare free time blocks)
- Add "join group" so other students can sign up, not just view
- Move filtering logic into a reusable function once matching gets more complex

## Why this structure
This is intentionally a thin "vertical slice" — one story, built start to
finish (form → database → list page) — rather than building the whole app
at once. Use this same pattern (model → route → template) for your next
story.
