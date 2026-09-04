import pandas as pd


def load_data(path):
    """Load raw CSV data."""
    return pd.read_csv(path)


def clean_titanic(df):
    """Clean the Titanic dataset: handle missing values, fix dtypes."""
    df = df.drop_duplicates()
    df['Age'] = df['Age'].fillna(df['Age'].median())
    df = df.drop(columns=['Cabin'])
    df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

    df['Survived'] = df['Survived'].astype('category')
    df['Pclass'] = df['Pclass'].astype('category')
    df['Sex'] = df['Sex'].astype('category')
    df['Embarked'] = df['Embarked'].astype('category')

    df['Sex'] = df['Sex'].str.lower().str.strip()
    df['Embarked'] = df['Embarked'].str.upper().str.strip()

    return df


def save_processed(df, path):
    """Save cleaned data to processed folder."""
    df.to_csv(path, index=False)