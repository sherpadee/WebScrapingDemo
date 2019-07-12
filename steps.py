import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as fig

convert_tz = lambda x: x.to_pydatetime().replace(tzinfo=pytz.utc).astimezone(pytz.timezone('Asia/Shanghai'))
get_year = lambda x: convert_tz(x).year
get_month = lambda x: '{}-{:02}'.format(convert_tz(x).year, convert_tz(x).month) #inefficient
get_date = lambda x: '{}-{:02}-{:02}'.format(convert_tz(x).year, convert_tz(x).month, convert_tz(x).day) #inefficient
get_day = lambda x: convert_tz(x).day
get_hour = lambda x: convert_tz(x).hour
get_day_of_week = lambda x: convert_tz(x).weekday()

steps = pd.read_csv("HealthData.csv")
plot = steps.plot(x='Start', y='Steps', title= 'Daily step counts', figsize=[20, 6])
fig = plot.get_figure()
fig.savefig("steps.png")

steps_by_date = steps.groupby(['Start'])['Steps'].sum().reset_index(name='Steps')
print( tabulate(steps_by_date, headers='keys', tablefmt='psql') )


