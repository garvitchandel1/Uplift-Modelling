🚀 Uplift Modeling for Campaign Profit Optimization
🎯 Objective

Traditional marketing models predict who will convert.

This project instead estimates:

Who will convert because of a promotion.

We model incremental impact, not correlation.

📊 Business Problem

Targeting high-probability converters wastes budget on users who would convert anyway.

We reformulate campaign targeting as a causal decision problem:

CATE(x)=P(Y=1∣T=1,X=x)−P(Y=1∣T=0,X=x)
CATE(x)=P(Y=1∣T=1,X=x)−P(Y=1∣T=0,X=x)

Where:

T = Promotion shown

Y = Conversion

X = Customer features

Goal:

Maximize incremental conversions

Maximize campaign profit

Identify optimal targeting fraction

🗂 Dataset

Criteo Uplift Dataset

~14M observations

Randomized treatment assignment

Features: f0–f11

Binary treatment (treatment)

Binary outcome (conversion)

Randomization enables clean causal estimation.

🧠 Modeling Strategy
Baselines

Random Targeting

Conversion Model (XGBoost)

Predicts conversion probability

Ignores treatment effect

Uplift Models
🔹 T-Learner

Separate models for treated & control

Uplift = μ₁(x) − μ₀(x)

🔹 X-Learner

Estimates pseudo treatment effects

Trains regression model on uplift

Handles treatment imbalance (85/15 split)

📈 Evaluation Framework

We do not report accuracy.

We evaluate using:

Uplift Curve

Qini Curve & Qini AUC

Profit Simulation

Policy Curve Optimization

Sensitivity Analysis

SHAP (treatment effect explainability)

💰 Profit Formulation
Profit=(Incremental Conversions×V)−(Users Targeted×C)
Profit=(Incremental Conversions×V)−(Users Targeted×C)

Where:

V
V = Profit per conversion

C
C = Promotion cost

🔥 Key Results

Under realistic economics:

X-Learner Profit: $41,213

Conversion Model Profit: $19,433

Random: Loss

🚀 Improvement

X-Learner improves profit by ~112% over conversion targeting.

🎯 Optimal Policy

Target top ~3% highest-uplift users.

📊 Qini AUC Ranking
| Model         | Qini AUC |
| ------------- | -------- |
| Random        | Lowest   |
| Conversion    | Higher   |
| T-Learner     | Higher   |
| **X-Learner** | Highest  |
Confirms superior uplift ranking quality.

📉 Economic Sensitivity

Campaign remains profitable across a wide range of:

Promotion costs

Conversion margins

Break-even behavior observed under high-cost / low-margin scenarios.

🔍 Explainability (SHAP)

Engagement signals (visit, exposure) drive responsiveness

Clear heterogeneity in treatment effects

Some users exhibit negative uplift

Confirms that treatment effect varies across users.

📁 Project Structure
data/
notebooks/
src/
outputs/
README.md


Modularized into:

data.py

models.py

uplift.py

economics.py

evaluation.py

🏁 Conclusion

Causal uplift modeling:

Outperforms predictive conversion models

Maximizes incremental profit

Identifies optimal targeting policy

Demonstrates economic robustness

Provides interpretable treatment drivers

This project reframes marketing targeting as a causal optimization problem rather than a classification task

## 👤 Author

**Garvit Chandel**  