import numpy as np


def compute_profit(df, score_col, cost, profit):
    df = df.sort_values(score_col, ascending=False).reset_index(drop=True)

    n = len(df)
    fractions = np.linspace(0.01, 1.0, 50)
    profits = []

    for frac in fractions:
        k = int(frac * n)
        subset = df.iloc[:k]

        treated = subset["treatment"] == 1
        control = subset["treatment"] == 0

        conv_t = subset.loc[treated, "conversion"].sum()
        conv_c = subset.loc[control, "conversion"].sum()

        if control.sum() > 0:
            control_rate = conv_c / control.sum()
        else:
            control_rate = 0

        incremental = conv_t - control_rate * treated.sum()

        total_profit = incremental * profit - k * cost
        profits.append(total_profit)

    return fractions, profits