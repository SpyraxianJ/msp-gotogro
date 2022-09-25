# confirm sale  button
MemberID = event.source.parent.getComponent('MemberID').text
ItemID = event.source.parent.getComponent('ItemID').text
Quantity = event.source.parent.getComponent('Quantity').text

if MemberID == '' or ItemID == '' or Quantity == '':
	system.gui.messageBox('Please complete all fields')
	try:
		system.db.runNamedQuery("insert sale",{"Quantity" :Quantity,"MemberID" :MemberID,"ItemID" :ItemID})
							
		event.source.parent.getComponent('ItemID').text = ''
		event.source.parent.getComponent('Quantity').text = ''

	except:
		system.gui.messageBox('failed insert')


# cancel sale button
table = event.source.parent.getComponent('Power Table') 

if table.selectedRow != -1:
 
    ItemID = table.data.getValueAt(table.selectedRow, "ItemID")
    system.db.runNamedQuery("delete sale",{"ItemID":ItemID})
    
    system.db.runNamedQuery("select inventory")
else:  
	system.gui.messageBox('failed delete')