import pandas as pd

def calculate_demographic_data(print_data=True):


    # Load data
    df = pd.read_csv("adult.data.csv")

    # 1. Number of each race
    race_count = df["race"].value_counts()

    # 2. Average age of men
    average_age_men = round(df[df["sex"] == "Male"]["age"].mean(), 1)

    # 3. Percentage with Bachelor's degrees
    percentage_bachelors = round((df["education"] == "Bachelors").mean() * 100, 1)

    # 4. Advanced education
    higher_edu = df["education"].isin(["Bachelors", "Masters", "Doctorate"])
    lower_edu = ~higher_edu

    # 5. % with advanced education >50K
    higher_education_rich = round((df[higher_edu]["salary"] == ">50K").mean() * 100, 1)

    # 6. % without advanced education >50K
    lower_education_rich = round((df[lower_edu]["salary"] == ">50K").mean() * 100, 1)

    # 7. Min work hours
    min_work_hours = df["hours-per-week"].min()

    # 8. % earning >50K among those who work min hours
    rich_percentage = round(
        (df[(df["hours-per-week"] == min_work_hours) & (df["salary"] == ">50K")].shape[0] /
         df[df["hours-per-week"] == min_work_hours].shape[0]) * 100, 1)

    # 9. Country with highest % >50K
    rich_by_country = df[df["salary"] == ">50K"]["native-country"].value_counts()
    total_by_country = df["native-country"].value_counts()
    rich_country_percent = (rich_by_country / total_by_country * 100).dropna()
    highest_earning_country = rich_country_percent.idxmax()
    highest_earning_country_percentage = round(rich_country_percent.max(), 1)

    # 10. Top occupation in India among >50K
    top_IN_occupation = df[
    (df["native-country"] == "India") & (df["salary"] == ">50K")
]["occupation"].value_counts().idxmax()
    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
