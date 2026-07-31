from viconnexusapi import ViconNexus

def get_camera_temperatures():
    # Initialize the Vicon Nexus API client
    vicon = ViconNexus.ViconNexus()
    
    # Retrieve IDs of all devices connected to the system
    device_ids = vicon.GetDeviceIDs()
    
    print(f"Found {len(device_ids)} total device node(s).")
    
    for device_id in device_ids:
        # Fetch human-readable metadata for each device node
        name, device_type, rate, output, active = vicon.GetDeviceDetails(device_id)
        
        # Filter strictly for Vicon hardware optical cameras
        if device_type == "Camera":
            try:
                # Query the specific hardware 'Temperature' attribute
                # This returns (property_value, is_enabled)
                temp_val, enabled = vicon.GetDeviceProperty(device_id, "Temperature")
                
                print(f"Camera ID: {device_id} | Name: {name} | Temperature: {temp_val}°C")
            except Exception as e:
                print(f"Could not retrieve temperature for Camera {name} (ID: {device_id}): {e}")

if __name__ == "__main__":
    get_camera_temperatures()
