# GasUtility

This django app has primarily 3 parts: servReq, reqTrack and manageReq.
The base url gives option to use either servReq or reqTrack.
To use manageReq, one must directly open it via URL.

servReq is used by customers to submit requests onto the portal.
They can give their name, contact info, type of service they need, short description of the problem and attach files.
This request is stored onto the server and a request tracking ID is given to the user.
The request ID is actually the primary key of the database and is thus unique.
If a file is submitted, the file is named "file_<request_ID>.<file_extension>" and stored in the media folder.
Any file of any extension is allowed.

reqTrack is used by the customer to track their submitted request.
Customers can input their tracking ID and get all details submitted by them and the time when the request was submitted.
If the issue has been marked as resolved by a customer support representative, then the time when it was resolved is also displayed.
Customers can also download the file they had submitted while creating the request.

manageReq is used by customer support representatives and not the customers.
It displays all the existing requests in the system along with all their details.
Files uploaded by customers can also be downloaded by the representative.
Status of any request can be changed by mentioning the request ID and updated status.
If the status is marked as "Resolved", the time is updated in the database.
