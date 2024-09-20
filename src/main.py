CPU_DATA = [
    {
        "time": "2021-01-01T00:00:00Z",
        "value": [60, 65, 70, 80, 33, 40, 25, 22, 23, 24, 15, 20, 24, 19, 21, 25],
        "group_name": "group-1",
        "number_of_servers": 2
    },
    {
        "time": "2021-01-01T00:00:00Z",
        "value": [60, 65, 70, 80, 85, 90, 68, 72, 73, 74],
        "group_name": "group-2",
        "number_of_servers": 3
    },
    {
        "time": "2021-01-01T00:00:00Z",
        "value": [90, 88, 62, 83, 84, 85, 90, 74, 90, 95],
        "group_name": "group-3",
        "number_of_servers": 7
    },
    {
        "time": "2021-01-01T00:00:00Z",
        "value": [60, 80, 85, 90, 68, 72, 72, 73, 74, 55, 60, 61],
        "group_name": "group-4",
        "number_of_servers": 4
    },
    {
        "time": "2021-01-01T00:00:00Z",
        "value": [20, 15, 10, 6, 23, 10, 18, 21, 23, 11, 21, 24, 22],
        "group_name": "group-5",
        "number_of_servers": 4
    },
]


def auto_scaling_decision(cpu_data: list[int], current_servers: int) -> tuple[str, int]:
    last_10_data = cpu_data[-10:]

    avg_cpu = sum(last_10_data) / len(last_10_data)

    if avg_cpu > 75:
        return "scale up", current_servers + 1
    elif avg_cpu < 25:
        return "scale down", current_servers - 1 if current_servers > 1 else current_servers
    else:
        return "maintain current", current_servers


if __name__ == "__main__":
    for group in CPU_DATA:
        decision, updated_servers = auto_scaling_decision(group['value'], group['number_of_servers'])
        print(f"Group {group['group_name']}: {decision} to {updated_servers} servers")
