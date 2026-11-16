import pandas as pd
df=pd.read_excel('customer churn analyse.xlsx')
print(df.head(20))

#replacing blanks with 0 as tenure is 0 and no total charges are recorded
df["TotalCharges"] =df["TotalCharges"].replace(" ","0")
df["TotalCharges"] =df["TotalCharges"].astype("float")
df.info()
print(df.isnull().sum())
print("Overallnull values",df.isnull().sum().sum())
print(df.describe())

# #Converted 0 and 1 values of senior citizen to yes/no to make it easier to understand
df['SeniorCitizen'] =df['SeniorCitizen'].map({'Yes':1,'No':0})
print(df.head(30))
import seaborn as sns
import matplotlib.pyplot as plt
ax =sns.countplot(x ="Churn",data=df)
ax.bar_label(ax.containers[0])
plt.title("Count of customer by Churn")
plt.show()

plt.figure(figsize = (3.4, 3.4))
gb =df.groupby("Churn").agg( {"Churn": "count"} )
plt.pie (gb["Churn"] , labels=gb.index , autopct="%1.2f%%")
plt.title("Percentage of Churn customer ", fontsize=10)
plt.show()

#from the given pie chart we can conclude that 26.54% of our customer have churned out.
#not Let's explore the reason behind it
plt.figure(figsize =(4.4, 4.4))
sns.countplot(x ="gender", data= df, hue= "Churn")
plt.title("Churn by gender")
plt.show()

plt.figure(figsize=(4.3,4.3))
sns.countplot(x="SeniorCitizen", data=df,hue="Churn")
plt.title("Churn by SeniorCitizen")
plt.show()

#Create percentage table
ct = pd.crosstab(df["SeniorCitizen"], df["Churn"], normalize="index") * 100

# Plot 100% stacked bar chart
ax = ct.plot(
    kind="bar",
    stacked=True,
    figsize=(4.4, 4.4)
)

plt.title("Churn by SeniorCitizen (%)")
plt.xlabel("SeniorCitizen")
plt.ylabel("Percentage (%)")
plt.xticks(rotation=0)
plt.legend(title="Churn", bbox_to_anchor = (0.9,0.9)) # Customize legend location

# Add percentage labels
for container in ax.containers:
    labels = [f"{v:.1f}%" if v > 0 else "" for v in container.datavalues]
    ax.bar_label(container, labels=labels, label_type="center")

plt.ylim(0, 100)
plt.show()
#Comparative a greated pecentage of pepole in senior citizen category have churned

plt.figure(figsize = (5.4, 5.4))
sns.histplot(x ="tenure", data= df, bins =72, hue = "Churn")
plt.show()
# pepole bwho have used our services for a Long time have stayed and pepole who have used our services
# 1or 2 months

plt.figure(figsize = (4.3, 4.3))
ax=sns.countplot(x = "Contract", data = df,hue="Churn")
ax.bar_label(ax.containers[0])
plt.title("count of customer by Contract")
plt.show()
# Pepole who have month contrat are likely to churn than from those who have 1 or 2 years or contract

features = [
    "Partner",
    "Dependents",
    "PhoneService",
    "MultipleLines",
    "InternetService",
    "OnlineSecurity",
    "OnlineBackup",
    "DeviceProtection",
    "TechSupport",
    "StreamingTV",
    "StreamingMovies",
]

# # Plot in batches of 4
batch_size = 4
for i in range(0, len(features), batch_size):
    batch = features[i : i + batch_size]
    plt.figure(figsize=(12, 5))
    for j, col in enumerate(batch):
        plt.subplot(1, len(batch), j + 1)
        sns.countplot(x=col, hue="Churn", data=df)
        plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
 #customers without these services/relationships generally have higer churn counts.
 # internet Service and OnlineSecurity/Backup/DeviceProtection:customers using certain internet services,especially Fiber
 #optic, show comparatively higer churn.Overall,service type and customer relationship factors appear to be important
 #indicators of customer churn.

plt.figure(figsize =(6.4,6.4))
ax = sns.countplot(x="PaymentMethod", data =df,hue="Churn")
ax.bar_label(ax.containers[0])
ax.bar_label(ax.containers[1])
plt.title("Churned customer Payment Method")
plt.xticks(rotation =45)
plt.tight_layout()
plt.show()
#customer is Likely to churn when he is using electronic check as a payment method. 