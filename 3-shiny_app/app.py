"""
Import packages
"""
from shiny import App, render, ui, reactive
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
acs_sample = pd.read_csv(r"C:\Users\Lucas Jiang\OneDrive - The University of Chicago\MPP\Fall 2022\DAP2-Python\Final Project\data\acs_merge.csv")
app_ui = ui.page_fluid(
    ui.row(ui.column(12, ui.h1("Mean Wage across US States by Different Categories"),
                         ui.hr(), 
                         align="center")),
    
    ui.row(ui.column(4, ui.em(ui.h3("Authors: Yankun Jiang, Yining Liang, Yuna Fang")),
                        offset=1,
                        align="center"),
           ui.column(4, ui.em(ui.h3("CNetID: yj1084, liangyn17, yunafang")),
                        offset=2,
                        align="center")),
    ui.row(ui.br()),
    ui.row(ui.column(4, ui.input_select(id="gender",
                                        label="Mean wage vs. gender - Choose a state", 
                                        choices=list(acs_sample["state_name"].unique())),
                        offset=1,
                        align="left")),
    ui.row(ui.br()),
    ui.row(ui.column(12, ui.output_plot(id="gender_graph"),
                         align="center")),
    ui.row(ui.br()),
    ui.row(ui.column(4, ui.input_select(id="age",
                                 label="Mean wage vs. age - Choose a state",
                                 choices=list(acs_sample["state_name"].unique())),
                        offset=1,
                        align="left")),
    ui.row(ui.column(12, ui.output_plot(id="age_graph"),
                         align="center"))
    )
def server(input, output, session):
    #prepare the data needed
    @reactive.Calc
    def get_gender():
        acs_gender = pd.read_csv(r"C:\Users\Lucas Jiang\OneDrive - The University of Chicago\MPP\Fall 2022\DAP2-Python\Final Project\data\acs_merge.csv")
        return acs_gender[acs_gender["state_name"] == input.gender()]
    def get_age():
        acs_age = pd.read_csv(r"C:\Users\Lucas Jiang\OneDrive - The University of Chicago\MPP\Fall 2022\DAP2-Python\Final Project\data\acs_merge.csv")
        return acs_age[acs_age["state_name"] == input.age()]
    
    #plot
    @output
    @render.plot
    def gender_graph():
        gender_sum = get_gender()
        gender_plot, ax = plt.subplots(figsize=(10,10))
        ax = sns.boxplot(x="gender", y="WAGP", hue="education_level", data=gender_sum, palette=["pink", "blue"])
        ax.set_ylabel("Mean Wage")
        ax.set_xlabel("Educational Attainment")
        ax.set_title(f"{input.gender()} mean wage by gender and educational attainment")
        return gender_plot
    @output
    @render.plot
    def age_graph():
        age_sum = get_age()
        age_plot, ax = plt.subplots(figsize=(10,10))
        ax = sns.boxplot(x="age_group", y="WAGP", hue="education_level", data=age_sum, palette=["red","purple"])
        ax.set_ylabel("Mean Wage")
        ax.set_xlabel("Educational Attainment")
        ax.set_title(f"{input.age()} mean wage by age group and educational attainment")
        return age_plot
        


app = App(app_ui, server)
