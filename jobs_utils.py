import csv


class Job:
    def __init__(self, name, state):
        self.name = name
        self.state = state


class Year(Job):
    def __init__(self, name, state, pay, year):
        super().__init__(name, state)
        self.pay = pay
        self.year = year

    def show_year(self):
        return self.year

    def show_pay(self):
        x = self.pay
        x = int(x)
        return x


def search_state(a):
    state_dict = {}
    with open("jobs.csv", "r") as jobs:
        csv_reader = csv.reader(jobs)
        for line in csv_reader:
            if len(line) > 2:

                if line[0] == a:
                    state_dict[line[1]] = line
    return state_dict


def get_job(b, c):
    answer = ""
    for job in b:
        if job == c:
            for i in b[job]:
                if b[job].index(i):
                    answer = i

    return answer


def get_years_pay(d, e):
    pay_list = []
    sal_list = []
    for job in d:
        if e == job:
            for i in d[job]:
                pay_list.append(i)

    sal_list.append(pay_list[2])
    sal_list.append(pay_list[5])
    sal_list.append(pay_list[6])
    sal_list.append(pay_list[7])
    sal_list.append(pay_list[8])
    return sal_list


def get_description(b, c):
    answer = ""
    pay_list = []
    for job in b:
        if job == c:
            for i in b[job]:
                pay_list.append(i)
    answer = pay_list[3]
    return answer
