# DP2-Python-Final-Project

Members: Yuna Fang (yunafang), Yining Liang(liangyn17), Yankun Jiang (yj1084)

GithubRepoName: git@github.com:Lucas-Jiang-9723/DP2-Python-Final-Project.git

Research Question:
Equity of education: Does having a higher education elevate people’s social status in the U.S.?
Students from high income families while parents did not have a college or university degree are likely to have an increase in social status as compared to those from disadvantaged families (Braga, McKernan, Ratcliffe, & Baum, 2017). What is the equity of education? Equity of education can be viewed to mean that schools, as well as education systems, ensure the same learning opportunities for all students irrespective of their financial backgrounds. Can we say there is equity in education? Does it help in elevating an individual social status? To some extent, higher education can boost people’s social status in the U.S. However, it is vital to note that not all graduates from low-income families share the same benefits and access to the best universities in the country, which guarantee a better chance to improve one’s social status. Our research question will help understand whether the higher education institution one attends plays a positive role in elevating one’s social status. Moreover, this helps understand which other factors lead to social status apart from higher education. For example, factors such as parents' previous education level, family income and the cultural experience of the student in the family also have a significant impact on social status. We also show the mean wage for different genders under different educational attainment levels to take a glance at other potential inequalities on education outcomes.

Methodology:

Data1-mrc_tables: 
The data we used comes from the data website provided in the Mobility Report Cards article: http://www.equality-of-opportunity.org/data/. It provides a dataset of all college students from 1999-2013 that describes the income distribution of parents and children for each college in the United States. The raw data comes from the Social Security Administration, the Federal Income Tax Returns, and Department of Education data for 1996-2014. They included each student's date of birth, gender, social security number, and individual taxpayer status. We used two features, seaborn and matplotlib, as well as individual pandas data processing functions in the first graph. The pandas in the first one is mainly used to group data and find the mean. The second one uses pandas, matplotlib and numpy to plot the image. The pandas in the second one is mainly used to filter the data in LA state. Moreover, the second plot shows that there is a positive linear relationship between the parents’ income and children’s income, so we decided to use this as our model to fit.

Data-acs_merge & us-state-ansi-fips:
We used API to retrieve the data from American Census Bureau’s 2019 American Community Survey for state fips, gender, age, wage, and educational attainment for the survey takers. We merged the ACS data with the US State Fips code file to easily convert the fips codes to state names for later usage in the shiny app.

NLP: 
For the NLP part, we mainly use two packages - Beautiful Soup and Requests. We used those two packages to retrieve the text content from Mckinsey’s report on racial and ethnic equity in US higher education. Then re package is used to cleanse the unwanted elements in the content retrieved. Lastly we did an analysis on polarity and subjectivity of the report.

Shiny app: 
We built a shiny app to showcase two interactive plots - one for mean wage against genders of survey takers using educational attainment as a dummy variable hue, and the other for mean wage against different age groups of the survey takers, using educational attainment as a dummy variable as well. The interactive part is revealed through the choices of states that the survey takers are from.


Data results and analysis:
Result 1: 
From the first static plot(static1.png) , we can observe that the higher the university ranking, the higher the kid's salary. This indicates that a college degree can significantly improve a person's job prospects and earning potential. From the second plot of the linear fit(static2 and model fitting.png), we can observe that parents' wages are positively correlated with children's wages. This means that parents with higher incomes are likely to have higher levels of human capital, making them more capable of supporting their children to complete their education. 

Result 2 - displayed through the shiny app images: 
Across the age groups, it appears that on average, ones with higher educational attainment levels have a higher wage than those with lower levels across states. And that across states, on average, males appear to have higher wages than females, controlling educational attainment levels.

                                                                     References
Braga, B., McKernan, S.-M., Ratcliffe, C., & Baum, S. (2017). Wealth inequality is a barrier      to education and Social Mobility. Wealth Inequality Is a Barrier to Education and Social Mobility. Retrieved May 22, 2022, from https://www.urban.org/sites/default/files/publication/89976/wealth_and_education_3.pdf
