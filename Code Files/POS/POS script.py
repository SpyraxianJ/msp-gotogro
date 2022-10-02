#Enter Sale Button
MemberID = event.source.parent.getComponent('MemberID').text
ItemID = event.source.parent.getComponent('ItemID').text
Quantity = event.source.parent.getComponent('Quantity').text


if MemberID == '' or ItemID == '' or Quantity == '':
	system.gui.messageBox('Please complete all fields')
else:
	try:
		query="SELECT COUNT(ItemID) FROM inventory WHERE ItemID='%s'"
		recordExists=system.db.runScalarQuery(query % (str(ItemID)))
		 			
		if recordExists: 
		 	system.db.runNamedQuery("insert sale",{"Quantity" :Quantity,"MemberID" :MemberID,"ItemID" :ItemID})
		 	event.source.parent.getComponent('ItemID').text = ''
		 	event.source.parent.getComponent('Quantity').text = ''
		 	
		 	if event.source.parent.getComponent('Item Count').intValue== 0:
		 		event.source.parent.getComponent('Item Count').intValue = 1
		 	else:
		 		event.source.parent.getComponent('Item Count').intValue = event.source.parent.getComponent('Item Count').intValue + 1
		else: 
			system.gui.messageBox('item not found')
		
	except:
		system.gui.messageBox('failed insert')


#Confirm Sale button

event.source.parent.getComponent('Item Count').intValue = 0

#cancel item
table = event.source.parent.getComponent('Power Table') 
ItemID = table.data.getValueAt(table.selectedRow, "ItemID")

if table.selectedRow != -1:

 	system.db.runNamedQuery("delete sale",{"ItemID" :ItemID})
 	event.source.parent.getComponent('Item Count').intValue = event.source.parent.getComponent('Item Count').intValue -1
else: 
 	system.gui.messageBox('failed delete')

#clear all
event.source.parent.getComponent('MemberID').text = ''
event.source.parent.getComponent('Quantity').text = ''
event.source.parent.getComponent('ItemID').text = ''


#table data
"SELECT sales.t_stamp, sales.ItemID, sales.Quantity, inventory.Price FROM sales JOIN inventory ON inventory.ItemID = sales.ItemID ORDER BY t_stamp descLIMIT {Root Container.Item Count.intValue}"




