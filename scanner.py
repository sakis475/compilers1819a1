"""
Sample script to test ad-hoc scanning by table drive.
This accepts a number with optional decimal part [0-9]+(\.[0-9]+)?
NOTE: suitable for optional matches
"""



def getchar(text,pos):
	""" returns char category at position `pos` of `text`,
	or None if out of bounds """
	
	if pos<0 or pos>=len(text): return None
	
	c = text[pos]
	
	# **Σημείο #3**: Προαιρετικά, προσθέστε τις δικές σας ομαδοποιήσεις
	
	

	if c > '0' and c <= '2': return '1OR2'

	if c >= '6' and c <= '9': return 'BIGGERTHANFIVE'


	# Αν δευ είναι όλα τα παραπάνω, επέστρεψε το χαρακτήρα αυτούσιο
	return c;

	


def scan(text,transitions,accepts):
	""" scans `text` while transitions exist in
	'transitions'. After that, if in a state belonging to
	`accepts`, it returns the corresponding token, else ERROR_TOKEN.
	"""
	
	# initial state
	pos = 0
	state = 's0'
	# memory for last seen accepting states
	last_token = None
	last_pos = None
	
	
	while True:
		
		c = getchar(text,pos)	# get next char (category)
		
		if state in transitions and c in transitions[state]:
			state = transitions[state][c]	# set new state
			pos += 1	# advance to next char
			
			# remember if current state is accepting
			if state in accepts:
				last_token = accepts[state]
				last_pos = pos
			
		else:	# no transition found

			if last_token is not None:	# if an accepting state already met
				return last_token,last_pos
			
			# else, no accepting state met yet
			return 'ERROR_TOKEN',pos
			
	
# **Σημείο #1**: Αντικαταστήστε με το δικό σας λεξικό μεταβάσεων
transitions = { 
       			's0': {'3':'s3' ,'1OR2':'s1', '0' : 's1'},
       			's1': {'0':'s2', '3':'s2' ,'1OR2' : 's2' ,'4' : 's2', '5' : 's2','BIGGERTHANFIVE':'s2' },
       			's2': {'0':'s5', '3':'s5' ,'1OR2' : 's5' ,'4' : 's5', '5' : 's5','BIGGERTHANFIVE':'s5'},
       			's3': {'5' : 's4','0':'s2', '3':'s2' ,'1OR2' : 's2' ,'4' : 's2'},
       			's4': {'0':'s5'},
       			's5': {'0':'s6', '3':'s6' ,'1OR2' : 's6' ,'4' : 's6', '5' : 's6','BIGGERTHANFIVE':'s6'},
       			's6': {'0':'s7', '3':'s7' ,'1OR2' : 's7' ,'4' : 's7', '5' : 's7','BIGGERTHANFIVE':'s7'},
       			's7': {'G' : 's13', 'K' : 's8', 'M' : 's10'},
       			's8': {'T' : 's9'},
       			's10': {'P':'s11'},
       			's11': {'S' : 's9'},
       			's13': {'0':'s14', '3':'s14' ,'1OR2' : 's14' ,'4' : 's14', '5' : 's14', 'BIGGERTHANFIVE':'s14'},
       			's14': {'0':'s15', '3':'s15' ,'1OR2' : 's15' ,'4' : 's15', '5' : 's15', 'BIGGERTHANFIVE':'s15'},
       			's15': {'K': 's8', 'M' : 's10'}
       			

     		  } 

# **Σημείο #2**: Αντικαταστήστε με το δικό σας λεξικό καταστάσεων αποδοχής
accepts = { 's9':'WIND_TOKEN'
     	  }


# get a string from input
text = input('give some input>')

# scan text until no more input
while text:		# i.e. len(text)>0
	# get next token and position after last char recognized
	token,pos = scan(text,transitions,accepts)
	if token=='ERROR_TOKEN':
		print('unrecognized input at position',pos,'of',text)
		break
	print("token:",token,"text:",text[:pos])
	# new text for next scan
	text = text[pos:]
