import pandas as pd
import csv
import plotly.express as px

dataFrames = pd.read_csv("projectData.csv")

mean = dataFrames.groupby(["student_id", "level"], as_index = False)["attempt"].mean()


print("the calculated mean is: "+str(mean))

figure = px.scatter(
    mean,
    x = "student_id",
    y = "level",
    size = "attempt",
    color = "attempt"
)

figure.show()