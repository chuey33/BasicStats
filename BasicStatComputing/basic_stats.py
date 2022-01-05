# Author: Colin Huey
# Date: 1/3/2021
# Description: The following code takes the imported module "statistics" and utilizes it's functions to calculate the
# mean, median, and mode of a given list of people and their respective ages.


import statistics  # Imports module statistics containing mathematical functions.


class Person:
    """"Makes a class Person which represents peoples names and ages."""

    def __init__(self, p_name, p_age):
        """Initializes the variables."""
        self.p_name = p_name  # initializes variable p_name as given persons' names
        self.p_age = p_age  # initializes variable p_age as given persons' ages

    def get_age(self, p_age):
        """Get function to be able to obtain age from list."""
        return p_age  # Returns a called person's age.


def basic_stats(list_of_people):
    """Returns name and age of people and calculates the mean, median, and mode of for each person's age."""
    age_list = []  # Empty list to hold people's ages.

    for i in list_of_people:
        age_list.append(i.p_age)
    mean_age = statistics.mean(age_list)  # Use mean function in "statistics" to calculate mean of the ages.
    median_age = statistics.median(age_list)  # Use median function in "statistics" to calculate median of the ages.
    mode_age = statistics.mode(age_list)  # Use mode function in "statistics" to calculate mode of the ages.
    return mean_age, median_age, mode_age  # Returns calculated mean, median and mode values.