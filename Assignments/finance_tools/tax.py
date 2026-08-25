class Income_Tax:
    def __init__(self, resident_type: str = "entity", taxable_income: int = 0):
        self.resident_type = resident_type
        self.taxable_income = taxable_income

    def cal_income_tax(self):
        if self.resident_type.lower() == "entity":
            tax_liability = self.taxable_income * .25
        elif self.resident_type.lower() == "natural person":
            if self.taxable_income < 1000000:
                tax_liability = self.taxable_income * 0.01
            else:
                tax_liability = (1000000 * 0.01) + ((self.taxable_income - 1000000) * 0.10)
        else:
            raise ValueError("Invalid Tax Individual")

        return round(tax_liability)


class VAT:
    def __init__(self, taxable_amount, applicability: str = "taxable"):
        self.taxable_amount = taxable_amount
        self.applicability = applicability

    def cal_VAT(self):
        if self.applicability.lower() == "taxable":
            vat_amount = self.taxable_amount * 0.13
        elif self.applicability.lower() == "zero vat":
            vat_amount = 0
        elif self.applicability.lower() == "electricity":
            vat_amount = self.taxable_amount * 0.05
        elif self.applicability.lower() == "exempt":
            return "VAT is exempt for the good"
        else:
            raise ValueError("Goods or services not recognized. Please look into it.")

        return round(vat_amount)