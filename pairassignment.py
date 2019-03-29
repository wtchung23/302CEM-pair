import math
# reference: https://www.ird.gov.hk/eng/ese/st_comp_2018_19_budget/stcfrm.htm

def cal_MPF(income):
    if income < 7100*12:
        mpf = 0
    elif income >= 30000*12:
        mpf = 1500*12
    else:
        mpf = income*0.05
    return math.floor(mpf)

def cal_netIncome(income):
    return income - cal_MPF(income)

def cal_ncIncome(income):
    basic_allowance = 132000
    return cal_netIncome(income) - basic_allowance

def srTax(netIncome):
    rate = 0.15
    return netIncome*rate

def prTax(ncIncome):
    rate = 0.02
    tax = 0
    nci_per_year = 50000

    while ncIncome > 0:
        if ncIncome > nci_per_year:
            tax = tax + nci_per_year * rate
            rate += 0.04
            ncIncome = ncIncome - nci_per_year
            if rate > 0.14:
                tax = tax + ncIncome * 0.17
                break
        else:
            tax = tax + ncIncome * rate
            break

    return math.floor(tax)

def cal_stax(income):
    netIncome = cal_netIncome(income)
    ncIncome = cal_ncIncome(income)

    if netIncome >= 2022000:
        # standard rate tax
        tax = srTax(netIncome)
    else:
        # progressive rate tax
        tax = prTax(ncIncome)

    return math.floor(tax)

def cal_jtax(husband_income,wife_income):
    netIncome = cal_netIncome(husband_income)+cal_netIncome(wife_income)
    ncIncome = cal_ncIncome(husband_income)+cal_ncIncome(wife_income)

    if netIncome>=3144000:
        #standard rate tax
        tax = srTax(netIncome)
    else:
        # progressive rate tax
        tax = prTax(ncIncome)
    return math.floor(tax)

#final tax after tax reduction
def final_tax(husband_income,wife_income):
    husbandTax = cal_stax(husband_income)
    wifeTax = cal_stax(wife_income)
    sTax = husbandTax+wifeTax
    # print("\nSeparate taxation = " + str(sTax))

    jTax = cal_jtax(husband_income,wife_income)
    # print("Joint net chargeable income = " + str(joint_nci))
    # print("Joint taxation = " + str(jTax))

    if sTax<=jTax:
        if husbandTax*0.75>=20000:
            husbandTax = husbandTax - 20000
        else:
            husbandTax = husbandTax*(1-0.75)
        if wifeTax*0.75>=20000:
             wifeTax = wifeTax - 20000
        else:
             wifeTax = wifeTax*(1-0.75)
        sTax = husbandTax + wifeTax
        finalTax = sTax
    else:
        finalTax = jTax
        if finalTax*0.75>20000:
            finalTax = finalTax - 20000
        else:
            finalTax = finalTax*(1-0.75)

    return math.floor(finalTax)

if __name__ == '__main__':
    #income per year
    husband_income = int(input("\nPlease input husband's personal input per year:"))
    wife_income = int(input("Please input wife's personal input per year:"))
    print("\nHusband's MPF = " + str(cal_MPF(husband_income)))
    print("Wife's MPF = " + str(cal_MPF(wife_income)))

    print("\nHusband tax payable = " + str(cal_stax(husband_income)))
    print("Wife tax payable= " + str(cal_stax(wife_income)))
    print("\nSeparate taxation = " + str(cal_stax(husband_income)+cal_stax(wife_income)))
    print("Joint taxation = " + str(cal_jtax(husband_income,wife_income)))

    # print(final_tax(husband_income, wife_income))
    if cal_stax(husband_income)+cal_stax(wife_income)<=cal_jtax(husband_income,wife_income):
        print("\nWe recommend Separate assessment.")
    else:
        print("\nWe recommend Joint assessment.")

    print("\nAfter tax reduction, the final tax is "+ str(final_tax(husband_income,wife_income)))

