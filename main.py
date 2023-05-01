from matplotlib import pyplot as plt
import jobs_utils


def play():
    state = input("Enter the state stating with a capital letter eg Alabama")
    title = input("Enter the title each word starting with a capital letter")
    ans = jobs_utils.search_state(state)

    if ans:
        pay = jobs_utils.get_job(ans, title)

        if pay:
            desc = jobs_utils.get_description(ans, title)
            desc = desc.replace("-", "$")
            print("The current median salary of a " + title + " in " + state + " is: $" + pay)
            print("Job Description: " + desc)

            year_pay = jobs_utils.get_years_pay(ans, title)

            year_1 = jobs_utils.Year(title, state, year_pay[0], 2022)
            year_2 = jobs_utils.Year(title, state, year_pay[1], 2022)
            year_3 = jobs_utils.Year(title, state, year_pay[2], 2022)
            year_4 = jobs_utils.Year(title, state, year_pay[3], 2022)
            year_5 = jobs_utils.Year(title, state, year_pay[4], 2022)

            salaries = [year_5.show_pay(), year_4.show_pay(), year_3.show_pay(), year_2.show_pay(), year_1.show_pay()]

            years = ["2018", "2019", "2020", "2021", "2022"]

            plt.plot(years, salaries)
            plt.title("General salary trend for a " + title + " in " + state + " in the last five years")
            plt.xlabel("Years")
            plt.ylabel("Median salary(USD)")

            plt.show()

        else:
            print("The job title is not available in this state")
    else:
        print("You entered a wrong state")


play()
