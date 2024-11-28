import os

def handle_user_data():
    """
    Handle the User Data file:
    1. Use default file if found.
    2. Ask for a custom file path if default file not found.
    3. Skip if no file is provided or path is invalid.
    """
    default_user_data_file = "temp-swap-setup-file.txt"
    
    # Step 1: Check if the default file exists
    if os.path.isfile(default_user_data_file):
        print(f"Default User Data file '{default_user_data_file}' found. Using it.")
        with open(default_user_data_file, 'r') as file:
            return file.read()
    else:
        # Step 2: Ask user to provide the full path to a User Data file or skip
        print(f"Default User Data file '{default_user_data_file}' not found.")
        user_data_file = input("Please enter the full path to the User Data file or press Enter to skip: ").strip()

        if user_data_file:
            # If the user provides a path, check if the file exists
            if os.path.isfile(user_data_file):
                print(f"User Data file '{user_data_file}' found. Using it.")
                with open(user_data_file, 'r') as file:
                    return file.read()
            else:
                # If the file doesn't exist, show error and skip User Data
                print(f"Error: The specified User Data file '{user_data_file}' does not exist. Skipping User Data.")
                return None
        else:
            # If the user presses Enter without input, skip User Data
            print("No User Data file provided. Skipping User Data.")
            return None


def create_ec2_instance():
    """
    Main function to create an EC2 instance with user input for parameters.
    """
    # Step 1: Instance Type Selection
    print("Select the EC2 instance type:")
    print("1 - [2vCPU and 2GiB RAM - t3.small] TomcatServer")
    print("2 - [2vCPU and 4GiB - t3.medium] Jenkins_Server | Sonarqube | Jfrog | Docker | K8S")
    print("3 - [2vCPU and 8GiB - t3.large] Kubernetes Setup")
    instance_type_choice = input("Enter the number corresponding to the desired instance type: ").strip()

    # Instance details based on selection
    instance_types = {
        "1": {"type": "t3.small", "ami": "ami-05edb7c94b324f73c"},
        "2": {"type": "t3.medium", "ami": "ami-05edb7c94b324f73c"},
        "3": {"type": "t3.large", "ami": "ami-05edb7c94b324f73c"},
    }

    selected_instance = instance_types.get(instance_type_choice, {"type": "t3.small", "ami": "ami-05edb7c94b324f73c"})
    print(f"Selected Instance Type: {selected_instance['type']}")
    print(f"Using default AMI ID: {selected_instance['ami']}")

    # Step 2: Instance Name
    instance_name = input("Enter Name for the EC2 Instance: ").strip()

    # Step 3: Storage Size
    storage_size = input("Enter Storage Size in GB (default: 8): ").strip() or "8"
    storage_size = int(storage_size)

    # Handle User Data
    user_data = handle_user_data()

    # Step 4: EC2 Instance Creation Logic (mock step)
    print(f"Creating EC2 instance with the following parameters:")
    print(f"Instance Type: {selected_instance['type']}")
    print(f"AMI ID: {selected_instance['ami']}")
    print(f"Instance Name: {instance_name}")
    print(f"Storage Size: {storage_size} GB")
    if user_data:
        print(f"User Data will be used during instance creation.")
    else:
        print("No User Data will be provided.")

    # Proceed with EC2 creation (mock step)
    print("EC2 instance creation in progress...")

    # Here you would add the actual AWS EC2 creation code using Boto3 or CLI commands

    print("EC2 instance created successfully!")


if __name__ == "__main__":
    create_ec2_instance()
