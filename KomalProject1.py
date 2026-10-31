import pandas as pd
import numpy as np
df=pd.read_csv("Data_Analysis_Python_Pandas_Task.csv")
print(df)

#Task.1(Data Loading and Inspection)
print("=====================First 10 records================")
print(df.head(10))
print("======================Last 5 records=====================")
print(df.tail(5))
print("==================Find the number of rows and columns===============")
print(df.shape)
print("=====================Display columns names and datatypes============")
print(df.dtypes)
print("====================Statistical Summmary using describe()===========")
print(df.describe())

#Task.2(Data Cleaning)
print("===========Identifying and remove duplicate records=================")
print(df.isnull())
print("=========Finding Missing Value in each Column=======================")
print(df.isna())
print("============Correct Inconsistant department name and Extra Spances=======")
df["Department"]=df["Department"].str.strip()
df["Department"]=df["Department"].replace({'it':'IT','It':'IT','hr':'HR','Hr':'HR',
                                            'sales':'Sales','finance':'Finance'})
print(df)
print("===========Negative Salary And Invalid Performance Score==============")
print(df[df["Monthly Salary"]<0])
df.loc[~df["Performance Score"].between(1,10),
                                        "Performance Score"]=np.nan
      
#Task.3(Data Transformation)
print("===============Creating Annual Salary Column======================")
df["Annual_Salary"]=(df["Monthly Salary"]*12)
print(df)
print("===============Creating Experience level column=================")
df["Expreience_Level"]=(np.where(df["Experience Years"]<=2,"Fresher",
                                 np.where(df["Experience Years"]<=5,"Mid Level","senior")))
print(df)
print("===========Creating Performance Category Column=================")
df['performance_category']=(np.where(df['Performance Score']<=2,"Low",np.where(df['Performance Score']<=5,"Average",
                     np.where(df['Performance Score']>5,"High ","Invalid"))))
print(df)
print("=================Create Salary Band====================")
df['salary_band']=(np.where(df['Monthly Salary']<=50000,"Low",np.where(df['Monthly Salary']<=100000,"Medium"
                                ,np.where(df['Monthly Salary']>100000,"High","Invalid"))))
print(df)

#Task 4:-Business Analysis
print("==============4. Business Analysis================")
print("========Average Salary By Department===========")
average_salary=df.groupby("Department")["Monthly Salary"].mean()
print("Average Salary by Department:",average_salary)
print("=============Highest Paid Employee============")
highest_Paid_Emp=df.loc[df['Monthly Salary'].idxmax()]
print(highest_Paid_Emp)
print("==================Top 10 performance Score============")
top_per_score=df.groupby(["Employee Name","Employee ID"])["Performance Score"].max()
print(top_per_score.head(10))
print("================Average Salary By Job Role==============")
Avg_Salary_Job_Role=df.groupby("Job Role")["Monthly Salary"].mean().sort_values(ascending=False)
print(Avg_Salary_Job_Role)
print("============Compare Average Experience Across Department==============")
Avg_Exp_depart=df.groupby("Department")["Experience Years"].mean().sort_values(ascending=False)
print(Avg_Exp_depart)
print("=============Employee Attrition Percentage===========")
attrition_rate=df["Attrition"].astype(str).str.strip().str.lower().eq("Yes").mean()*100
print("Attrition Percentage:",round(attrition_rate,2),"%")
print("==========Find Emp High Salary with Low Performance Score==========")
print(df[(df["Monthly Salary"]>=100000) &(df["Performance Score"]<=1)])

#Task 5:-Advance Pandas
print("==================5. Advanced Pandas==================")
print("=============Summarise Department Performance==============")
summarise=df.groupby("Department")["Performance Score"].sum().sort_values(ascending=False)
print(summarise)
print("==============Calculate Multiple Statistics==============")
print(df.groupby("Department").agg({"Monthly Salary":["mean","max","min"],
                                          "Performance Score":"median",
                                          "Employee ID":"count"}))
print("===============Sort Values to Rank Employee==================")
Sort_values_Rank_Emp=df.sort_values("Performance Score",ascending=False)
print(Sort_values_Rank_Emp)
print("===========Use loc and iloc to filter reord==========")
print(df.loc[df["Monthly Salary"]>50000])
print(df.iloc[0:5])
print("=============Use pivot table to compare salary and performance=========")
print(pd.pivot_table(df,
    index="Department",
    columns="Performance Score",
    values="Monthly Salary",
    aggfunc="mean"
))
print("==========Use merge to combine employee and department budget datasets=====")
budget = pd.DataFrame({
    "Department": ["IT", "HR", "Sales", "Finance", "Marketing"],
    "Department_Budget": [500000, 200000, 350000, 300000, 250000]
})

merged_df = pd.merge(df, budget, on="Department", how="left")
print(merged_df.head())
print("================Use apply()or vectorized operations to classify employees==============")
df["Employee_Status"] = df["Performance Score"].apply(
    lambda x: "Good" if pd.notna(x) and x >= 7 else "Needs Review"
)

print(df[["Employee Name", "Employee_Status"]].head())
#Task 6:-Business Deliverables
print("===============6. Business Deliverables==============")
print("=================clean Dataset=================")
df.to_excel("cleaning_Data_Analysis_Python_Pandas_Task.xlsx")
print(df)
print("Successfully load excel file")
