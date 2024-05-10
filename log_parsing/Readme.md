This code parses both the search-query or search-result. It outputs to a file output.csv that can be imported into Googlesheet or Excel for filtering.
The code runs under Python 3.10.

steps:
1. Save the code into a folder, say /Users/monty/workspace/gcp/.
2. Download the monthly log from your Glean GCP instance. The bucket name is something like scio-xxxx-search-query, where xxxx is your project number.
3. Edit the code to set the folder path. (I hard-coded it) and run.


