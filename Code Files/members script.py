#Save User Button
#scripting on the save user button action performed event

#gets text frrom botton compononets and save to a variable 
Address = event.source.parent.getComponent('Address').text
FName = event.source.parent.getComponent('FName').text
CCard = event.source.parent.getComponent('CCard').text
Mobile = event.source.parent.getComponent('Mobile').text

#puts this into a name query to insert into SQL else outputs error message
try:
	system.db.runNamedQuery("insert member",{"Address":Address,"CCard":CCard,"FName" :FName, "Mobile" :Mobile})
					
	event.source.parent.getComponent('Address').text = ''
	event.source.parent.getComponent('FName').text = ''
	event.source.parent.getComponent('CCard').text = ''
	event.source.parent.getComponent('Mobile').text = ''
	system.db.runNamedQuery("select members")
except:
	system.gui.messageBox('failed insert')

#table
#SQL statement that run on the table every polling rate interval
"SELECT MemberID, FName, Address, CCard, Mobile, lastUpdated FROM Members ORDER BY FName ASC, MemberID ASC"

table.pollingRate = 5