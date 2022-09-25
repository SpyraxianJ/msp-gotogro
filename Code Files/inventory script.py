#Save Item Button
#scripting on the save item button action performed event
Name = event.source.parent.getComponent('Name').text
Price = event.source.parent.getComponent('Price').text
Stock_Quantity = event.source.parent.getComponent('Stock_Quantity').text

if Name == '' or Price == '' or Stock_Quantity == '':
	system.gui.messageBox('Please complete all fields')
else:

	try:
		system.db.runNamedQuery("insert inventory",{"Name":Name,"Price":Price,"Stock_Quantity" :Stock_Quantity})
				
		event.source.parent.getComponent('Name').text = ''
		event.source.parent.getComponent('Price').text = ''
		event.source.parent.getComponent('Stock_Quantity').text = ''
		system.db.runNamedQuery("select inventory")
	
	except:
		system.gui.messageBox('failed insert')
               
    
#Delete Item Button
#scripting on the delete item button action performed event
table = event.source.parent.getComponent('Power Table') 

if table.selectedRow != -1:
 
    ItemID = table.data.getValueAt(table.selectedRow, "ItemID")
    system.db.runNamedQuery("delete inventory",{"ItemID":ItemID})
    
    system.db.runNamedQuery("select inventory")
else:  
	system.gui.messageBox('failed delete')


#table 
#SQL statement that run on the table every polling rate interval
'SELECT * FROM inventory'
table.pollingRate = 5