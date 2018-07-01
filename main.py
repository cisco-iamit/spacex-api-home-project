"""
Print the total number of launches
and summary of last n launches.
"""

# you can import local modules, too. see spacex.py
from spasex import get_launches, recent_launches

launches = get_launches()
n_launches = len(launches)

print(f"SpaceX has launched {n_launches} rockets!")
n_recent_launches = int(input("How many recent launches do you want to see: "))

# scan the list of recent launches, one by one
for launch in recent_launches(n=n_recent_launches,
                              launches=launches):
    # assign text value based on a boolean value
    successful = "Yes" if launch['launch_success'] else "No"
    print(f"Mission name: {launch['mission_name']}\n"
          f"Date: {launch['launch_date_utc']}\n"
          f"Rocket: {launch['rocket']['rocket_name']}\n"
          f"Successful: {successful}\n\n")

