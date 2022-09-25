#Save User Button
#scripting on the save user button action performed event
Address = event.source.parent.getComponent('Address').text
FName = event.source.parent.getComponent('FName').text
CCard = event.source.parent.getComponent('CCard').text
Mobile = event.source.parent.getComponent('Mobile').text
MemberID = event.source.parent.getComponent('MemberID').text

if FName == '' or Address == '' or CCard == '' or Mobile == '':
	system.gui.messageBox('Please complete all fields')
else:
	sel_qry = "SELECT MemberID, FName, Address, CCard, Mobile FROM Members WHERE MemberID = '%s'"
	result = system.db.runQuery(sel_qry % str(MemberID))
	if len(result) > 0:
		if system.gui.confirm('Update details for MemberID %s?' % MemberID):
			try:
				##update query
				system.db.runNamedQuery("update member",{"Address":Address,"CCard":CCard,"FName" :FName, "Mobile" :Mobile, "MemberID" :MemberID})
				
				event.source.parent.getComponent('Address').text = ''
				event.source.parent.getComponent('FName').text = ''
				event.source.parent.getComponent('CCard').text = ''
				event.source.parent.getComponent('Mobile').text = ''
				event.source.parent.getComponent('MemberID').text = ''
				system.db.runNamedQuery("select members")
			except:
				system.gui.messageBox('failed to update user')
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


#Edit User Button
#scripting on the edit user button action performed event
table = event.source.parent.getComponent('Power Table')

if table.selectedRow != -1:
	
	FName = table.data.getValueAt(table.selectedRow, "FName")
	Address = table.data.getValueAt(table.selectedRow, "Address")
	CCard = table.data.getValueAt(table.selectedRow, "CCard")
	Mobile = table.data.getValueAt(table.selectedRow, "Mobile")
	MemberID = table.data.getValueAt(table.selectedRow, "MemberID")
	
	str_CCard = str(CCard)
	str_Mobile = str(Mobile)
	str_MemberID = str(MemberID)
	
	event.source.parent.getComponent('FName').text = FName
	event.source.parent.getComponent('Address').text = Address
	event.source.parent.getComponent('CCard').text = str_CCard
	event.source.parent.getComponent('Mobile').text = str_Mobile
	event.source.parent.getComponent('MemberID').text = str_MemberID
else:  
	system.gui.messageBox("Please Select a Row!") 
    
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