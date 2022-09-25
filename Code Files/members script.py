#Save User Button
#scripting on the save user button action performed event
Address = event.source.parent.getComponent('Address').text
FName = event.source.parent.getComponent('FName').text
CCard = event.source.parent.getComponent('CCard').text
Mobile = event.source.parent.getComponent('Mobile').text

#error checking for blank inputs
if FName == '' or Address == '' or CCard == '' or Mobile == '':
	system.gui.messageBox('Please complete all fields')
else:

	try:
		system.db.runNamedQuery("insert member",{"Address":Address,"CCard":CCard,"FName" :FName, "Mobile" :Mobile})
						
		event.source.parent.getComponent('Address').text = ''
		event.source.parent.getComponent('FName').text = ''
		event.source.parent.getComponent('CCard').text = ''
		event.source.parent.getComponent('Mobile').text = ''
		system.db.runNamedQuery("select members")
	except:
		system.gui.messageBox('failed insert')

    
#Delete User Button
#scripting on the delete user button action performed event
table = event.source.parent.getComponent('Power Table') 

if table.selectedRow != -1:
 
    MemberID = table.data.getValueAt(table.selectedRow, "MemberID")
    system.db.runNamedQuery("delete member",{"MemberID":MemberID})
    system.db.runNamedQuery("select members")
else:  
	system.gui.messageBox('failed insert')
    
#Clear Button
event.source.parent.getComponent('Address').text = ''
event.source.parent.getComponent('FName').text = ''
event.source.parent.getComponent('CCard').text = ''
event.source.parent.getComponent('Mobile').text = ''
event.source.parent.getComponent('MemberID').text = ''

#table
#SQL statement that run on the table every polling rate interval
"SELECT MemberID, FName, Address, CCard, Mobile, lastUpdated FROM Members ORDER BY FName ASC, MemberID ASC"

table.pollingRate = 5