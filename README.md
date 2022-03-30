# Patient Monitoring System with Django + New Module

## Migrated my previous repository Patient-Monitoring-System to Django and added a Speech to text module that implements a queue management system

This repository fulfils Project 4 for the class EC 530. (Ignore this statement if you are not a TA/Professor for the BU class EC 530)

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

