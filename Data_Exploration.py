import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

historical_data = pd.read_csv("C:\\Users\\jmaliks2\\Documents\\Python\\Python_Projects\\DoorDash\\datasets\\historical_data.csv")

from datetime import datetime 

historical_data["created_at"] = pd.to_datetime(historical_data['created_at'])
historical_data["actual_delivery_time"] = pd.to_datetime(historical_data['actual_delivery_time'])

historical_data["actual_total_delivery_duration"] = (historical_data["actual_delivery_time"] - historical_data["created_at"]).dt.total_seconds()

historical_data['estimated_non_prep_duration'] = historical_data["estimated_store_to_consumer_driving_duration"] + historical_data["estimated_order_place_duration"]

store_id_unique = historical_data["store_id"].unique().tolist()
#print(store_id_unique)
store_id_and_category = {store_id: historical_data[historical_data.store_id == store_id].store_primary_category.mode() for store_id in store_id_unique}
print(historical_data.store_primary_category)

#print(historical_data.head()