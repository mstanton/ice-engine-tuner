import can
import pandas as pd

def export_can_tune(file_path, output_csv):
    tune_data = []
    
    # Open the CAN interface
    with can.interface.Bus(channel='can0', bustype='socketcan') as bus:  # Adjust channel and bustype as needed
        print("Listening for CAN messages...")
        while True:
            msg = bus.recv()  # Receive CAN message
            if msg is not None:
                # Filter for tuning parameters (example IDs)
                if msg.arbitration_id in [0x100, 0x101, 0x102]:  # Replace with actual tuning IDs
                    tune_data.append({
                        'timestamp': msg.timestamp,
                        'id': msg.arbitration_id,
                        'data': msg.data.hex()  # Convert data to hex string
                    })
                    print(f"Received tuning data: {msg}")

            # Optional: Break condition to stop listening (e.g., after a certain number of messages)
            if len(tune_data) >= 100:  # Adjust as needed
                break

    # Convert to DataFrame and export to CSV
    df = pd.DataFrame(tune_data)
    df.to_csv(output_csv, index=False)
    print(f"Tuning data exported to {output_csv}")

# Example usage
export_can_tune('path/to/can_data.log', 'tune_data.csv')  # Update paths as needed