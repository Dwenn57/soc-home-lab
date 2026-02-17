import subprocess
import time


# Function to run a shell command
def run_command(command):
    print(f"Running: {command}")
    result = subprocess.run(command, shell=True)
    if result.returncode != 0:
        print(f"⚠️ Error while executing: {command}")
    else:
        print(f"✅ Success: {command}")


# Initial startup (without Kibana)
services = ["elasticsearch"]  # , "db", "dvwa"]  # , "ubuntu1"]
for service in services:
    run_command(f"docker compose -f test.yml up -d {service}")


# Wait before starting Kibana
print("⏳ Waiting 30 seconds before starting Kibana...")
time.sleep(15)


run_command("docker compose -f test.yml up -d kibana")


# # Wait before starting Filebeat
# print("⏳ Waiting 30 seconds before starting Filebeat...")
# time.sleep(30)

# run_command("docker compose -f test.yml up -d filebeat")
