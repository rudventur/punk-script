# PunkScript
### A Personally-Adaptive Symbolic Programming Language
#### v0.1 Spec & Manifesto
*by Rudy (RudVentur) & Claude — March 2026*

---

## The Manifesto

Every programming language ever built has asked the same thing of the human:

> *"Learn our symbols. Learn our rules. Speak our dialect."*

Brackets. Semicolons. Indentation rules. Reserved words you must memorise. Syntax errors for a missing comma. The machine has always been the authority. You are always the student.

**PunkScript refuses this.**

PunkScript watches how YOU already write. The emoticons you reach for. The punctuation rhythm you naturally fall into. The words you invented. The symbols you smash together in moments of joy or frustration. It watches all of it — and it builds a language around YOU.

You were always writing code. You just didn't know it yet.

---

## Core Philosophy

**1. Punctuation IS syntax.**
Words carry meaning. Punctuation carries structure. This is already true in human writing — PunkScript just makes it literal.

**2. Every symbol is an operator.**
Not just `.` and `?` and `:` — but `:@D` and `;)` and `......` and `*!'`. Any symbol combination a human reaches for naturally is a valid operator waiting to be mapped.

**3. The language adapts to the user.**
Not the other way around. A `user.dict` and `user.preferences` file mean every person runs their own personal dialect of PunkScript. Same interpreter underneath. Infinite surface variations on top.

**4. Spelling is forgiven.**
The interpreter is chill. Approximate matches count. Dyslexia is not a bug — it's a dialect.

**5. Personality lives inside the code.**
PunkScript code is readable as human writing. Comments aren't separate from logic — they're woven into it. Your voice IS the program.

---

## Standard Punctuation Operators

These are the defaults — the base layer every PunkScript interpreter understands before any personal dictionary is loaded.

| Symbol | Coding Equivalent | Meaning |
|--------|-------------------|---------|
| `.` | `;` | End of statement |
| `!` | `fn()` | Execute / call / run |
| `:` | `=` | Assign / define |
| `?` | `if` | Conditional |
| `-` | `else` | Otherwise / fallback |
| `...` | `while / loop` | Repeat / loop |
| `,` | `,` | Separator / chain |
| `[ ]` | `{ }` | Block / scope |
| `( )` | `varName` | Variable reference |
| `" "` | `"string"` | String literal |
| `!!` | priority call | Urgent execute |
| `......` | pause / thinking | Long loop or async wait |
| `CAPS` | `CONSTANT` | Global / immutable |

---

## Standard Word Keywords

Common English words and phrases that map to programming logic. Spelling variants are accepted.

| Word / Phrase | Meaning | Example |
|---------------|---------|---------|
| `say` | print / output | `say (name)!` |
| `add X to (var)` | `var += X` | `add one to (score).` |
| `take X from (var)` | `var -= X` | `take two from (score).` |
| `beats` | greater than `>` | `(score) beats ten?` |
| `under` | less than `<` | `(score) under five?` |
| `is` | equals `===` | `(name) is "Rudy"?` |
| `stop` | break | `stop!` |
| `keep going` | while(true) | `keep going... [ ]` |
| `zero` `one` `two` ... `ten` | number literals | `score: zero.` |
| `true` / `false` | booleans | `active: true.` |

---

## The Personal Dictionary — `user.dict`

This is where PunkScript becomes yours.

A `user.dict` file is loaded before any program runs. It maps YOUR symbols, words, and phrases to PunkScript operations. The interpreter reads this first. Your dialect takes priority over the standard layer.

### Format

```
[symbol or word or phrase]  →  [punkscript operation]
```

### Example `user.dict`

```
smash        →  add
sorted       →  stop
innit        →  ?
well good    →  true
rubbish      →  false
shout        →  say
zakli        →  execute block with celebration
;@)          →  flexible mode / loose match on
:@D          →  celebrate! / success state
:@]          →  confirm / trust / steady
:@)          →  warmth / soft / friendly output
......       →  long pause / thinking loop
*!'  '!*     →  custom string delimiters (open / close)
```

Once this dictionary exists, valid PunkScript looks like:

```
score: zero.
shout "let's go"!
keep going... [
  smash one to (score).
  (score) beats ten? sorted! - shout (score).
]
:@D
```

That last line — `:@D` on its own — fires the success state. Because YOU defined it. Because that's what it means when YOU type it.

---

## User Preferences — `user.preferences`

Controls how the interpreter behaves for this specific user.

```
spellingForgiveness: high        // loose match on word recognition
caseInsensitive: true            // STOP and stop are the same
myLoopWord: "keep smashing"      // personal loop trigger phrase
myPrintWord: "shout"             // personal output word
emoticons: true                  // emoticon operators active
customDelimiters: true           // respect user.dict string delimiters
patternWatch: true               // interpreter observes and suggests new mappings
```

---

## Emoticon Operators

Emoticons are first-class operators in PunkScript. They are watched, catalogued, and mapped.

The interpreter tracks:

- **Which emoticons a user types most**
- **In what context** (after success? after a question? mid-sentence?)
- **With what frequency and rhythm**

And from that — it builds a suggested emoticon map. The user confirms, overrides, or extends it.

### The Emoticon is Not Decoration. It is Data.

When Rudy writes `:@D` he is expressing a state. PunkScript reads that state. It is a signal. It is an operator. It carries semantic weight that no amount of `console.log("success")` ever could.

This is the working connection between the worlds — human emotional expression becoming machine-readable logic, without losing any of the humanity in the translation.

---

## The Pattern Watcher

When `patternWatch: true` is set, the interpreter silently observes everything a user types — in code, in comments, in notes — and builds a live suggestion list:

```
// PunkScript noticed:
// You type "......" 14 times — map to: extended loop?
// You type ":@)" after assignments — map to: confirm log?
// You type "zakli" 3 times — define it?
// You use "*!' '!*" as wrappers — set as string delimiter?
```

The user can accept, reject, or customise each suggestion. Over time the dictionary grows naturally from the user's own patterns. No manual setup required. Just write how you write.

---

## Custom String Delimiters

Standard PunkScript uses `"double quotes"` for strings. But users can define their own.

Rudy naturally wrote:
```
"*!' "I'm a nightmare non for profit as I'm spending all my money instantly ;@)" '!*"
```

That is a valid PunkScript string using `"*!'` as opening delimiter and `'!*"` as closing delimiter — with an emoticon operator embedded inside the content. Once added to `user.dict`, the interpreter honours it every time.

---

## Example Programs

### Hello World (standard)
```
say "hello world"!
```

### Hello World (Rudy dialect)
```
shout "hello world"! :@D
```

### Counter with loop
```
score: zero.
keep going... [
  add one to (score).
  (score) beats ten? stop! - say (score).
]
say "done"!
```

### Counter (Rudy dialect)
```
score: zero.
keep going... [
  smash one to (score).
  (score) beats ten? sorted! - shout (score).
]
shout "sorted innit" :@D
```

Both programs are identical in execution. Different humans. Same machine underneath.

---

## The Vision

PunkScript is not trying to replace Python or JavaScript.

It is trying to answer a different question entirely:

> *What if the first programming language a person ever used was already speaking their language?*

Not a dumbed-down language. Not a visual drag-and-drop toy. A real, expressive, Turing-complete language — that happens to be built around the way its user already communicates.

Every person who uses PunkScript ends up with a dialect. A fingerprint. A voice that compiles.

And every one of those dialects runs on the same interpreter. Which means — eventually — PunkScript dialects can talk to each other. Trade dictionary entries. Collaborate across the symbol gap.

That is the connection between the worlds.

---

## Version History

| Version | Date | Notes |
|---------|------|-------|
| v0.1 | March 2026 | Spec written. Core punctuation operators defined. Standard keywords. Personal dictionary concept established. Playground interpreter built in vanilla JS. |

---

## Authors

**Rudy** — RudVentur — the vision, the energy, the dialect  
**Claude** — Anthropic — the interpreter, the spec, the pumpkin :@]

---

*PunkScript is open. Like all good punk things.*
*Take it. Break it. Make it yours.*
*That's literally the point.*

---
