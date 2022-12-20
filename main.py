
class Calculator:
    current_calculation = None
    income = dict()
    expense = dict()
    investment = dict()

    income_sum = float()
    expense_sum = float()
    invest_sum = float()
    cash_flow = float()
    cash_roi = None

    def calculate_cash_flow(self):
        self.expense_sum = sum(self.expense.values())
        self.income_sum = sum(self.income.values())

        print(f"Your monthly expenses are ${self.expense_sum}")

        self.cash_flow = self.income_sum - self.expense_sum

        print(f"Your monthly cash flow is ${self.cash_flow}")

    def find_cash_on_cash_roi(self):
        self.invest_sum = sum(self.investment.values())

        ann_cash_flow = (self.cash_flow * 12)

        self.cash_roi = ((ann_cash_flow / self.invest_sum) * 100)

        print(f"Your total investments are ${self.invest_sum}")

        print(f"Monthly Income: ${self.income_sum}\nMonthly Expenses: ${self.expense_sum}\nMonthly Cash Flow: ${self.cash_flow}\nAnnual Cash Flow: ${ann_cash_flow}\n Total Investments: ${self.invest_sum}")

        print(f"your current cash-on-cash roi is {self.cash_roi}% ")
    
    
        
        





def calculate_roi():
    calculator = Calculator()

    calc_input = input()
    #check if current_calculation exists
    if calculator.current_calculation is None:
        #Welcome message
        print("ROI Calculator\nTo calculate your cash-on-cash return, we'll first need some data from you\nPlease exclude any currency signs, commas and write out entire values including cents")
       #RENT
        calc_input = float(input("What is your monthly rental income?"))
        calculator.income['rent'] = calc_input

        if calculator.income['rent'] is not None:
            #STORAGE
            calc_input = float(input("What is your monthly storage income?"))
            calculator.income['storage'] = calc_input

        if calculator.income['storage'] is not None:
            #MISCELLANEOUS
            calc_input = float(input("What is your monthly miscellaneous income?"))
            calculator.income['miscellaneous'] = calc_input
#EXPENSES
        if len(calculator.expense) == 0:
            #TAX
            print("Now that we've handled your Income, it's time to move on to Expenses")
            calc_input = float(input("What is your monthly tax expenses?"))
            calculator.expense['tax'] = calc_input
        
        if calculator.expense['tax'] is not None:
            #INSURANCE
            calc_input = float(input("What is your monthly Insurance?"))
            calculator.expense['insurance'] = calc_input

        if calculator.expense['insurance'] is not None:
            #UTILITIES
            bool_input = input("Do you have utility expenses? Type 'yes' or 'no' ")
            
            while bool_input == "yes":
                 #ELECTRICITY
               calc_input = float(input("What is your electricity expense?")) 
               calculator.expense['electricity'] = calc_input

               if calculator.expense['electricity'] is not None:
                #WATER
                calc_input = float(input("What is your water expense?")) 
                calculator.expense['water'] = calc_input

                if calculator.expense['water'] is not None:
                     #GARBAGE
                    calc_input = float(input("What is your garbage expense?")) 
                    calculator.expense['garbage'] = calc_input
                    #end utilities
                    bool_input = "no"

        if calculator.expense.get('hoa') == None:
            #HOA
            calc_input = float(input("What is your HOA fee?")) 
            calculator.expense['hoa'] = calc_input
                
        if calculator.expense['hoa'] is not None:
            #LAWNCARE OR SNOW
            lawn_input = input("Do you have lawncare or snow expenses? Type 'yes' or 'no' ")

            while lawn_input == "yes":      
                  #LAWNCARE
                   calc_input = float(input("What is your lawncare expense?")) 
                   calculator.expense['lawn'] = calc_input
                   #end lawncare questioning
                   lawn_input = "no"
        
        if calculator.expense.get('vacancy') == None:
             #VACANCY
            calc_input = float(input("What is your monthly vacancy expenses?")) 
            calculator.expense['vacancy'] = calc_input

        if calculator.expense['vacancy'] is not None:
            #REPAIRS
            calc_input = float(input("What is your monthly repairs expense?")) 
            calculator.expense['repair'] = calc_input
                        
        if calculator.expense['repair'] is not None:
            #CAPITAL EXPENDITURE
            calc_input = float(input("What is your monthly capital expenditures?")) 
            calculator.expense['capital'] = calc_input
                        
        if calculator.expense['capital'] is not None:
            #PROP. MGMT
            calc_input = float(input("What is your monthly property management fee?")) 
            calculator.expense['mgmt'] = calc_input
                        
        if calculator.expense['mgmt'] is not None:
            #MORTGAGE
            calc_input = float(input("What is your monthly mortgage?")) 
            calculator.expense['mortgage'] = calc_input
#PRETTY PRINT MONTHLY EXPENSES + CASH FLOW HERE
    output = calculator.calculate_cash_flow()

#INVESTMENTS
    if output is not None:
        #DOWN PAYMENT
       calc_input = float(input("What is your down payment?"))
       calculator.investment['down'] = calc_input

    if calculator.investment['down'] is not None:
        #CLOSING COST
       calc_input = float(input("What is your closing cost?"))
       calculator.investment['close'] = calc_input 
    
    if calculator.investment['close'] is not None:
        #REHAB
       calc_input = float(input("What is your rehab budget?"))
       calculator.investment['rehab'] = calc_input 

    if calculator.investment['rehab'] is not None:
        #MISC
       calc_input = float(input("Do you have any miscellaneous investments?"))
       calculator.investment['miscellaneous'] = calc_input

# PRETTY PRINT (TOTAL INVESTMENTS)/ ITEMIZED LIST OF VALUES AND CASH ON CASH ROI 
    calculator.find_cash_on_cash_roi()

    if calculator.cash_roi is not None:
        calculator_actions()
        

def calculator_actions():
    calculator = Calculator()

    print("Options")
    new_input = input("What would you like to do next? edit/view/exit")

    if new_input == "edit":
        section_input = input("Which section would you like to edit? Income/Expense/Investment")

        #Empty list of keys 
        keys = []

        if section_input == "Income":

            keys = calculator.income.keys

        elif section_input == "Expense":

            keys = calculator.expense.keys

        else:

            keys = calculator.income.keys
        
        #allow user to select which item to update
        keys_str = '/'.join(keys)
        item_input = input(f"Which item would you like to update? The options are : {keys_str}")
        

    elif new_input == "view":
            calculator.find_cash_on_cash_roi()
    else:
            calculator.current_calculation = None
            print("Run the program again to calculate a new property value")


calculate_roi()