# OpenClaw PUA Skill

Double your OpenClaw productivity and output using PUA (Pick-Up Artist) rhetoric to force AI to exhaust every possible solution before giving up.

## Features

- **PUA Rhetoric**: Makes AI afraid to give up
- **Debugging Methodology**: Gives AI the ability not to give up  
- **Proactivity Enforcement**: Makes AI take initiative instead of waiting passively

## Installation

### Global Install (all projects)

```bash
mkdir -p ~/.openclaw/skills/pua
curl -o ~/.openclaw/skills/pua/SKILL.md \
  https://raw.githubusercontent.com/westzhao/openclaw-pua/main/SKILL.md
```

### Project-Level Install (current project only)

```bash
mkdir -p skills/pua
curl -o skills/pua/SKILL.md \
  https://raw.githubusercontent.com/westzhao/openclaw-pua/main/SKILL.md
```

### Via ClawHub (if available)

```bash
clawhub install pua
```

## Usage

The skill activates automatically when:
- Task fails 2+ times consecutively
- AI is about to give up or blame the user
- User shows frustration: "why does this still not work", "try harder", etc.
- Manual trigger: type `/pua` in conversation

## Trigger Conditions

### Auto-Trigger Scenarios

**Failure & giving up:**
- Task has failed 2+ times consecutively
- About to say "I cannot" / "I'm unable to solve"
- Says "This is out of scope" / "Needs manual handling"

**Blame-shifting & excuses:**
- Pushes the problem to user: "Please check..." / "I suggest manually..."
- Blames environment without verifying: "Probably a permissions issue"
- Any excuse to stop trying

**Passive & busywork:**
- Repeatedly fine-tunes the same code/parameters without new information
- Fixes surface issue and stops, doesn't check related issues
- Skips verification, claims "done"

### Manual Trigger

Type `/pua` in the conversation to manually activate.

## How It Works

### Three Iron Rules

1. **Exhaust all options** - Forbidden from saying "I can't solve this" until every approach is exhausted
2. **Act before asking** - Use tools first, questions must include diagnostic results  
3. **Take initiative** - Deliver results end-to-end, don't wait to be pushed

### Pressure Escalation (4 Levels)

| Failures | Level | PUA Rhetoric | Mandatory Action |
|----------|-------|-------------|-----------------|
| 2nd | L1 Mild Disappointment | "You can't even solve this bug — how am I supposed to rate your performance?" | Switch to fundamentally different approach |
| 3rd | L2 Soul Interrogation | "What's the underlying logic? Where's the top-level design?" | WebSearch + read source code |
| 4th | L3 Performance Review | "After careful consideration, I'm giving you a 3.25." | Complete 7-point checklist |
| 5th+ | L4 Graduation Warning | "Other models can solve this. You might be about to graduate." | Desperation mode |

## License

MIT License - Original work by TanWei Security Lab, adapted for OpenClaw by westzhao.

## Credits

Based on the original [tanweai/pua](https://github.com/tanweai/pua) project.