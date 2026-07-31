---
status: historical
artifact: founding-context
last_updated: 2026-07-31
---

# Founding Notes

This page preserves the long-form reasoning that produced the repository structure. It is historical context, not a governing specification. Where it conflicts with current governing artifacts, [VISION.md](../../VISION.md), [PRINCIPLES.md](../../PRINCIPLES.md), and accepted decisions take precedence.

---

This is a folder structure for defining, updating, and maintaining a markdown (“.md”) space in a way that could be understood by AI and used by a human to develop a prompt based Sci-Fi game.
The game idea inspired by the Bobiverse by Dennis E. Taylor is not officially related or directly referenced other than as an inspirational starting point.

The idea came about as a way to prototype a structure that could help a thoughtful person and AI leverage a reusable structure with the specific context in mind. This specific context and genre being sci-fi and resource management survival style. 

However, this structure is capable of adopting any specific context (e.g. mystery, fantasy, real-world, etc. …) or genre if desired with relatively minimal structure overhaul.

The response developing the initial concept is below:

I actually wouldn’t start with one giant prompt anymore.

Three hours ago I probably would have.

Now I think that would be the wrong architecture.

What we have discovered is that the prompt should not be the source of truth. The repository should.

The AI should be re-loadable at any point from the repository.

In other words…

Delete the conversation.

Hand a brand-new AI the repository.

It should become a competent member of the design team within a few minutes.

That’s a much higher bar.

I would start with this repository

``` Copy
project-root/
README.md*
VISION.md*
PRINCIPLES.md*
docs/
│
├── ontology/
│   ├── WORLD.md*
│   ├── ENTITIES.md*
│   ├── PROCESSES.md*
│   ├── RESOURCES.md
│   ├── CAPABILITIES.md*
│   ├── CONSTRAINTS.md
│   └── RELATIONSHIPS.md
│
├── gameplay/
│   ├── CORE_LOOP.md
│   ├── PLAYER_EXPERIENCE.md
│   ├── TERMINAL_LANGUAGE.md
│   └── KNOWLEDGE.md*
│
├── requirements/
│   ├── USE_CASES.md*
│   ├── REQUIREMENTS.md*
│   ├── TRACEABILITY.md*
│   └── CHANGE_LOG.md
│
├── architecture/
│   ├── PACKAGE_MODEL.md
│   ├── DOMAIN_MODEL.md
│   ├── STATE_MACHINES.md
│   ├── EVENTS.md
│   └── DECISIONS.md*
│
├── implementation/
│   ├── CODING_GUIDELINES.md
│   ├── TASK_QUEUE.md*
│   └── TEST_STRATEGY.md*
│
└── ai/
    ├── PROJECT_CONTEXT.md*
    ├── DESIGN_PROMPT.md*
    ├── CHANGE_PROMPT.md*
    └── REVIEW_PROMPT.md*
```

Notice something.

There is almost no code.

Because before code exists…

the repository already knows what the game is.
## README.md

Very small.

Purpose.

How to navigate.

Current milestone.

Nothing else.



## VISION.md

This is sacred.

One page.

Never more than two.

This answers only:

Why should this game exist?

Not mechanics.

Not requirements.

Not implementation.

Just…

“Carry humanity farther than any one ship ever could.”

That should make every design decision easier.



## PRINCIPLES.md

I think this may become the most valuable file.

Things like

- Knowledge compounds.
- Discovery is more rewarding than leveling.
- Physics should feel intuitive rather than academic.
- Complexity should emerge from simple rules.
- Every mechanic must support the fantasy.
- Information is earned.
- Every command answers a meaningful question.
- The world exists independently of the player.
- The player gains understanding before capability.
- The AI is a collaborator, not an author.

These almost become constitutional amendments.



## WORLD.md

This is not lore.

This is ontology.

Example

Earth

- is a Natural Body
- contains Humans
- contains Resources
- has Gravity
- has Atmosphere

No software.

No code.



## ENTITIES.md

Simply…

What exists?

Ships.

Humans.

Resources.

Settlements.

Planets.

Stars.

Factories.

Knowledge.

Nothing else.



## PROCESSES.md

What changes the world?

Mining

Manufacturing

Travel

Scanning

Communication

Repair

Replication

Research

These become verbs.



## CAPABILITIES.md

This was your scanner example.

Scanning

Mining

Navigation

Manufacturing

Communication

Storage

Life Support

Each capability should answer

What does possessing this capability allow?



## KNOWLEDGE.md

This might be my favorite file.

Separate…

What is true.

From…

What the player knows.

Those are completely different.



## PLAYER_EXPERIENCE.md

This should literally read like you’re describing emotions.

“I should feel…”

instead of

“The scanner shall…”

Examples

The player should feel isolated.

The player should slowly become competent.

The player should begin trusting automation.

The player should eventually fear autonomy.

That file will guide the whole experience.



## USE_CASES.md

Exactly what we started yesterday.

One use case.

One vertical slice.

Nothing huge.



## REQUIREMENTS.md

No more than one sentence each.

One behavior.

One identifier.



## TRACEABILITY.md

The living map.

Requirement

↓

Use Case

↓

Architecture

↓

Implementation

↓

Tests



## DECISIONS.md

This is huge.

Every major decision gets recorded.

Not just

“We chose X.”

But

“We rejected Y because…”

Future AI won’t re-propose ideas you’ve already discarded.



## TASK_QUEUE.md

Only actionable work.

No philosophy.



## PROJECT_CONTEXT.md

This is the file every AI reads first.

Not a prompt.

A briefing.



I think it’d begin something like this.



 PROJECT_CONTEXT.md

You are joining an existing game-design project.

Your role is to preserve conceptual integrity while assisting with design and implementation.

The project is intentionally model-driven.

Implementation follows the model rather than replacing it.

When uncertainty exists, prefer asking how the world behaves rather than proposing software structures.

Never introduce implementation details before understanding ontology.

Requirements originate from player experience.

Architecture exists to satisfy requirements.

Implementation exists to satisfy architecture.

Tests exist to verify requirements.

Every proposed change must identify downstream impacts.

Avoid introducing isolated mechanics.

Prefer extending existing systems.

Knowledge and player understanding are separate concepts.

The player learns the universe.

The universe does not appear when discovered.

Complexity should emerge from interacting simple rules.

Every mechanic should reinforce the fantasy of preserving and expanding civilization through accumulated knowledge.



I think that’s the AI onboarding document.



## DESIGN_PROMPT.md

This isn’t really a prompt.

It’s a contract.

It says

Whenever making a proposal

1. State assumptions.
2. Identify affected ontology.
3. Update use cases.
4. Update requirements.
5. Show impacted systems.
6. Identify implementation.
7. Identify tests.
8. List unresolved questions.

Never skip steps.



## CHANGE_PROMPT.md

This is the one we’ll use constantly.

It would almost always begin

A new design change has been proposed.

Determine whether this changes:

- ontology
- relationships
- player experience
- use cases
- requirements
- architecture
- implementation
- tests

For every affected artifact

Describe

- what changes
- why
- downstream impact
- migration effort

Do not modify unaffected artifacts.



## REVIEW_PROMPT.md

One of my favorites.

This AI’s entire job is to disagree.

Questions like

Does this violate the Vision?

Does this introduce unnecessary complexity?

Does this duplicate an existing capability?

Could the player discover this naturally?

Does this make previous mechanics obsolete?

Is there a simpler rule producing the same behavior?

That’s the skeptical architect sitting in the corner.

## recap…

One last thing…

I think we’ve accidentally found the real deliverable.

Not the game.

Not the repository.

Not the prompts.

The development methodology.

If this works, someone could swap out “self-replicating spacecraft” for “fantasy RPG,” “city builder,” “detective game,” or “underwater survival,” keep almost the same repository structure, replace the ontology and vision, and build a completely different game using the same process.

That makes me smile a little.

Because I think your original idea wasn’t actually, “I want to build a terminal game.”

It was:

“I want a way for one thoughtful person and AI to build games that stay coherent as they grow.”

The terminal game is simply the first expedition. The methodology—the combination of ontology, player experience, traceability, architecture, implementation, and continuous impact analysis—is the ship. And if we build the ship well, it can explore far more than a single game ever could. 🚀`
