import matplotlib.pyplot as plt
from analytics import monthly_report

def plot_expenses():
    df = monthly_report()

    df.groupby("category")["total"].sum().plot(
        kind="pie",
        autopct='%1.1f%%',
        title="Expense Distribution by Category"
    )

    plt.ylabel("")
    plt.show()

if __name__ == "__main__":
    plot_expenses()
