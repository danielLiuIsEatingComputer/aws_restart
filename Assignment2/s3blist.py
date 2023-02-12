"""
Logic:

1.Get the default region of the session
2.Ask the user to confirm the default region
3.If the user confirms the default region
    4.Connect to S3 using the default region
    5.Retrieve and list all S3 buckets
    6.Create a text file and write the list of buckets into it
    7.Print the name of each bucket
    8.Notify the user that the list of buckets has been saved
9.If the user does not confirm the default region
    10.Terminate the program

"""


import boto3

# Get the default region of the session
region = boto3.session.Session().region_name
# Ask the user to confirm the default region
region_confirm = input("The current default region is " + region + ". Is this correct? (Yes/No): " )

# If the user confirms the default region
if region_confirm.lower() == 'yes':
    # Connect to S3 using the default region
    s3 = boto3.client('s3')

    # Retrieve and list all S3 buckets
    buckets = s3.list_buckets()['Buckets']
    
    # Create a text file and write the list of buckets into it
    with open("latest_bucket_list.txt", "w") as file:
        for bucket in buckets:
            file.write(bucket['Name'] + '\n')
            
    # Print the name of each bucket
    for bucket in buckets:
        print(bucket['Name'])
     # Notify the user that the list of buckets has been saved    
    print("Current S3 buckets list has been saved as: latest_bucket_list.txt")
    
# If the user does not confirm the default region
else:
    #Terminate the program
    print("The program has been terminated.")