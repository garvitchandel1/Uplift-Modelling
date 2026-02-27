# 🚀 Uplift Modeling for Campaign Profit Optimization

## 🎯 Objective
Traditional marketing models predict **who will convert**. This project shifts the paradigm to estimate **incremental impact**: identifying users who convert *specifically because* of a promotion.

By modeling the causal effect rather than simple correlation, we move from passive prediction to **active profit optimization**.

---

## 📊 Business Problem
Targeting high-probability converters often wastes budget on "Sure Things"—users who would have purchased regardless of an incentive. We reformulate campaign targeting as a **Conditional Average Treatment Effect (CATE)** problem:

$$CATE(x) = P(Y=1 | T=1, X=x) - P(Y=1 | T=0, X=x)$$

**Where:**
* **$T$**: Promotion shown (Treatment)
* **$Y$**: Conversion (Outcome)
* **$X$**: Customer features

**Goal:** Maximize incremental conversions and campaign ROI by identifying the optimal targeting fraction.

---

## 🗂 Dataset: Criteo Uplift
* **Scale**: ~14M observations.
* **Nature**: Randomized Treatment Assignment (ideal for clean causal estimation).
* **Features**: `f0–f11` (Anonymized).
* **Targeting**: 85/15 treatment/control split.
* **Optimization**: Prototyped on a 2M stratified sample; retrained on the full 14M dataset using memory-optimized dtypes.

---

## 🧠 Modeling Strategy

### Baselines
1. **Random Targeting**: The benchmark for non-informed strategy.
2. **Conversion Model (XGBoost)**: Predicts $P(Y|X)$. It focuses on likely buyers but ignores whether the treatment actually causes the behavior.

### Uplift Models
* **T-Learner**: Uses two separate models (Treatment vs. Control) to calculate $Uplift = \mu_1(x) - \mu_0(x)$.
* **X-Learner**: Designed for unbalanced treatment groups. It estimates pseudo-treatment effects and trains a second-stage regression on the imputed uplift.

---

## 📈 Evaluation Framework
We avoid standard classification metrics (Accuracy/F1) in favor of causal metrics:
* **Uplift & Qini Curves**: Measuring cumulative incremental gain.
* **Qini AUC**: Quantifying the model's ability to rank users by treatment responsiveness.
* **Policy Curve Optimization**: Finding the "sweet spot" for population saturation.
* **SHAP**: For treatment effect explainability.

---

## 💰 Profit Formulation & Results
We define profit as:
$$\text{Profit} = (\text{Incremental Conversions} \times V) - (\text{Users Targeted} \times C)$$

**Where:**
* **$V$** = Profit per conversion
* **$C$** = Cost per promotion

### 🔥 Key Performance Comparison
| Model | Qini AUC | Max Profit (14M Scale) |
| :--- | :--- | :--- |
| **X-Learner** | **Highest** | **$134,804** |
| T-Learner | High | $118,200 |
| Conversion Model | Medium | $19,433 |
| Random | Lowest | (Loss) |

> **🚀 Result:** X-Learner improves profit by **~112%** over traditional conversion targeting.
> **🎯 Policy:** The optimal strategy targets the **top ~3%** highest-uplift users.

---

## 🔍 Insights & Explainability
* **SHAP Analysis**: Engagement signals (visit, exposure) drive the highest responsiveness.
* **Heterogeneity**: Clear evidence that treatment effects vary; some users exhibit negative uplift (they are discouraged by the ad).
* **Stability**: The optimal targeting fraction (~3%) remained consistent when scaling from the 2M prototype to the full 14M dataset.

---

## 📁 Project Structure
text
├── data/        # Criteo raw and processed samples
├── notebooks/   # EDA, Prototyping, and Visualization
├── src/         # Modular Python scripts
│   ├── data.py       # Preprocessing & Memory Optimization
│   ├── models.py     # T-Learner & X-Learner Implementations
│   ├── uplift.py     # Causal Logic
│   ├── economics.py  # Profit & Sensitivity Analysis
│   └── evaluation.py # Qini & Metrics Logic
└── README.md

---

## 🏁 Conclusion

By reframing marketing targeting as a **causal optimization problem** rather than a simple classification task, this project demonstrates how data science directly impacts the bottom line. 

**Key Takeaways:**
* **Precision over Volume**: Targeting the top **3%** of users yielded the maximum profit, proving that "less is more" when incentives are involved.
* **Causal Dominance**: The **X-Learner** outperformed traditional conversion models by **112%**, identifying users who only convert when prompted.
* **Economic Resilience**: Sensitivity analysis confirmed the model's profitability remains robust across varying promotion costs and conversion margins.

This approach ensures marketing spend is no longer a "sunk cost" but a calculated investment in incremental growth.

---

## 👤 Author

**Garvit Chandel** [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/your-profile) 
[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white)](https://github.com/your-username) 
[![Portfolio](https://img.shields.io/badge/Portfolio-4CAF50?style=flat&logo=google-chrome&logoColor=white)](https://yourportfolio.com)

---
