#Save Item Button
#scripting on the save item button action performed event
Name = event.source.parent.getComponent('Name').text
Price = event.source.parent.getComponent('Price').text
Stock_Quantity = event.source.parent.getComponent('Stock_Quantity').text
ItemID = event.source.parent.getComponent('ItemID').text

if Name == '' or Price == '' or Stock_Quantity == '':
	system.gui.messageBox('Please complete all fields')
else:
	sel_qry = "SELECT ItemID, Name, Price, Stock_quantity FROM Inventory WHERE ItemID = '%s'"
	result = system.db.runQuery(sel_qry % str(ItemID))
	if len(result) > 0:
		if system.gui.confirm('Update details for ItemID %s?' % ItemID):
			try:
				system.db.runNamedQuery("update inventory",{"Name":Name,"Price":Price,"Stock_Quantity" :Stock_Quantity, "ItemID" :ItemID})
							
				event.source.parent.getComponent('Name').text = ''
				event.source.parent.getComponent('Price').text = ''
				event.source.parent.getComponent('Stock_Quantity').text = ''
				event.source.parent.getComponent('ItemID').text = ''
			except:
				system.gui.messageBox('failed insert')
	else:
		try:
			system.db.runNamedQuery("insert inventory",{"Name":Name,"Price":Price,"Stock_Quantity" :Stock_Quantity})
					
			event.source.parent.getComponent('Name').text = ''
			event.source.parent.getComponent('Price').text = ''
			event.source.parent.getComponent('Stock_Quantity').text = ''
			system.db.runNamedQuery("select inventory")
		
		except:
			system.gui.messageBox('failed insert')
            
            
#Edit Item Button
#scripting on the edit item button action performed event
table = event.source.parent.getComponent('Power Table')
	
if table.selectedRow != -1:
		
	Name = table.data.getValueAt(table.selectedRow, "Name")
	Price = table.data.getValueAt(table.selectedRow, "Price")
	Stock_Quantity = table.data.getValueAt(table.selectedRow, "Stock_Quantity")
	ItemID = table.data.getValueAt(table.selectedRow, "ItemID")

		
	str_Price = str(Price)
	str_Stock_Quantity = str(Stock_Quantity)
	str_ItemID = str(ItemID)
		
	event.source.parent.getComponent('Name').text = Name
	event.source.parent.getComponent('Price').text = str_Price
	event.source.parent.getComponent('Stock_Quantity').text = str_Stock_Quantity
	event.source.parent.getComponent('ItemID').text = str_ItemID
	
else:  
	system.gui.messageBox("Please Select a Row!")     
    
#Delete Item Button
#scripting on the delete item button action performed event
table = event.source.parent.getComponent('Power Table') 

if table.selectedRow != -1:
 
    ItemID = table.data.getValueAt(table.selectedRow, "ItemID")
    system.db.runNamedQuery("delete inventory",{"ItemID":ItemID})
    
    system.db.runNamedQuery("select inventory")
else:  
	system.gui.messageBox('failed delete')
    
#clear Button
event.source.parent.getComponent('Name').text = ''
event.source.parent.getComponent('Price').text = ''
event.source.parent.getComponent('Stock_Quantity').text = ''


#table 
#SQL statement that run on the table every polling rate interval
'SELECT * FROM inventory'
table.pollingRate = 5