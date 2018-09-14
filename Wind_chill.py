import sys

user_input = [float(i) for i in sys.argv[1:]]

def wind_chill(t, v):
	if -50 < t < 50 and 3 < v < 120:
		return 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * (v ** 0.16)
	else:
		return None

print("Today's wind chill is :", wind_chill(user_input[0], user_input[1]), "degrees Farenheit.")
