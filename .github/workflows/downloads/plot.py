import pandas as pd
import matplotlib.pyplot as plt

# Read the spreadsheet
df = pd.read_csv("downloads.csv", header=None, names=["Date", "Downloads"])
df["Date"] = pd.to_datetime(df["Date"])

# Plot the download data
plt.figure(figsize=(10, 6))
plt.plot(df["Date"], df["Downloads"])
plt.title("Downloads Over Time")
plt.xlabel("Date")
plt.ylabel("Downloads")
plt.savefig("downloads.png")
