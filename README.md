# ME Course Planner — Rose-Hulman Institute of Technology

A browser-based tool that helps Mechanical Engineering students plan their remaining coursework through graduation. Students select their completed courses, configure their situation, and either generate a full suggested schedule or build their own manually with live validation.

Supports four curriculum plans, optional summer quarters, and automatic extended enrollment planning up to six years.

---

## Files

All files must be kept in the same folder for the tool to work.

| File | Description |
|------|-------------|
| `me_planner.html` | The course planner application |
| `ME_curriculum.csv` | Master course list — all ME courses with credits, prerequisites, and quarter availability |
| `plan_standard.csv` | Standard 4-year ME plan |
| `plan_calculus_abc.csv` | Calculus ABC plan (MA 105/106/107 entry path) |
| `plan_rose2_mme.csv` | Rose² MME plan (accelerated BS+MS, Management of Engineering track) |
| `plan_rose2_mem.csv` | Rose² MEM plan (accelerated BS+MS, Mechanical Engineering track) |
| `README.md` | This file |

---

## Opening the Tool

The planner loads course data from the CSV files at startup using `fetch()`, so **all files must be in the same folder** and served over a web server or local server. Opening `me_planner.html` directly from your file system may fail in some browsers (particularly Chrome) due to local file access restrictions.

**Option 1 — Local server (recommended for local use):**
Navigate to the folder in a terminal and run:
```
python -m http.server
```
Then open `http://localhost:8000/me_planner.html` in your browser.

**Option 2 — Web server:**
Upload all files to any static web hosting location and open the URL.

**Option 3 — Firefox:**
Firefox generally allows local `fetch()` without a server. Opening the file directly in Firefox should work.

---

## How to Use

### Step 1 — Select your curriculum plan

Use the tabs in the header to select the plan that matches your enrollment:

| Tab | Description |
|-----|-------------|
| Standard | Standard 4-year ME plan. Requires both CHEM 111 and BIO 101. |
| Calculus ABC | For students who entered via MA 105/106/107. MA 113 is required as a summer course between Year 1 and Year 2. |
| Rose² MME | Accelerated BS+MS plan (Management of Mechanical Engineering). Pre-RHIT credits cover MA 111/112, PH 111, CHEM 111, and electives. |
| Rose² MEM | Accelerated BS+MS plan (Mechanical Engineering Management). Same structure as Rose² MME with different graduate elective focus. |

### Step 2 — Configure your settings (left panel)

| Setting | Description |
|---------|-------------|
| Upcoming quarter | The next quarter you will enroll in (Fall, Winter, Spring, or Summer) |
| Year standing | Your current academic year |
| Target cr/quarter | Desired credit load per quarter, between 12 and 18 (Suggest mode only) |
| Control course | Choose EM 306 (Vibration Analysis) or ME 306 (Control Systems) — only one is required |
| Show summer | Toggle whether summer quarters are displayed in the plan grid |

### Step 3 — Enter completed electives

Use the counters below the settings to record how many of each elective type you have already completed. Required counts vary by plan:

| Elective type | Standard / Calc ABC | Rose² MME / MEM |
|---------------|--------------------:|----------------:|
| HSSA Electives | 6 | 5 |
| Technical Electives | 3 | 3 |
| Math/Science Elective | 1 | 1 |
| Free Electives | 2 | 0 (satisfied by pre-RHIT credits) |

HUM H190 and ENGL H290 are tracked individually as named courses, not counted in the elective counters.

### Step 4 — Mark completed courses

The course list shows all required courses for the selected plan, grouped by year. Click each course to cycle through three states:

| State | Appearance | Meaning |
|-------|-----------|---------|
| □ (empty) | Normal | Not yet taken — will be scheduled |
| ◐ (dash) | Amber highlight | In progress this quarter — counted as complete for prerequisites, not rescheduled |
| ✓ (check) | Faded | Completed — excluded from the plan |

**Note on CHEM 111 and BIO 101:** Both courses are required in the Standard plan and both satisfy each other's downstream prerequisite (ME 328). Mark whichever you have completed and the other will unlock correctly.

### Step 5 — Choose a mode and generate

Use the **Suggest** / **Build** tabs in the top-right corner of the header to switch modes.

---

## Suggest Plan Mode

Click **Generate plan →** to produce a full schedule from your upcoming quarter through graduation.

The scheduler respects all prerequisites and quarter availability, targets your specified credit load, and places electives following the pattern of the selected plan. Key behaviors:

- **Overdue courses are prioritized** — if a course should have been taken in a prior year, it is placed as early as prerequisites allow and marked with a purple **delayed** badge
- **Summer quarters** — shown as a fourth column when enabled; the required MA 113 summer course in the Calculus ABC plan appears automatically
- **Extended enrollment** — the plan extends into a 5th or 6th year automatically if all requirements cannot fit within four years, clearly labeled in the grid

### Reading the output

**Course card colors (left border):**

| Color | Meaning |
|-------|---------|
| Red | Core ME requirement |
| Dark blue | HSSA requirement |
| Brown | Capstone sequence (ME 470 / 471 / 472) |
| Green | Technical elective |
| Purple | Math/science elective |
| Teal | Free elective |
| Dark teal | Summer course |

**Badges on cards:**
- `alt` — course is placed in a non-primary offering quarter
- `delayed` — course is placed later than its standard curriculum year

**Quarter credit totals:** green = within range, amber = under 12, red = over 18.

For Rose² plans, pre-RHIT and transfer credits appear in a separate section below the plan grid.

---

## Custom Build Mode

Switch to **Custom build** to manually place courses quarter by quarter across up to six years (including summer quarters when enabled).

Each quarter column has a **+ add…** dropdown to place courses or elective slots. Courses are grouped into those normally offered in that quarter and those that are not (which will be flagged). Elective slots show how many of each type remain.

### Live validation

| Highlight | Meaning |
|-----------|---------|
| Red card background | One or more prerequisites not satisfied by earlier quarters |
| Amber card background | Course not normally offered in this quarter |

Prerequisite checking is cumulative — courses placed in earlier quarters count as satisfied for later ones. Courses marked as completed or in-progress in the left panel also count.

The summary bar tracks overall degree progress: core courses placed or completed vs. total required, and each elective type vs. its required count.

---

## Updating the Curriculum

### Adding or changing a course — `ME_curriculum.csv`

Each row is one course. Column reference:

| Column | Description |
|--------|-------------|
| `course_id` | Course identifier (e.g., `ME 302`) |
| `title` | Full course name |
| `credits` | Credit hours |
| `year` | Standard curriculum year |
| `primary_quarter` | Quarter(s) normally offered, semicolon or pipe-separated |
| `alternate_quarters` | Additional offering quarters, semicolon or pipe-separated |
| `prerequisites` | Semicolons separate AND conditions; `or` separates options within a group (e.g., `PH 111; EM 121; MA 113` or `CHEM 111 or CHEM 112`) |
| `notes` | Additional context |

### Changing a plan's schedule — `plan_*.csv`

Each plan file has four sections identified by header rows:

**Metadata row** (`plan_id, plan_name, total_credits, notes`) — plan name and any note displayed to the student.

**`elective_requirements` section** — one row per elective type defining its label and required count:
```
type,label,count
hssa,HSSA Elective,6
tech,Technical Elective,3
ms,Math/Science Elective,1
free,Free Elective,2
```

**`pre_rhit_credits` section** — courses completed before enrollment, shown below the plan grid (Rose² plans only):
```
course_id,title,credits
MA 111,Calculus I,5
```

**`schedule` section** — one row per course slot:
```
year_num,year_label,quarter,course_id,title,credits,slot_type
1,Freshman,Fall,MA 111,Calculus I,5,core
1,Freshman,Fall,HSSA Elective,,4,elective-hssa
1,Freshman,Summer,MA 113,Calculus III,5,core
```

Valid `slot_type` values: `core`, `hssa`, `capstone`, `elective-hssa`, `elective-tech`, `elective-ms`, `elective-free`

For elective slots, `course_id` and `title` may be left blank. For summer courses, set `quarter` to `Summer`.

---

## Degree Requirements Summary

| Requirement | Standard | Calc ABC | Rose² MME | Rose² MEM |
|-------------|:--------:|:--------:|:---------:|:---------:|
| Total credits | 194 | 197 | 194 | 194 |
| HSSA Electives | 6 | 6 | 5 | 5 |
| Technical Electives | 3 | 3 | 3 | 3 |
| Math/Science Elective | 1 | 1 | 1 | 1 |
| Free Electives | 2 | 2 | 0 | 0 |
| Summer course required | — | MA 113 | — | — |
| Pre-RHIT credits required | — | — | 30 cr | 30 cr |

EM 306 (Vibration Analysis) and ME 306 (Control Systems) are mutually exclusive across all plans.

---

## Known Limitations

- **Alternate prerequisite equivalencies** — the planner uses exact course IDs from `ME_curriculum.csv`. Students who satisfied a prerequisite through transfer credit or a cross-listed equivalent should mark the Rose-Hulman equivalent as in-progress or done to unlock downstream courses correctly.
- **Rose² elective specialization** — MME Core and MEM Tech Focus elective slots are treated as standard technical elective slots for scheduling purposes. Consult your advisor for approved graduate course selections.
- **Build mode does not save** — the custom build grid is held in memory and resets on page refresh. Screenshot or record your plan before closing.
- **Plan switching resets elective counters** — switching plans clears elective completion counts since requirements differ between plans. Course completion states are preserved.
