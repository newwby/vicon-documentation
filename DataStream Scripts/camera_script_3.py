from viconnexusapi import ViconNexus
import time

def get_camera_temperatures_via_pause():
    vicon = ViconNexus.ViconNexus()
    
    # 1. Ensure we are online so the camera IDs are populated
    if not vicon.IsLive():
        vicon.SetLiveMode()
        time.sleep(0.5)
        
    device_ids = vicon.GetDeviceIDs()
    cameras = []
    
    for device_id in device_ids:
        name, device_type, _, _, _ = vicon.GetDeviceDetails(device_id)
        if device_type == "Camera":
            cameras.append((device_id, name))
            
    if not cameras:
        print("No cameras found in the active Live tree.")
        return

    # 2. PAUSE the live stream (Do NOT go offline)
    # This stops the frame data thread but KEEPS the hardware objects active
    print("Pausing live stream to safely read hardware registers...")
    vicon.Pause() 
    time.sleep(0.5) # Allow the hardware thread to settle
    
    try:
        for device_id, name in cameras:
            try:
                # Query the camera temperature property
                temp_val, _ = vicon.GetDeviceProperty(device_id, "Temperature")
                print(f"Camera: {name} (ID: {device_id}) | Temp: {temp_val}°C")
            except Exception as e:
                print(f"Skipping {name}: {e}")
    finally:
        # 3. Resume real-time tracking
        print("Resuming live stream...")
        vicon.SetLiveMode() 

if __name__ == "__main__":
    get_camera_temperatures_via_pause()
