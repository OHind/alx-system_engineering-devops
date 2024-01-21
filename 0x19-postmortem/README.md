Postmortem: System goes down.

![image](https://github.com/OHind/alx-system_engineering-devops/assets/18174519/a32d0352-b548-4c8b-a75f-a1609a44f747)

Issue Summary:
On April 2021, the company's server went down, no one could acess or load materials for work

Timeline:
09:14 - 404 error for anyone trying to access the server
09:20 - Ensuring that Apache and MySQL are up and running
09:40 - Reviewing the error logs to check where the error might be coming from
09:45 - Check /var/log to see that the Apache server was being prematurely shut down
09:50 - Further invistigations show that a configuration file was modified by mistake when implementing a new functionnality
09:55 - A rollback script is deployed to cancel new modiications.
10:00 - After quick restart to Apache server returned a status of 200 and OK

Root cause and resolution:
The root cause of the problem was a bug in a recently deployed update script that corrupted the system files.
To resolve the issue, the engineering team rolled back the new. script

Corrective and Preventive Measures:
	All servers and sites should have error logging turned on to easily identify errors if anything goes wrong.
	All servers and sites should be tested locally before deploying on a multi-server setup this will result in correcting errors before going live resulting in less fixing time if site goes down.
