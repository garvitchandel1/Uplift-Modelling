# 🚀 Uplift Modeling for Campaign Profit Optimization

## 🎯 Objective
Traditional marketing models predict **who will convert**. This project shifts the paradigm to estimate **incremental impact** — identifying users who convert *specifically because* of a promotion.

By modeling the causal effect rather than simple correlation, we move from passive prediction to **active profit optimization**.

---

## 📊 Business Problem
Targeting high-probability converters often wastes budget on "Sure Things" — users who would have purchased regardless of an incentive. We reformulate campaign targeting as a **Conditional Average Treatment Effect (CATE)** problem:

\[
CATE(x) = P(Y=1 \mid T=1, X=x) - P(Y=1 \mid T=0, X=x)
\]

**Where:**
- **T**: Promotion shown (Treatment)  
- **Y**: Conversion (Outcome)  
- **X**: Customer features  

**Goal:** Maximize incremental conversions and campaign ROI by identifying the optimal targeting fraction.

---

## 🗂 Dataset: Criteo Uplift
- **Scale**: ~14M observations  
- **Nature**: Randomized treatment assignment (ideal for clean causal estimation)  
- **Features**: `f0–f11` (anonymized)  
- **Split**: 85/15 treatment/control  
- **Optimization Strategy**:  
  - Prototyped on a 2M stratified sample  
  - Retrained on the full 14M dataset using memory-optimized dtypes  

---

## 🧠 Modeling Strategy

### Baselines
1. **Random Targeting** — Benchmark for non-informed strategy  
2. **Conversion Model (XGBoost)** — Predicts \( P(Y \mid X) \); identifies likely buyers but ignores incremental causality  

### Uplift Models
- **T-Learner**  
  - Two separate models (treatment vs. control)  
  - Uplift = \( \mu_1(x) - \mu_0(x) \)

- **X-Learner**  
  - Designed for unbalanced treatment groups  
  - Estimates pseudo-treatment effects  
  - Trains second-stage regression on imputed uplift  

---

## 📈 Evaluation Framework
Instead of traditional classification metrics (Accuracy/F1), we use causal evaluation metrics:

- **Uplift & Qini Curves** — Cumulative incremental gain  
- **Qini AUC** — Ranking quality for treatment responsiveness  
- **Policy Curve Optimization** — Identifying optimal population saturation  
- **SHAP Analysis** — Treatment effect interpretability  

---

## 💰 Profit Formulation & Results

Profit is defined as:

\[
\text{Profit} = (\text{Incremental Conversions} \times V) - (\text{Users Targeted} \times C)
\]

**Where:**
- **V** = Profit per conversion  
- **C** = Cost per promotion  

### 🔥 Key Performance Comparison

| Model              | Qini AUC | Max Profit (14M Scale) |
|--------------------|----------|------------------------|
| **X-Learner**      | Highest  | **$134,804**           |
| T-Learner          | High     | $118,200               |
| Conversion Model   | Medium   | $19,433                |
| Random             | Lowest   | Negative               |

**Result:**  
The **X-Learner** improves profit by **~112%** over traditional conversion targeting.

**Optimal Policy:**  
Target the top **~3%** highest-uplift users.

---

## 🔍 Insights & Explainability
- **SHAP Analysis** — Engagement signals (visits, exposure) drive the highest responsiveness  
- **Heterogeneous Effects** — Some users exhibit negative uplift (discouraged by promotion)  
- **Stability** — Optimal targeting fraction (~3%) remained consistent when scaling from 2M to 14M observations  

---

## 📁 Project Structure

```text
.
├── data/               # Criteo raw and processed samples
├── notebooks/          # EDA, prototyping, visualization
├── src/                # Modular Python scripts
│   ├── data.py         # Preprocessing & memory optimization
│   ├── models.py       # T-Learner & X-Learner implementations
│   ├── uplift.py       # Causal logic
│   ├── economics.py    # Profit & sensitivity analysis
│   └── evaluation.py   # Qini & metrics logic
├── .gitignore
└── README.md
```

---

## 🏁 Conclusion
By reframing marketing targeting as a **causal optimization problem** rather than a classification task, this project demonstrates direct bottom-line impact.

### Key Takeaways
- **Precision over Volume** — Targeting the top **3%** maximized profit  
- **Causal Dominance** — X-Learner outperformed conversion targeting by **112%**  
- **Economic Robustness** — Profitability remained stable across varying promotion costs and margins  

Marketing spend transitions from a sunk cost to a calibrated investment in incremental growth.

---

## 👤 Author

**Garvit Chandel**  
[LinkedIn](https://www.linkedin.com/in/your-profile)  
[GitHub](https://github.com/your-username)  
[Portfolio](https://yourportfolio.com)
