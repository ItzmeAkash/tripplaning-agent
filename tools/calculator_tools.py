from langchain.tools import tool
from pydantic import BaseModel,Field

class CalculatorTools():
    @tool("Make a calculation")
    def calculate(operation):
        """Usefull to perform any mathematical calculations,
        like sum,minus,mutiplication,divison,etc.
        The input to this tool should be a mathematical
        expression,a couple examples are `200*7` or `5000/2*10`
        """
        try:
            return eval(operation)
        except SyntaxError:
            return "Error: Invalid syntax in mathematical expression"
        

#Define a Pydantic Model for the tool's input parameters

# class CalculationInput(BaseModel):
#     operation: str = Field(..., description="The mathematical operation to perform")   
#     factor: float  =  Field(..., description="A factor by which to multiply the result of the operation")
    
    
#Use the tool decortor with the args_schema parameters pointing to the pydantic model
# @tool("perform_calculation", args_schema=CalculationInput, return_direct=True)
# def perform_calculation(operation: str, factor: float) -> str:
#     """
#     Pefroms a specified mathematical operation and multiplies the result by a given factor.
    
#     Parameters:
#     - operation (str): A string representing a mathematical operation, e.g. "2+3"
#     - factor (float): A factor by which to multiply the result of the operation
    
#     Returns:
#     - A string representation of the calculation result
#     """
    
#     # Peform the calculation
#     result  = eval(operation) * factor
    
#     # Return the result as a string
#     return f"The result of '{operation}' multiplied by '{factor}' is {result}."

    
 