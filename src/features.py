import pandas as pd


def engineer_features(df):
    """Add engineered features grounded in domain reasoning."""
    df = df.copy()

    df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
    df['IsAlone'] = (df['FamilySize'] == 1).astype(int)

    df['Title'] = df['Name'].str.extract(r',\s*([^\.]*)\.')
    df['Title'] = df['Title'].replace(
        ['Lady', 'Countess', 'Capt', 'Col', 'Don', 'Dr', 'Major',
         'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare'
    )
    df['Title'] = df['Title'].replace(['Mlle', 'Ms'], 'Miss')
    df['Title'] = df['Title'].replace('Mme', 'Mrs')

    df['FarePerPerson'] = df['Fare'] / df['FamilySize']
    df['AgeBucket'] = pd.cut(df['Age'], bins=[0, 12, 60, 100],
                               labels=['Child', 'Adult', 'Senior'])
    df['HasCabin'] = df['Cabin'].notna().astype(int)

    return df


def target_encode_out_of_fold(X_col, y, n_splits=5, seed=42):
    """Target encode a categorical column using out-of-fold means."""
    from sklearn.model_selection import KFold

    encoded = pd.Series(index=X_col.index, dtype=float)
    kf = KFold(n_splits=n_splits, shuffle=True, random_state=seed)
    global_mean = y.mean()

    for train_idx, val_idx in kf.split(X_col):
        train_col = X_col.iloc[train_idx]
        train_y = y.iloc[train_idx]
        val_col = X_col.iloc[val_idx]

        category_means = train_y.groupby(train_col).mean()
        encoded.iloc[val_idx] = val_col.map(category_means).fillna(global_mean)

    return encoded