# 🚨 Day 100: Fatal Police Shootings Analysis

> _The final capstone. Data science applied to one of America's most pressing social justice issues._

---

## 💡 The Concept

A comprehensive data science investigation into **10,430 fatal police shootings** across the United States from **January 2015 to December 2024**. Three datasets are merged, cleaned, and analyzed to uncover patterns across race, age, mental illness, weapon type, flee status, and geography — then cross-referenced with state-level crime statistics.

---

## 📊 Datasets

| Dataset | Rows | Description |
|---|---|---|
| `fatal-police-shootings-data.csv` | 10,430 | Individual shooting incidents (2015–2024) |
| `fatal-police-shootings-agencies.csv` | 3,727 | Law enforcement agencies involved |
| `state_crime.csv` | ~3,000 | State-level crime rates (1960–present) |
| `Final_shooting_dataset.csv` | 9,514 | Merged & cleaned master dataset |

---

## 🔄 Data Pipeline

```
fatal-police-shootings-data.csv
        │
        ▼ explode agency_ids (one row per agency)
        │
        ▼ merge with agencies on agency_ids ←── fatal-police-shootings-agencies.csv
        │
        ▼ drop: id_agency, race_source, location_precision, county
        │
        ▼ fill nulls: race/flee/armed/gender → "Unknown"
        │              age → median (36.0)
        │
        ▼ drop rows missing: threat_type, city, lat/lon
        │
        ▼ add: Decade column, year column
        │
        ▼
Final_shooting_dataset.csv  (9,514 rows · 21 columns · 0 nulls)
```

---

## 🧹 Data Quality

```
Original combined rows:  14,157
Final clean rows:          9,514
Data retained:             67.2%
Duplicates:                    0
Null values remaining:         0
```

---

## 📋 Final Dataset Schema

| Column | Type | Description |
|---|---|---|
| `id_police` | int | Incident ID |
| `date` | datetime | Date of shooting |
| `threat_type` | str | point / attack / move / shoot / etc. |
| `flee_status` | str | not / foot / car / Unknown |
| `armed_with` | str | gun / knife / unarmed / replica / etc. |
| `city` / `state` | str | Location |
| `latitude` / `longitude` | float | GPS coordinates |
| `name_police` | str | Victim name |
| `age` | float | Victim age (median-filled) |
| `gender` | str | male / female / Unknown |
| `race` | str | W / B / H / A / N / O / Unknown |
| `mentally_ill` | bool | Mental illness involved |
| `body_camera` | bool | Officer had body camera |
| `name_agency` | str | Agency name |
| `type` | str | local_police / sheriff / state_police |
| `total_shootings` | float | Agency's total shooting count |
| `Decade` | Int64 | 2010 or 2020 |

---

## 📈 Key Findings

### Incidents Per Year
```
2015 → 1,076   ← highest recorded year
2016 → 1,013
2017 →   958
2018 →   922
2019 →   920
...
```

### Victim Demographics
```
Average age:   37.6 years
Youngest:       0 years
Oldest:        91 years
Std deviation: 12.9 years
```

### Cross-Referenced with State Crime Data
- State-level violent crime rates (assault, murder, robbery, rape)
- Property crime rates per 100,000 population
- Historical data from 1960 to present for trend analysis

---

## 🛠️ Tech Stack

| Tool | Role |
|---|---|
| `pandas` | Data loading, merging, cleaning, aggregation |
| `numpy` | Numerical operations |
| `plotly.express` | Interactive visualizations |
| `matplotlib` / `seaborn` | Static charts |

---

## 📦 Dependencies

```bash
pip install pandas numpy matplotlib seaborn plotly
```

---

## ▶️ Run It

```bash
jupyter notebook Day100.ipynb
```

---

## 📁 Files

| File | Description |
|---|---|
| `Day100.ipynb` | Full analysis — cleaning, merging, EDA, visualizations |
| `fatal-police-shootings-data.csv` | Raw incident data (Washington Post) |
| `fatal-police-shootings-agencies.csv` | Agency metadata |
| `state_crime.csv` | State crime statistics (1960–present) |
| `Final_shooting_dataset.csv` | Merged, cleaned master dataset |

---

> _"The goal is to turn data into information, and information into insight."_
> — This is what Day 100 is about. 🎓
