# desktop notification inform you for system utilities (battery percentage)
# works in laptops
import psutil
from pynotifier import Notification


battery = psutil.sensors_battery()
percent = battery.percent
hello = "Hello User!"

Notification(title = 'Ποσοστό Μπαταρίας', description = str(round(percent,2)) + "%", duration = 5).send()
