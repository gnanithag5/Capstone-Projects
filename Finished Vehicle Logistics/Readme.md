# Finished-Vehicle-Logistics

### **Overview**

Efficient vehicle logistics management is vital in auto manufacturing plants to streamline operations and reduce resource waste. However, locating vehicles in large holdings is challenging due to constant inventory movement and the lack of systematic tracking. To address this, an IoT solution was developed to help employees quickly identify vehicle locations, enhancing efficiency. After evaluating cutting-edge technologies, including Bluetooth Low Energy (BLE) and RFID with Real-Time Location Systems (RTLS), the RFID-RTLS solution was chosen for its superior range, readability, and scalability.

### **Project Code**

The code has 6 modules primarily in the colab notebook,

The notebook is structured with the following key features:

1. Visualization of an Empty Parking Lot: Displays the layout of the parking lot with specified dimensions, including parking spaces and driveways.

2. Data Generation and Vehicle Assignment: Generates data for the vehicles and assigns them to parking spaces based on unique tag IDs. The data is stored in a Pandas DataFrame that includes details like tag ID, timestamp, vehicle status, manufacturing date, and more.

3. Vehicle Location by Tag ID: Allows you to input a vehicle’s tag ID and visually find the vehicle’s location within the parking lot.

4. Exit and Inspection Updates: Updates the DataFrame when a vehicle exits the parking lot for inspection and when it re-enters after inspection.

5. Re-Entry and Status Updates: Tracks the status changes of vehicles, such as re-entry after inspection.

6. RTLS-Based Vehicle Location: Uses RTLS sensor data to locate vehicles that are not found in their assigned parking spaces.

### **Requirements**

1. NumPy
2. Pandas
3. Matplotlib
4. Random
5. datetime

### **Usage**

1. Visualization of the Parking Lot: Running the first code snippet, the parking lot layout will be displayed.
2. Vehicle Assignment: Run the second snippet to generate random vehicle data and assign them to parking spaces.
3. Retrieve Vehicle Location: Enter the Tag ID in the provided input box to get the location of a vehicle in the parking lot.
4. Exit and Inspection: To simulate vehicle exit for inspection, run the corresponding snippet to update the status in the DataFrame.
5. Re-entry and Status Updates: After the vehicle returns to the parking lot, use the relevant code to update the status and location.
6. RTLS Tracking: If the vehicle is not in its assigned parking space, the system will use RTLS sensor data to locate it in real-time.
