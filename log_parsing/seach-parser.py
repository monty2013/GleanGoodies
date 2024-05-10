import os
import json
def read_json_files(folder_path):
    # Check if the folder path exists
    if not os.path.exists(folder_path):
        print(f"The folder '{folder_path}' does not exist.")
        return
    json_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
    # create an output file
    with open('output.csv', 'w') as ofile:
        # Iterate through each JSON file and process its contents
        for json_file in json_files:
#            print(json_file)
            with open(json_file, 'r') as file:
                for line in file:
                    ### This is to parse the search-query events that contains a summary
                    if "raw_query" in line: 
                        try:
                            data = json.loads(line)
#                            print(os.path.basename(json_file) + "," + data["insertId"])
                            ofile.write(data["insertId"]+","+ data["jsonPayload"]["RequestOptions"]["UserIdentity"]["User"] + ","+data["jsonPayload"]["TrackingToken"]+"," + data["jsonPayload"]["RequestOptions"]["RequestID"] +","+ data["receiveTimestamp"] +"," + data["jsonPayload"]["RequestOptions"]["QueryStr"]+"\n")
                        except json.JSONDecodeError:
                            print(f"Error reading line in '{json_file}' - Invalid JSON format.")
                            continue
                    ### This is parse the search-result json files ####    
                    elif "TrackingSignals" in line and "Results" in line:    
                        try:
                            data = json.loads(line)
#                            print(os.path.basename(json_file) + "," + data["insertId"])
                            if (data["jsonPayload"]["Results"]):
                                for r in data["jsonPayload"]["Results"]:
                                    if (r["Id"]):
                                        ofile.write(data["insertId"]+"," + data["jsonPayload"]["ObfuscatedUserIdentity"]["User"] + ","+r["TrackingSignals"]["search"]["request_token"] +","+ data["timestamp"] +","+r["Id"] +","+r["Url"]+"\n")
                        except json.JSONDecodeError:
                            print(f"Error reading line in '{json_file}' - Invalid JSON format.")
                            continue
'''                    else:
                        try:
                            data = json.loads(line)
                            print(os.path.basename(json_file) + "," + data["insertId"])
                        except json.JSONDecodeError:
                            print(f"Error reading line in '{json_file}' - Invalid JSON format.")
                            continue
'''                            
# Download the files as folder from GCS to the local drive, then run this code
folder_path = '/Users/monty/workspace/gcp/05'
read_json_files(folder_path)
