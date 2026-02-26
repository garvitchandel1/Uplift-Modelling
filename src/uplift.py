import numpy as np


def predict_t_learner(model_t, model_c, X):
    features = [c for c in X.columns if c != "treatment"]
    mu1 = model_t.predict_proba(X[features])[:, 1]
    mu0 = model_c.predict_proba(X[features])[:, 1]
    return mu1 - mu0


def predict_x_learner(effect_model, X):
    features = [c for c in X.columns if c != "treatment"]
    return effect_model.predict(X[features])


def compute_qini(df, score_col):
    df = df.sort_values(score_col, ascending=False).reset_index(drop=True)

    treated = df["treatment"] == 1
    control = df["treatment"] == 0

    cum_treated = (df["conversion"] * treated).cumsum()
    cum_control = (df["conversion"] * control).cumsum()

    cum_treated_n = treated.cumsum()
    cum_control_n = control.cumsum()

    control_rate = np.where(
        cum_control_n > 0,
        cum_control / cum_control_n,
        0,
    )

    incremental = cum_treated - control_rate * cum_treated_n
    return incremental