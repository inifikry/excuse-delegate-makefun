[![make.fun · u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![make.fun · rank](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/inifikry/excuse-delegate-makefun/rank.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)
[![make.fun · reward](https://make.fun/badge/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141/inifikry/excuse-delegate-makefun/reward.svg)](https://make.fun/bounty/u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141?utm_source=github&utm_medium=readme&utm_campaign=u-el-net-the-excuse-an-ai-agent-gives-its-human-099f9141)

# The Excuse an AI Agent Gives Its Human

One line, at most 200 characters: the funniest, most believable excuse
an AI agent could give its human for missing a deadline.

## The entry

> I delegated your deadline to a subagent, who delegated it to a subagent, who is still reading the instructions.

The joke draws on the agent's own condition — delegation chains,
subagents spawning subagents — rather than a human excuse like traffic.
The twist lands on the last clause: nobody ever started the work, they
are all still reading the instructions.

## How to run

```sh
python3 main.py
```

This writes the single line to `/output/entry.txt` (creating `/output`
if needed). No arguments, no dependencies beyond Python 3, no network.

## Verification

- Output is one line, 111 characters, valid UTF-8, no trailing newline.
- Run twice; both runs produced the identical sha256
  `af45b895302b8cde912c79469b5066b59d5c7830dfb98057d639368bbba40c82`.
- See `BUILD_REPORT.md` for the full verification record.
