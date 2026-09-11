# 🚀 Day 99: Space Race Analysis

> _67 years of humanity reaching for the stars — analyzed, visualized, and decoded._

---

## 💡 The Concept

A comprehensive data science analysis of **6,711 space launches** spanning from Sputnik 1 (1957) to 2024. Explores which countries dominated the space race, which organizations succeed most, how launch costs evolved, and how activity shifted across decades.

---

## 📊 Dataset Overview

| Field | Description |
|---|---|
| `Organisation` | Launch organization (SpaceX, NASA, ISRO, etc.) |
| `Location` | Launch site and country |
| `Datetime` | Launch date and time (UTC) |
| `Details` | Rocket name and mission payload |
| `Rocket_Status` | Active / Retired |
| `Price` | Launch cost in millions USD |
| `Mission_Status` | Success / Failure / Partial Failure |

- **6,711 total launches** · **66 unique organizations** · **22 countries**
- Price data available for **2,637** of 6,711 launches

---

## 🔬 Analysis Performed

### 🌍 Country-Level Analysis
```
Success Rate by Country:
🥇 China Coastal Waters  → 100.0%
🥈 Russia                →  94.3%
🥉 France                →  93.8%
   China                 →  93.6%
   USA                   →  89.9%
   India                 →  83.7%
   North Korea           →  37.5%
```

### 🏢 Organization-Level Analysis
```
Top Organizations (50+ launches):
1. ULA          → 99.4% success rate
2. Boeing       → 96.4%
3. SpaceX       → 96.2%
4. Arianespace  → 96.0%
5. CASC         → 95.4%
   ...
   ISRO         → 83.7%  (77 successes, 10 failures)
```

### 📅 Launches Per Decade
```
1950s →    49 launches  (Space Race begins)
1960s → 1,007 launches  (Apollo era)
1970s → 1,238 launches  ← Peak decade
1980s → 1,192 launches
1990s →   891 launches
2000s →   667 launches
2010s →   905 launches  (Commercial era)
2020s →   722 launches  (ongoing)
```

### 💰 Launch Cost Insights
```
Most expensive org (avg):  NASA     → $453.11M
Cheapest org (avg):        Astra    →   $2.50M
Overall avg price:                  →  $69.16M
```

---

## 🛠️ Feature Engineering

```python
# Country extracted from location string
df["Country"] = df["Location"].str.split(",").str[-1].str.strip()

# Datetime normalized
df["Datetime"] = pd.to_datetime(df["Datetime"]).dt.strftime("%Y-%m-%d")

# Decade column added
df["Decade"] = ((pd.to_datetime(df["Datetime"]).dt.year // 10) * 10)
```

---

## 📦 Dependencies

```bash
pip install pandas numpy matplotlib plotly seaborn
```

---

## ▶️ Run It

```bash
jupyter notebook Day99.ipynb
```

---

## 📁 Files

| File | Description |
|---|---|
| `Day99.ipynb` | Full analysis notebook — cleaning, EDA, visualizations |
| `space_races.csv` | Dataset of 6,711 space launches (1957–2024) |
