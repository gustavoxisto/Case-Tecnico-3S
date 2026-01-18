"""
    Escreva uma função que calcula o quanto um funcionário tem a receber de dois benefícios: Férias e Décimo Terceiro Salário ao 
    pedir demissão.

    Simplificando o cenário, as férias zeram a cada aniversário de emprego (ou seja, ele sempre tirou as férias corretamente) 
    e o décimo terceiro zera a cada virada de ano (não fica nenhum valor residual de um ano para outro).
"""

from datetime import date

class TerminationSalary:

    def __init__(self, salary: float, hire_date: date, termination_date: date):
        if termination_date <= hire_date:
            raise ValueError("Termination date must be after hire date.")
        
        self.salary = salary
        self.hire_date = hire_date
        self.termination_date = termination_date
        self._last_anniversary = None
        self._vacation_months = None
        self._thirteenth_months = None

    def _get_last_anniversary(self) -> date:
        if self._last_anniversary is not None:
            return self._last_anniversary
        
        last_anniversary = date(
            self.termination_date.year,
            self.hire_date.month,
            self.hire_date.day
        )

        if last_anniversary > self.termination_date:
            last_anniversary = date(
                self.termination_date.year - 1,
                self.hire_date.month,
                self.hire_date.day
            )

        self._last_anniversary = last_anniversary
        return last_anniversary

    def _get_vacation_months(self) -> int:
        if self._vacation_months is not None:
            return self._vacation_months
        
        last_anniversary = self._get_last_anniversary()
        
        vacation_months = (
            (self.termination_date.year - last_anniversary.year) * 12
            + (self.termination_date.month - last_anniversary.month)
        )

        if self.termination_date.day >= last_anniversary.day:
            vacation_months += 1

        self._vacation_months = min(vacation_months, 12)
        return self._vacation_months
    
    def _get_thirteenth_months(self) -> int:
        if self._thirteenth_months is not None:
            return self._thirteenth_months
        
        thirteenth_months = self.termination_date.month - 1
        if self.termination_date.day >= 15:
            thirteenth_months += 1

        self._thirteenth_months = thirteenth_months
        return thirteenth_months
    
    def get_vacation_value(self) -> float:
        vacation_months = self._get_vacation_months()
        return self.salary * vacation_months / 12
    
    def get_thirteenth_value(self) -> float:
        thirteenth_months = self._get_thirteenth_months()
        return self.salary * thirteenth_months / 12

    def calculate(self) -> dict:
        vacation_value = self.get_vacation_value()
        thirteenth_value = self.get_thirteenth_value()

        return {
            "vacation_pay": round(vacation_value, 2),
            "thirteenth_salary": round(thirteenth_value, 2),
            "total": round(vacation_value + thirteenth_value, 2)
        }

if __name__ == '__main__':
    salary = 5000.00
    hire_date = date(2023, 2, 26)
    termination_date = date(2026, 5, 30)
    
    termination = TerminationSalary(salary, hire_date, termination_date)
    result = termination.calculate()
    print(f"Salary in termination date: {result}")