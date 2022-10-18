#Save User Button
#scripting on the save user button action performed event
import re

Address = event.source.parent.getComponent('Address').text
FName = event.source.parent.getComponent('FName').text
Email = event.source.parent.getComponent('Email').text
Mobile = event.source.parent.getComponent('Mobile').text
MemberID = event.source.parent.getComponent('MemberID').text

#result = re.search(pattern, target_string)
emailCheck = re.match(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', Email)
addressCheck = re.match(r'^\d+\s[A-z]+\s[A-z]+', Address)
fnameCheck = re.match(r'^[^0-9]+$', FName)
mobileCheck = re.match(r'\d{10}', Mobile)

print(emailCheck) 
print(addressCheck) 
print(fnameCheck) 
print(mobileCheck) 

#check for blank inputs
if FName == '' or Address == '' or Email == '' or Mobile == '':
	system.gui.messageBox('Please complete all fields')
#check for regex compliance
elif emailCheck!= None and addressCheck!= None and fnameCheck!= None and mobileCheck != None:
		sel_qry = "SELECT MemberID, FName, Address, Email, Mobile FROM Members WHERE MemberID = '%s'"
		result = system.db.runQuery(sel_qry % str(MemberID))
		if len(result) > 0:
			if system.gui.confirm('Update details for MemberID %s?' % MemberID):
				try:
					##update query
					system.db.runNamedQuery("update member",{"Address":Address,"Email":Email,"FName" :FName, "Mobile" :Mobile, "MemberID" :MemberID})
				
					event.source.parent.getComponent('Address').text = ''
					event.source.parent.getComponent('FName').text = ''
					event.source.parent.getComponent('Email').text = ''
					event.source.parent.getComponent('Email').text = ''
					event.source.parent.getComponent('Mobile').text = ''
					event.source.parent.getComponent('MemberID').text = ''
				except:
					system.gui.messageBox('failed to update user')
		else:
			try:
				system.db.runNamedQuery("insert member",{"Address":Address,"Email":Email,"FName" :FName, "Mobile" :Mobile})
							
				event.source.parent.getComponent('Address').text = ''
				event.source.parent.getComponent('FName').text = ''
				event.source.parent.getComponent('Email').text = ''
				event.source.parent.getComponent('Mobile').text = ''

			except:
				system.gui.messageBox('failed to insert new member')
else:
	system.gui.messageBox("Incorrect Formatting.\n")


#Edit User Button
#scripting on the edit user button action performed event
table = event.source.parent.getComponent('Power Table')
if event.source.selected == 1:
	if table.selectedRow != -1:
		
		FName = table.data.getValueAt(table.selectedRow, "FName")
		Address = table.data.getValueAt(table.selectedRow, "Address")
		Email = table.data.getValueAt(table.selectedRow, "Email")
		Mobile = table.data.getValueAt(table.selectedRow, "Mobile")
		MemberID = table.data.getValueAt(table.selectedRow, "MemberID")
		
		str_Email = str(Email)
		str_Mobile = str(Mobile)
		str_MemberID = str(MemberID)
		
		event.source.parent.getComponent('FName').text = FName
		event.source.parent.getComponent('Address').text = Address
		event.source.parent.getComponent('Email').text = str_Email
		event.source.parent.getComponent('Mobile').text = str_Mobile
		event.source.parent.getComponent('MemberID').text = str_MemberID
		event.source.text = "Exit Editing"
	else:
		event.source.selected = 0
		system.gui.messageBox("Please Select a Row!") 
else:
	event.source.parent.getComponent('Address').text = ''
	event.source.parent.getComponent('FName').text = ''
	event.source.parent.getComponent('Email').text = ''
	event.source.parent.getComponent('Mobile').text = ''
	event.source.parent.getComponent('MemberID').text = ''
	event.source.parent.getComponent('Group').getComponent('Search').text = ''
	event.source.text = "Edit Users"
	table.selectedRow = -1
    
#Delete User Button
#scripting on the delete user button action performed event
table = event.source.parent.getComponent('Power Table') 

if table.selectedRow != -1:
    MemberID = table.data.getValueAt(table.selectedRow, "MemberID")
    if system.gui.confirm('Delete Member?'):
    	system.db.runNamedQuery("delete member",{"MemberID":MemberID})
else:  
	system.gui.messageBox('failed insert')
    
#Clear Button
#clears last inputted value
event.source.parent.getComponent('Address').text = ''
event.source.parent.getComponent('FName').text = ''
event.source.parent.getComponent('Email').text = ''
event.source.parent.getComponent('Mobile').text = ''
event.source.parent.getComponent('MemberID').text = ''
event.source.parent.getComponent('Group').getComponent('Search').text - ''


#clears last accepted value
event.source.parent.getComponent('Email').committedValue = ''
event.source.parent.getComponent('Address').committedValue = ''

#table
#SQL statement that run on the table every polling rate interval
"SELECT MemberID, FName, Address, Email, Mobile, lastUpdated FROM Members WHERE MemberID LIKE '%{Root Container.Group.Search.text}'ORDER BY FName ASC, MemberID ASC"
table.pollingRate = 1

#regex used on text field

Address = '\d{1,3}.?\d{0,3}\s[a-zA-Z]{2,30}\s[a-zA-Z]{2,15}'
Email = '([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'