# ME Course Planner — Rose-Hulman Institute of Technology

A standalone browser-based tool that helps Mechanical Engineering students plan their remaining coursework through graduation. Given a student's completed courses and upcoming quarter, it either generates a full multi-quarter schedule automatically or allows the student to build their own schedule with live validation.

No installation, server, or internet connection required — open `me_planner.html` directly in any modern browser.

---

## Files

| File | Description |
|------|-------------|
| `me_planner.html` | The course planner application |
| `ME_curriculum.csv` | Source data — all ME courses with credits, prerequisites, and quarter availability |
| `README.md` | This file |

---

## How to Use

### Step 1 — Open the planner

Open `me_planner.html` in any modern web browser (Chrome, Firefox, Edge, Safari). No setup required.

### Step 2 — Configure your situation (left panel)

Set the following before generating a plan:

| Setting | Description |
|---------|-------------|
| Upcoming quarter | The next quarter you will enroll in (Fall, Winter, or Spring) |
| Year standing | Your current academic year (Freshman through 6th Year) |
| Target cr/quarter | Your desired credit load per quarter, between 12 and 18 (default: 16) |
| Control course | Choose either EM 306 (Vibration Analysis) or ME 306 (Control Systems) — only one is required |

### Step 3 — Enter completed electives

Use the four counters to record how many of each elective type you have already completed:

| Elective type | Total required |
|---------------|---------------|
| HSSA Electives | 6 |
| Technical Electives | 3 |
| Math/Science Elective | 1 |
| Free Electives | 2 |

These are in addition to HUM H190 and ENGL H290, which are tracked individually as courses.

### Step 4 — Mark completed courses

The course list groups all required ME courses by curriculum year. Click each course to cycle through three states:

| State | Appearance | Meaning |
|-------|-----------|---------|
| □ (empty) | Normal | Not yet taken — will be scheduled |
| ◐ (dash) | Amber highlight | In progress this quarter — treated as complete for prerequisite purposes, not scheduled again |
| ✓ (check) | Faded | Completed — excluded from the plan |

### Step 5 — Choose a mode and generate

Use the **Suggest plan** / **Custom build** tabs in the top-right to switch modes.

---

## Suggest Plan Mode

Click **Generate plan →** to produce a full schedule from your upcoming quarter through degree completion.

The scheduler:
- Respects all prerequisites before placing any course
- Respects quarter availability (primary and alternate offering quarters)
- Targets your specified credit load per quarter (12–18 credit cap enforced)
- **Prioritizes overdue courses** — if a course should have been taken in a prior year but wasn't, it is placed before on-time courses and marked with a purple **delayed** badge
- Distributes electives by type: HSSA electives fill any quarter with space; technical and math/science electives are placed in senior-year quarters; free electives are placed in junior year or later
- Extends into **5th or 6th year** automatically if required courses cannot all fit within four years, with extended quarters clearly labeled

The output displays a Fall/Winter/Spring column grid organized by academic year, matching the layout of the official curriculum flowchart.

### Reading the output

**Course card colors (left border):**

| Color | Type |
|-------|------|
| Red | Core ME requirement |
| Dark blue | HSSA requirement |
| Brown | Capstone sequence (ME 470/471/472) |
| Green | Technical elective |
| Purple | Math/science elective |
| Teal | Free elective |

**Badges on course cards:**
- `alt quarter` — course is being placed in a non-primary offering quarter
- `delayed` — course is being placed later than its standard curriculum year due to unmet prerequisites or credit limits

**Credit display colors:**
- Green — within the 12–18 credit range
- Amber — under 12 credits (flagged)
- Red — over 18 credits (flagged)

---

## Custom Build Mode

Click **Custom build** to manually construct your schedule quarter by quarter.

Each quarter column contains:
- A list of courses and elective slots you have placed there
- A **+ add course…** dropdown to add courses or elective slots
- Live credit total for the quarter

The dropdown organizes courses into two groups: courses normally offered in that quarter, and courses not normally offered (which will be flagged if added). Elective slots show how many of each type remain to be scheduled.

### Validation

Every course card is validated in real time:

| Highlight | Meaning |
|-----------|---------|
| Red background | One or more prerequisites are not satisfied by prior quarters |
| Amber background | Course is not normally offered in this quarter |

Prerequisite checking is cumulative — courses placed in earlier quarters count as satisfied for later quarters, just as they would in a real schedule.

The summary bar at the top tracks progress toward all degree requirements:
- **Core** courses placed vs. total required
- **HSSA**, **Tech**, **Math/Sci**, and **Free** elective counts vs. required

Extended years (5th and 6th) appear automatically in the build grid as you add content to them.

---

## Updating the Curriculum

When the ME curriculum changes, update both `ME_curriculum.csv` and the `COURSES` array inside `me_planner.html`. The HTML does not read the CSV at runtime — both files should be kept in sync manually.

### CSV column reference

| Column | Description |
|--------|-------------|
| `course_id` | Course identifier (e.g., `ME 302`) |
| `title` | Full course name |
| `credits` | Credit hours |
| `year` | Standard curriculum year (Freshman, Sophomore, Junior, Senior, varies) |
| `primary_quarter` | Quarter(s) normally offered, pipe-separated (e.g., `Fall\|Winter`) |
| `alternate_quarters` | Additional quarters when offered, pipe-separated |
| `prerequisites` | Required prior courses, pipe-separated AND conditions |
| `notes` | Mutual exclusions, grade requirements, or other context |

### JavaScript course entry format

Each course in the `COURSES` array in `me_planner.html` follows this structure:

```javascript
{
  id:      "ME 302",
  title:   "Heat Transfer",
  cr:      4,
  year:    "Junior",
  primary: "Spring",
  alt:     "Fall",
  prereqs: [["MA 221"], ["ES 312"]],   // AND of OR-groups
  type:    "core"
}
```

**Prerequisite syntax:** `prereqs` is an array of OR-groups. Every group must be satisfied (AND logic between groups); within a group, any one course satisfies it (OR logic). For example, `[["MA 221"], ["ES 312"]]` means MA 221 AND ES 312 are both required. A group like `[["EM 121", "BE 122"]]` means EM 121 OR BE 122 is required.

**Valid `type` values:** `core`, `hssa`, `capstone`

**Valid `year` values:** `Freshman`, `Sophomore`, `Junior`, `Senior`

---

## Degree Requirements Summary

The planner enforces the following total requirements per the standard 2025 ME curriculum (194 total credits):

| Requirement | Count | Credits each |
|-------------|-------|-------------|
| Required core courses | 34 | varies |
| HUM H190 (First-Year Writing Seminar) | 1 | 4 |
| ENGL H290 (Tech and Prof Communication) | 1 | 4 |
| HSSA Electives | 6 | 4 |
| Technical Electives | 3 | 4 |
| Math/Science Elective | 1 | 4 |
| Free Electives | 2 | 4 |

EM 306 (Vibration Analysis) and ME 306 (Control Systems) are mutually exclusive — students complete one or the other.

---

## Known Limitations

- **Alternate prerequisite equivalencies** — the planner requires the exact course IDs listed in the prerequisite field. Students who satisfied a prerequisite through transfer credit or a cross-listed equivalent should mark that course as complete using the in-progress or done state, which will unlock downstream courses correctly.
- **CHEM 111 / BIO 101** — the degree plan accepts either as the Foundations of Science III requirement. The planner currently schedules CHEM 111 by default. Students who took BIO 101 instead should mark CHEM 111 as complete so ME 328 unlocks correctly, or ask an advisor to confirm equivalency.
- **Elective placement in suggest mode** — electives are distributed by a general rule (HSSA any time, tech/math-sci in senior years, free in junior+). Students with specific elective requirements or restrictions should use Custom Build mode to place electives precisely.
- **Build mode does not auto-save** — the custom grid is held in memory and will reset if the page is refreshed. Export or screenshot your plan before closing.
