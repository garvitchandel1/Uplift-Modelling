import numpy as np
from xgboost import XGBClassifier, XGBRegressor


def train_conversion_model(X_train, y_train):
    features = [c for c in X_train.columns if c != "treatment"]

    model = XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1,
    )

    model.fit(X_train[features], y_train)
    return model


def train_t_learner(X_train, y_train):
    features = [c for c in X_train.columns if c != "treatment"]

    treated = X_train["treatment"] == 1
    control = X_train["treatment"] == 0

    model_t = XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1,
    )

    model_c = XGBClassifier(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1,
    )

    model_t.fit(X_train.loc[treated, features], y_train.loc[treated])
    model_c.fit(X_train.loc[control, features], y_train.loc[control])

    return model_t, model_c


def train_x_learner(X_train, y_train):
    features = [c for c in X_train.columns if c != "treatment"]

    model_t, model_c = train_t_learner(X_train, y_train)

    mu1 = model_t.predict_proba(X_train[features])[:, 1]
    mu0 = model_c.predict_proba(X_train[features])[:, 1]

    treated = X_train["treatment"] == 1
    control = X_train["treatment"] == 0

    tau = np.zeros(len(X_train))

    tau[treated] = y_train.loc[treated] - mu0[treated]
    tau[control] = mu1[control] - y_train.loc[control]

    effect_model = XGBRegressor(
        n_estimators=200,
        max_depth=6,
        learning_rate=0.1,
        subsample=0.8,
        colsample_bytree=0.8,
        random_state=42,
        n_jobs=-1,
    )

    effect_model.fit(X_train[features], tau)

    return model_t, model_c, effect_model