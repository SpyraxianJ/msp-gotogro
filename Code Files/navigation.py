# navigation scripting on each button
# the button for their own window has the formatting statically changed.
# i.e.indetend and now scripting
window = system.nav.openWindow('Inventory')
system.nav.centerWindow(window)

if mouseEntered() = true:
    event.source.buttonBG = system.gui.color(15,138,255) # turn the component blue
    event.source.foreground = system.gui.color(255,255,255) # turn the text white

else if mouseExited() = true:
    event.source.buttonBG = system.gui.color(250,250,251) # turn the component to white
    event.source.foreground = system.gui.color(46,46,46) # turn the text white