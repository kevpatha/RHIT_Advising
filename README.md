# ME Course Planner — Rose-Hulman Institute of Technology

A standalone browser-based tool that helps Mechanical Engineering students plan their remaining coursework. Given a set of completed (or in-progress) courses and an upcoming quarter, it generates a full multi-quarter schedule through graduation, respecting prerequisites, quarter availability, and credit load constraints.

---

## Files

| File | Description |
|------|-------------|
| `ME_planner.html` | The course planner application |
| `main.py` | Python launcher — starts a local web server and opens the planner in your browser |
| `ME_flowchart_standard_2025.pdf` | Official ME curriculum flowchart (source of truth for course data) |

---

## Quick Start

```bash
python main.py
```

This starts a local server on port 8765 and opens `ME_planner.html` automatically. Press `Ctrl+C` to stop.

Alternatively, open `ME_planner.html` directly in any modern web browser — no server or internet connection required.

---

## How to Use

### 1. Configure your situation
At the top of the left panel, set:
- **Upcoming quarter** — the next quarter you will be enrolling in (Fall, Winter, or Spring)
- **Starting year** — your current year standing (Freshman, Sophomore, Junior, Senior)
- **Credits/quarter** — your target credit load (12–18; default 16)
- **Control course** — toggle between **EM 306 Vibration Analysis** and **ME 306 Control Systems** (the curriculum requires one; the unchosen course is hidden from the list and excluded from scheduling)
- **HSSA electives done** — use the `−` / `+` stepper to record how many generic HSSA electives you have already completed (0–3 required beyond HUM H190 and ENGL H290)

### 2. Mark course status
The left panel lists every required ME course grouped by curriculum year. Click a course's state indicator to cycle through three states:

| Symbol | State | Effect on planner |
|--------|-------|-------------------|
| `□` (empty) | Not taken | Course will be scheduled in the plan |
| `–` (amber) | In progress | Counts as complete for prerequisite purposes; not re-scheduled |
| `✓` (red) | Completed | Excluded from plan; prereqs considered satisfied |

In-progress courses are listed in an info banner at the top of the generated plan so you can confirm they are being counted correctly.

### 3. Generate the plan
Click **Generate plan →**. The right panel displays a term-by-term schedule in the same Fall/Winter/Spring column format as the official curriculum flowchart, organized by academic year.

### 4. Read the output
Each course card shows the course ID, full title, credit hours, and an **alt quarter** badge when a course is scheduled outside its primary offering quarter.

The summary bar shows quarters planned, credits remaining, credits completed, target load, and which control course is selected.

**Color coding:**

| Color | Meaning |
|-------|---------|
| Red left border | Core ME requirement |
| Dark blue left border | HSSA requirement |
| Brown left border | Capstone sequence (ME 470 / 471 / 472) |
| Green left border | Free elective |

---

## Updating the Curriculum

Edit the `COURSES` array in the `<script>` block of `ME_planner.html`. Each entry uses this structure:

```javascript
{
  id:      "ME 302",
  title:   "Heat Transfer",
  credits: 4,
  year:    "Junior",
  primary: "Spring",
  alt:     "Fall",
  prereqs: [["MA 221"], ["ES 312"]],   // AND of OR-groups — see below
  type:    "core"
}
```

Valid `type` values: `core`, `hssa`, `capstone`, `elective`.

### Prerequisite format

`prereqs` is an array of OR-groups. The scheduler requires **all** groups to be satisfied (logical AND), and within each group **any one** course satisfies it (logical OR):

```javascript
// Requires MA 221 AND ES 312
prereqs: [["MA 221"], ["ES 312"]]

// Requires (ME 123 OR CSSE 120) AND (ES 213 OR ECE 203)
prereqs: [["ME 123", "CSSE 120"], ["ES 213", "ECE 203"]]

// No prerequisites
prereqs: []
```

---

## Technical Notes

The planner is a single self-contained HTML file with no external dependencies and no build step. All scheduling logic is written in vanilla JavaScript.
