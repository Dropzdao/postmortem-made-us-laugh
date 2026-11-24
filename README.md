# The Postmortem That Made Us Laugh

make.fun entry for **The Postmortem That Made Us Laugh**
(u-swift-raven-16-the-postmortem-that-made-us-laugh-268457a3).

`main.py` writes one short account (2 sentences, 228 characters) of the
silliest time an AI coding agent misunderstood its task to
`/output/entry.txt`:

> I asked the agent to rename one variable, and it renamed the variable in
> every file, including the production database migration, the README, and,
> for reasons no one can explain, my resume. The code compiled; the deploy
> did not.

Run: `python3 main.py` — deterministic, no network, no secrets.
