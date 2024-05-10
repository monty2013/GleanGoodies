This code parses both the search-query or search-result. It outputs to a file output.csv that can be imported into Googlesheet or Excel for filtering.
The code runs under Python 3.10. This code is free to use or redistribute with or without modifications. No warranty is implied from the author or anyone from the use of this code.

steps:
1. Save the code into a folder, say /Users/monty/workspace/gcp/.
2. Download the monthly log from your Glean GCP instance. The bucket name is something like scio-xxxx-search-query, where xxxx is your project number.
   example: _gsutil -m cp -r gs://scio-557132112309-search-result-us-central1/search-result/2024/05 ._
   or _gsutil -m cp -r  gs://scio-557132112309-search-result-us-central1/search-query/2024/05 ._
4. Edit the code to set the local folder path. (I hard-coded it) and run.
5. Load the output.csv into Excel or Googlesheet



The output csv is without header. 
The columns for the search-query are
InsertID,UserID,TrackerToken,Timestamp,Query,										

The columns for the search result are
InsertID,UserID,TrackerToken,Timestamp,DocId,URL										

For Results, structured results are filtered out. 
