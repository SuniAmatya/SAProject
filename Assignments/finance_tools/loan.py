class EMI_Calculator():
    def __init__(self, principal, rate, years):
        self.principal = principal
        self.rate = rate
        self.years = years

    def calculate_emi(self):
        monthly_rate= self.rate/12/100
        months = self.years * 12
        
        if self.rate == 0:
            emi_amount = self.principal/ months  #When entity is unsure of the rate applied.
        else:
            effective_rate = (
                monthly_rate * ((1+monthly_rate)**months)
                ) / (
                    ((1+monthly_rate)** months) -1)
            emi_amount = self.principal * effective_rate

        return round(emi_amount)