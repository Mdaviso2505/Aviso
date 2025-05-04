import subprocess

# Path to your Python script
script_path = '/storage/emulated/0/FIREX/unity3dxy.py'

# Initialize counters
total_runs = 0
restart_count = 0
total_count = 20000
each_count = 300
while restart_count < total_count:
    processes = []
    
    # Start 30 processes
    for i in range(each_count):
        process = subprocess.Popen(['python', script_path])
        processes.append((i, process))

    # Wait for all processes to complete and print success message
    for i, process in processes:
        process.wait()
        total_runs += 1
        print(f"success [{total_runs}]")
    
    # Increment restart count after each set of 30 completes
    restart_count += 1
    print(f"Processes completed set {restart_count} of {total_count}")

print("All processes completed successfully.")
