"""
You can create a Snowflake UDF (User Defined Function) from the 'simple_division' function. You only need to follow these steps:
	1. Right-click on the python file that contains the function you want to convert into a UDF.
	2. Choose the 'Black Diamond: Export Python UDF' option.
	3. Fill the template file 'UDF-Export-Snowflake-Python.sql' (on the 'Target' folder) with the requested information
		(you can ignore or delete the section 3.1, since that part is used to export a Procedure and section 3.2
		is used to export a User Defined Function, which is what we are doing in this case).
	4. Execute the SQL commands in the template file.
	5. Your funcion should be ready. You can perform queries using this UDF as you would normally do in Snowflake.
	6. Take into consideration that there are some limitations when creating Snowpark procedures or UDFs in Python.
"""
def simple_division(a: float, b: float):
    return a / b