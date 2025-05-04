import keyring
from datetime import datetime
import xml.etree.ElementTree as ET

def pytest_metadata(metadata):
    tree = ET.parse('C:\\PycharmProjects\\Demo_Online_Shopping\\Configurations\\settings.xml')
    root = tree.getroot()
    environment = root.find("Enviorment").text
    release = root.find("Release").text

    # Fetch secure username from keyring
    executed_by = keyring.get_password('execution', 'executed_username')
    metadata.clear()  # Optional: Clears default entries
    metadata["Environment"] =environment
    metadata["Release"]=release
    metadata["Date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    metadata["Executed By"] = executed_by
    metadata["Status"] = "Regression_report"
