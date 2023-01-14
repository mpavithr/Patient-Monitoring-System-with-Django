# Patient Monitoring System with Django + New Module

## Repository Explanation 

Migrated my previous repository Patient-Monitoring-Platform to Django and added a Speech to text module that implements a queue management system.


[Previous Repository](https://github.com/mpavithr/Patient-Monitoring-Platform) was done in flask. Have migrated to Django and added a new module that is the Speech to Text Module.

Refer to my [Previous Repository](https://github.com/mpavithr/Patient-Monitoring-Platform) to get an understanding of the project and device and chat modules.

## Speech to Text Module Explanation

### Design

Processing criteria: Number of API calls that can be handled simultaneously is equal to limit to number of threads/processes set by system. I have created a cluster that can handle 8 (default) queues wherein each queue follows FIFO principle. There is a need to either vertically or horizontally scale the system to increase API handling concurrency. A threshold could be defined and the system can be load tested to know what’s the load the system can handle. 

### Queue System 

How to run clusters for queue:
```python manage.py qcluster```

How to enqueue tasks:
```python manage.py shell```

### Testing Queue System

How to track the tasks enqueued, success and failure of each
```python manage.py qmonitor```

### Speech to text 

Integrated by using a google library

### Screenshots for speech2text module

<img width="734" alt="Screen Shot 2022-03-30 at 6 01 39 PM" src="https://user-images.githubusercontent.com/42751267/160943622-3fd30dca-e09e-4701-ba29-2b90f293ee1b.png">

<img width="1440" alt="Screen Shot 2022-03-30 at 6 01 45 PM" src="https://user-images.githubusercontent.com/42751267/160943638-d5477739-ba0f-4216-87e5-1efc96db6bad.png">

<img width="709" alt="Screen Shot 2022-03-30 at 6 01 55 PM" src="https://user-images.githubusercontent.com/42751267/160943658-72d290a1-4d7a-4d7c-b890-a0ac3b04f05d.png">

