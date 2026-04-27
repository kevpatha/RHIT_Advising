# RHIT ME Course Planner

An interactive four-year course planning tool for Rose-Hulman Institute of Technology Mechanical Engineering students. Students can generate a suggested schedule or build their own plan quarter by quarter, track elective requirements, and export their schedule to Excel.

---

## Files

| File | Description |
|------|-------------|
| `index.html` | Main application — open this in a browser |
| `ME_curriculum.csv` | All ME courses with credits, contact hours, prerequisites, and availability |
| `plan_standard.csv` | Standard ME plan elective requirements |
| `plan_calculus_abc.csv` | Calculus ABC track plan (MA 113 in summer) |
| `plan_rose2_mem.csv` | Rose² MEM dual-degree plan |
| `plan_rose2_mme.csv` | Rose² MME dual-degree plan |

All files must be in the **same folder**. Open `index.html` directly in a browser — no server required.

---

## Features

### Plan Selection
- **Standard** — default four-year ME track
- **Calculus ABC** — for students completing MA 113 the summer before Sophomore year
- **Rose² MEM / MME** — dual-degree tracks with modified elective requirements

### Configuration
- **Starting year and quarter** — set where in the curriculum you are
- **Show Summer quarter** — toggle Summer quarters on/off
- **Vibrations or Controls** — choose between EM 306 (Vibration Analysis) and ME 306 (Control Systems) for your Junior year elective
- **Pre-RHIT credits** — mark courses completed before arriving at Rose (AP, transfer, etc.)

### Suggest Plan
Clicking **Suggest plan →** generates a full four-year schedule based on:
- Prerequisites and quarter availability for each course
- HSSA elective distribution: 1 per year in Freshman, 1 per year in Junior, 2 in Sophomore, 3 in Senior
- Technical electives held until Senior year
- Free electives placed in Junior and Senior year
- Math/Science elective placed in Junior or Senior year
- Upper-level courses gated behind HSSA slot confirmation each year

### Build Mode
The grid lets you manually add or remove courses and electives quarter by quarter:
- **Course cards** show credit/contact hour counts and flag prerequisite issues in red
- **Delayed** badges appear on courses placed earlier than their standard year
- **Elective slots** can be dragged from the sidebar into any quarter
- The **credit/contact hour summary** updates live as you build

### Export
The **⬇ Excel** button downloads your current plan as a `.xlsx` file with a formatted schedule sheet and a full course list with types and credits.

---

## Elective Requirements (Standard Plan)

| Type | Credits | Slots | Placement |
|------|---------|-------|-----------|
| HSSA | 28 cr | 7 × 4 cr | 1 Frosh, 2 Soph, 1 Junior, 3 Senior |
| Technical | 16 cr | 4 × 4 cr | Senior year only |
| Math/Science | 4 cr | 1 × 4 cr | Junior or Senior |
| Free | 8 cr | 2 × 4 cr | 1 Junior, 1 Senior |

> Named HSSA courses (HUM H190, ENGL H290) satisfy degree requirements separately and are **not** counted against the 28 cr elective total.

---

## Development

### Curriculum Data (`ME_curriculum.csv`)

Each row is a course with these columns:

| Column | Description |
|--------|-------------|
| `course_id` | Unique course identifier (e.g. `ME 321`) |
| `title` | Display name |
| `credits` | Credit hours |
| `contact_hours` | Weekly contact hours (used for ch display) |
| `type` | `core`, `hssa`, or `capstone` |
| `primary_quarter` | Quarters normally offered (semicolon-separated) |
| `alternate_quarters` | Quarters offered less frequently |
| `prerequisites` | Semicolons = AND, `or` = OR within group |
| `plans` | Which plans include this course (`all`, or plan ID) |
| `plan_overrides` | Override year placement per plan (e.g. `all:Junior`) |

### Plan Data (`plan_*.csv`)

Each plan file defines elective credit totals in a fixed row format:

```
hssa_credits, tech_credits, ms_credits, free_credits
28, 16, 4, 8
```

Rose² plans may also list pre-RHIT replacement courses (e.g. MA 111/112 replaced by MA 113/114).

### Prerequisite Syntax

```
MA 221              → requires MA 221
MA 221; ES 201      → requires MA 221 AND ES 201  
MA 111 or MA 113    → requires MA 111 OR MA 113
```

---

## Known Behaviors

- **Calculus ABC plan**: MA 221, 222, 223 are pre-placed into Sophomore Fall/Winter/Spring to anchor the shifted math sequence correctly.
- **EM 306 vs ME 306**: Only one can be selected per plan; the other is excluded from scheduling.
- **Contact hours**: Displayed as `Xcr / Ych` on course cards only when they differ from credit hours.
- **5th year overflow**: If elective requirements can't fit in four years (e.g. very late start quarter), the scheduler will extend into a 5th year row.
