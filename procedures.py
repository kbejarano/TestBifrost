from snowflake.snowpark.types import StructField, StructType, IntegerType, StringType
from snowflake.snowpark import Session

"""
You can create a Snowflake stored procedure from the 'create_dummy_table' function. You only need to follow these steps:
    1. Import the build (this can be done from the Metals extension tab on the left activity bar). Wait for this import to finish.
    2. Right-click on the build.sbt file in the root of this project.
    3. Choose the 'Black Diamond: Export Python UDF' option.
    4. Fill the template file 'UDF-Export-Snowflake-Python.sql' (on the 'Target' folder) with the requested information
        (you can ignore or delete the section 3.2, since that part is used to export a User Defined Function and section 3.1
        is used to export a Procedure, which is what we are doing in this case).
    5. Execute the SQL commands in the template file.
    6. Your stored procedure should be ready. You can call this stored procedure as you would normally do in Snowflake.
    7. Take into consideration that there are some limitations when creating Snowpark procedures or UDFs in Python.
"""
def create_dummy_table(sess: Session):
    id_column = StructField("id", IntegerType())
    value_column: StructField = StructField("value", StringType())
    structure = StructType([id_column, value_column])
    example_dataframe = sess.createDataFrame([(1, "one"), (2, "two")], structure).write.saveAsTable("example_dummy_table")
    return "Procedure Executed Successfully"