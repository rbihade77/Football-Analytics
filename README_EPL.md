
# 📊 English Premier League (EPL) Attacking Players Analysis

## 🧾 Project Overview

This project focuses on analyzing and visualizing the performance of attacking players in the English Premier League (EPL) for a recent season. The analysis includes key offensive metrics such as Goals, Shots on Target, Expected Goals (xG), and conversion efficiency to gain insights into team attacking performance.

---

## 🗂️ Dataset

The dataset used is an Excel file named `attacking_players_filtered.xlsx`, which includes the following columns:
- `Squad` – Team name
- `Gls` – Goals scored
- `SoT` – Shots on Target
- `xG` – Expected Goals
- `G/Sh` – Goals per Shot
- `G/SoT` – Goals per Shot on Target
- `G-xG` – Over/Underperformance compared to xG
- `np:G-xG` – Over/Underperformance for non-penalty xG

---

## 📈 Key Analysis

1. **Top Teams Analysis:**
   - Sorted by `Gls`, `SoT`, `xG`, `G/Sh`, `G/SoT`, `G-xG`, and `np:G-xG`.

2. **Overperformance and Underperformance:**
   - Compared actual goals with expected goals (`xG`) and non-penalty xG.

3. **Visualizations:**
   - **Bar Chart:** Goals scored by each team.
   - **Scatter Plots:**
     - Shots vs. Goals
     - Goals/Shots vs. Total Goals
     - Goals/Shot on Target vs. Total Goals
   - **Grouped Bar Chart:** Comparison between actual goals and xG by team.

---

## 📌 How to Run

1. Make sure you have the required libraries installed:
   ```bash
   pip install pandas matplotlib seaborn openpyxl
   ```

2. Place your dataset file `attacking_players_filtered.xlsx` in the appropriate directory or update the file path in the script.

3. Run the Python script:
   ```bash
   python "English Premier League (EPL).py"
   ```

---

## 🛠 Tools & Libraries Used

- **Python**
- **Pandas** for data manipulation
- **Matplotlib & Seaborn** for data visualization

---

## 📬 Output Highlights

- Visual insights into goal-scoring efficiency.
- Identification of teams outperforming or underperforming based on expected goals.
- Interactive graphs useful for performance reviews and coaching decisions.

---

## 👤 Author

**Rohit Bihade**

GitHub: [rbihade77](https://github.com/rbihade77)
