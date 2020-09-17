class CompoundInterest:
    
    def __init__(self, principal_amount, years, interest_rate):
        self.principal_amount = principal_amount
        self.years = years
        self.interest_rate = interest_rate
        self.compounds_per_year = 12

    def part_one_of_equation(self, interest_rate):
        return round(1 + (self.interest_rate/self.compounds_per_year), 10)

    def part_two_of_equation(self, years):
        return self.years * self.compounds_per_year

    def compound_interest_calc(self, principal_amount, years, interest_rate):
        return round(self.principal_amount * pow(self.part_one_of_equation(self.interest_rate), self.part_two_of_equation(self.years)), 2)

# A = P(1 + r/n)nt

# P is the principal amount
# r is the annual rate of interest
# t is the number of years the amount is invested
# n is the number of times the interest is compounded per year
# A is the amount at the end of the investment