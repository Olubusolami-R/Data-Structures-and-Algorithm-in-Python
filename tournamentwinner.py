def tournamentWinner(competitions, results):
    # Write your code here.]
	#declare dictionary to store the cummulative points
	points={}
	for i in range(len(results)):
		#if hometeam wins in pair
		if results[i]==1:
			#store name of home team
			home=competitions[i][0]
			#if hometeam already won increment point
			if home in points:
				points[home]+=1
			#else initialize to 1
			else:
				points[home]=1
		else: #away team won
			away=competitions[i][1]
			#if away team already won increment point
			if away in points:
				points[away]+=1
			#else initialize to 1
			else:
				points[away]=1
	maximum=''
	maxpt=0
	for key,value in points.items():
		if value>maxpt:
			maxpt=value
			maximum=key
	
    return maximum
