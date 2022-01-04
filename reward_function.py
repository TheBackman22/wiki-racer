#reward function for racer_bot
	# awards points to the bot based on the number of links it took to
	# navigate from one page to another, as well as the 
	#amount of time the program toom to run

import constant

#in future reward functions, pass in 
# pass in the total number of clicks from all webpages navigates as
# well as the distance (number of links between starting page and current page on THIS PATH)
# and the displacement (number of links between starting page and current page on ANY VISITED PATH)

#simple reward function looks at starting page, ending page, distance, and time only
def simple_reward_function(current_page, ending_page, num_pages, time):

	reward = 0

	if current_page == ending_page:
		reward = (reward + 1) * 100
		# adjusts times in future as need be
		if time < 60: #total time less than 1 minute (60 seconds)
			reward = reward * 2
		elif time < 120: #two minutes
			reward =  reward * 1.5
		elif time < 180: #three minutes
			reward = reward * 1.2

	if num_pages <= constant.MAX_CLICKS:
		reward = reward * 1.2

	if num_pages == constant.MAX_CLICKS and current_page != ending_page:
		reward = 0

	return reward
	