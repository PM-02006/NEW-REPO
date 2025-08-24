class Client:
    def __init__(self,Salary=float(input("Enter your monthly income:")),Monthly_Expenses=float(input("Enter your monthly expenses:"))):
        self.__Salary = Salary
        self.__Monthly_Expenses = Monthly_Expenses
        self.__Has_House = False
        self.__Pays_Electrical = False
        self.__Has_Job = False
        self.__In_Dept = False
        self.__Has_Assets = False
        self.__Has_Vehicle = False
        self.__Score = 0
#METHODS
    def GetSalary(self):
        return self.__Salary

    def GetMonthly_Expenses(self):
        return self.__Monthly_Expenses

    def __House(self, Answer=str(input("Do you own a house?"))):
        if Answer.lower() == "yes":
            self.__Has_House = True
    def __Electrical(self,Answer=str(input("Do you pay electrical bills?"))):
        if Answer.lower() == "yes":
            self.__Pays_Electrical = True

    def __Job(self, Answer=str(input("Do you have a job?"))):
        if Answer.lower() == "yes":
            self.__Has_Job = True

    def __Assets(self, Answer=str(input("Do you have assets?"))):
        if Answer.lower() == "yes":
            self.__Has_Assets = True

    def __Vehicle(self, Answer=str(input("Do you own a vehicle?"))):
        if Answer.lower() == "yes":
            self.__Has_Vehicle = True

    def __Dept(self, Answer=str(input("Do you have any loans?"))):
        if Answer.lower() == "yes":
            self.__In_Dept = True
    def Evaluate_Score(self):
        self.__Job()
        self.__House()
        self.__Vehicle()
        self.__Assets()
        self.__Electrical()
        self.__Dept()

        match self.GetSalary():
            case Score if Score <= 25000 and Score<= 50000:
                self.__Score = self.__Score + 10
            case S if S <= 50000 and S <= 100000:
                self.__Score = self.__Score + 20
            case S if S > 100000:
                self.__Score = self.__Score + 30
        match self.GetMonthly_Expenses():
            case S if S <= 25000 and S <= 50000:
                self.__Score = self.__Score + 5
            case S if S <= 50000 and S <= 100000:
                self.__Score = self.__Score + 10
            case S if S > 100000:
                self.__Score = self.__Score + 15
        if self.__Has_Job:
            self.__Score = self.__Score + 20
        if self.__Has_Vehicle:
            self.__Score = self.__Score + 10
        if self.__Has_Assets:
            self.__Score = self.__Score + 25
        if self.__Has_House:
            self.__Score = self.__Score + 20
        if self.__Pays_Electrical:
            self.__Score = self.__Score + 5
        if self.__In_Dept:
            self.__Score = self.__Score + 15
        return self.__Score

    def LoanCriteria(self):
        match self.Evaluate_Score():
            case self.__Score if self.__Score <20:
                print("Client is not eligible for a loan")
            case self.__Score if self.__Score >= 20 and self.__Score <= 50:
                print("Loan approved for less than NPR 1,00,000")
            case self.__Score if self.__Score>50 and self.__Score <= 70:
                print("Loan approved for NPR less than NPR 5,00,000")
            case self.__Score if self.__Score > 70:
                print("Loan approved for more than NPR 5,00,000")





#MAIN
Customer= Client()
print(Customer.LoanCriteria())








