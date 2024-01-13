import os

current_dir = os.path.dirname(os.path.abspath(__file__))

# confirmed
def mysql_conn(database:str):
    from mysql import connector
    from configparser import ConfigParser

    # define config dir
    config_dir = os.path.join(current_dir, "../config/config.ini")

    # create config
    config = ConfigParser()
    config.read(config_dir)

    # create conn
    conn = connector.connect(
        host=config.get("mysql", "host"),
        port=config.get("mysql", "port"),
        user=config.get("mysql", "user"),
        database=database,
        password=config.get("mysql", "passwd")
    )

    # return conn
    return conn

def return_names(location_id, alert_id):
    conn = mysql_conn("information")
    cursor = conn.cursor()
    
    # get location name
    QUERY = f"""
    SELECT location_name
    FROM location_view
    WHERE location_id = {location_id}
    """
    cursor.execute(QUERY)
    location_name = cursor.fetchall()[0][0]
    
    # get alert name
    QUERY = f"""
    SELECT alert
    FROM alert_view
    WHERE alert_id = {alert_id}
    """
    cursor.execute(QUERY)
    alert = cursor.fetchall()[0][0]
    
    # close conn
    conn.close()
    
    return (location_name, alert)
    
# confirmed
def return_informations(grade:str, location_id:int):
    # define dict
    information_dict = {}

    # open conn
    conn = mysql_conn("information")
    cursor = conn.cursor()

    # set base query and values
    QUERY_building = """
    SELECT address
    FROM building_view
    WHERE building_id in (SELECT building_id FROM location WHERE location_id = %s)
    """
    VALUES_building = (location_id,)

    # safety manager
    QUERY_safetymanager = """
    SELECT access_token, phone_number
    FROM safety_manager_view
    WHERE location_id = %s
    """
    VALUES_safetymanager = (location_id,)

    # employee
    QUERY_employee = """
    SELECT access_token, phone_number
    FROM employee_view
    WHERE location_id = %s
    """

    # collect manager's informations
    if grade == "inspection":
        QUERY_employee += "AND job_id = %s"
        VALUES_employee = (location_id, 1)

    # collect everyone's informations
    elif grade == "evacuation":
        VALUES_employee = (location_id,)

    # get informations
    # building
    if grade == "evacuation":
        cursor.execute(QUERY_building, VALUES_building)
        building = cursor.fetchall()
        information_dict["building"] = [index[0] for index in building]

    # safety manager
    cursor.execute(QUERY_safetymanager, VALUES_safetymanager)
    safetymanager = cursor.fetchall()
    information_dict["safety_manager"] = [{"access_token": index[0], "phone_number": index[1]} for index in safetymanager]

    # employee
    cursor.execute(QUERY_employee, VALUES_employee)
    employee = cursor.fetchall()
    information_dict["employee"] = [{"access_token": index[0], "phone_number": index[1]} for index in employee]

    # close conn
    conn.close()

    return information_dict
