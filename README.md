# CIS3330-CODE-6-Descriptive-Analytics
## Instructions

In this CODE assignment, you will begin your business analytics training. This CODE assignment has the following two parts:

1. Python code implementation for producing descriptive statistics and annual reports of the big mac index.
  + Implement in the file **'code_6.py'** the code for the following functions
    + `get_describe_country`
      * The function receives a country code and calculates descriptive statistics for the country's data.
      * The function returns the descriptive statistics for the country.
    + `get_country_groupby_year`
      * The function receives a country code and calculates a report (e.g., descriptive statistics) that is aggregated by year
      * The function returns the report by year.
    + This part of the assignment will have automated grading on GitHub Classrooms.
2. Report on descriptive analytics that compares the big mac prices of five countries.
  + Post a question that can be answered using descriptive analytics.
  + Answer your descriptive analytics question by using the code implemented in **Part 1** of this assignment, other code you implement (optional) and the visualizations we learned in Week 8.
  + Include all the programming code for this part of the assignment inside the `if __name__ == "__main__":` statement.
  + Create a report in Word or Jupyter notebooks.
  + Upload your report to both this code repository and to Blackboard.

  ## Useful Python statements

  * Describe function in python produces descriptive statistics. To use (call) it you need to execute `df.describe`. 
    + Note that **'df'** is a generic DataFrame used in this example and that the describe function can also be used on a `Pandas.Series` data structure.
  * A boxplot can be created on a Pandas DataFrame or Series using the function `boxplot`. See the following example:
    + `df_country.boxplot(column='local_price')` creates a boxplot for the column local_price.
    + `df_country.boxplot(column='local_price', by='name')`creates a boxplot for the column local_price by the country names
   * A scatter plot can be created on a Pandas DataFrame or Series using the function `plot.scatter`. See the following example:
    + `plot.scatter(x='x_variable',y='y_variable')` creates a scatter plot for the given variables.
   * **Important** you need to import `import matplotlib.pyplot as plt` and execute the statement `plt.show()` to show your visualizations.
 
