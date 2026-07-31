from viconnexusapi import ViconNexus
import time

def get_live_camera_temperatures():
    vicon = ViconNexus.ViconNexus()
    
    # 1. MUST BE LIVE FIRST: Get all camera details while hardware is connected
    print("Checking system hardware while Live...")
    all_device_ids = vicon.GetDeviceIDs()
    
    camera_targets = []
    for device_id in all_device_ids:
        name, device_type, rate, output, active = vicon.GetDeviceDetails(device_id)
        if device_type == "Camera":
            camera_targets.append((device_id, name))
            
    if not camera_targets:
        print("No active cameras detected! Ensure Nexus is in 'Live' mode before starting.")
        return

    print(f"Found {len(camera_targets)} active cameras. Querying hardware metrics...")

    # 2. PAUSE STREAMING: Drop out of live mode briefly to fetch properties safely
    vicon.SetOfflineMode()
    time.sleep(0.3) # Short buffer for the API to register the state swap
    
    try:
        for device_id, name in camera_targets:
            try:
                # Query the camera hardware property safely while offline
                temp_val, enabled = vicon.GetDeviceProperty(device_id, "Temperature")
                print(f"Camera: {name} (ID: {device_id}) | Temperature: {temp_val}°C")
            except Exception as inner_error:
                print(f"Failed to query property for {name}: {inner_error}")
                
    finally:
        # 3. RESTORE LIVE: Instantly push the app back to real-time streaming
        vicon.SetLiveMode()
        print("System safely returned to Live Mode.")

if __name__ == "__main__":
    get_live_camera_temperatures()
