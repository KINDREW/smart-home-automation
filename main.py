import src.temperature_humidity as temp_humidity
import src.relay_control as relay
import src.motion_detection as motion
import src.camera_security as camera
import src.energy_monitoring as energy
import src.voice_control as voice

def main():
    print("Starting Smart Home Automation System...")
    # Example of running different modules
    temp_humidity.monitor_temperature_humidity()
    relay.control_appliance("on")
    motion.detect_motion()
    camera.capture_image()
    energy.monitor_energy_usage()
    voice.execute_voice_command("turn on the light")

if __name__ == "__main__":
    main()
