# Question 2: Auto Scaling Decision Script

### Problem:
Write a script that simulates a simple auto-scaling decision mechanism for a cloud service. The script will receive CPU utilisation as input of a list of instance and decide whether to scale up or scale down the number of servers.

1. If the average CPU utilisation is greater than 75% over the last 10 data points, scale up by increasing the number of servers by 1.
2. If the average CPU utilisation is below 25% over the last 10 data points, scale down by reducing the number of servers by 1.
3. Otherwise, maintain the current number of servers.

### Requirements:
1. Input: List of CPU utilisation percentages for the last 10 data points.
2. Output: A decision (scale up, scale down, or maintain current).

### Execution
```shell
docker build -t auto-scaling-script .
docker run --rm auto-scaling-script
```

### Output Can also be viewed in GitHubActions
* Navigate GitHub Actions
* Click on `Python Syntax Check and Docker Build` in the leftside panel.
* Select most recent successful run
* Expand `Run Docker Container`