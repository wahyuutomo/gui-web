// function init() defines function passed to webiopi().ready()
// NOTE* Change ("mcp") to the expander-name you designated in your config file
function init() {
		mcp = new GPIOPort("mcp");
        mcp2 = new GPIOPort("mcp2");
		mcp3 = new GPIOPort("mcp3");
		
		// refresh UI each seconds
		setInterval(updateUI, 3000);
}

// function called through setInterval
function updateUI() {
// call MCP.digitalRead 0 to 7 REST API
			if (mcp.isReady()) {
					for (var i=0;i<8;i++)
					{
						mcp.digitalRead(i, DigitalCallback);	 
						mcp2.digitalRead(i, DigitalCallback2);
						mcp3.digitalRead(i, DigitalCallback3);
					}
				}
}

function toggleswitch0() {
	if(switch0.checked) {
				  mcp.digitalWrite(0, 1, DigitalCallback);  }
	else {	
				  mcp.digitalWrite(0, 0, DigitalCallback);  }
}
		
function toggleswitch1() {		
	if(switch1.checked) {
				  mcp.digitalWrite(1, 1, DigitalCallback);  }
	else {	
				  mcp.digitalWrite(1, 0, DigitalCallback);  }
}

function toggleswitch2() {	
	if(switch2.checked) {
				  mcp.digitalWrite(2, 1, DigitalCallback);  }
	else {	
				  mcp.digitalWrite(2, 0, DigitalCallback);  }
}

function toggleswitch3() {
	if(switch3.checked) {
				  mcp.digitalWrite(3, 1, DigitalCallback);  }
	else {	
				  mcp.digitalWrite(3, 0, DigitalCallback);  }
}

function toggleswitch4() {
	if(switch4.checked) {
				  mcp.digitalWrite(4, 1, DigitalCallback);  }
	else {	
				  mcp.digitalWrite(4, 0, DigitalCallback);  }
}

function toggleswitch5() {		
	if(switch5.checked) {
				  mcp.digitalWrite(5, 1, DigitalCallback);  }
	else {	
				  mcp.digitalWrite(5, 0, DigitalCallback);  }
}

function toggleswitch6() {	
	if(switch6.checked) {
				  mcp.digitalWrite(6, 1, DigitalCallback);  }
	else {	
				  mcp.digitalWrite(6, 0, DigitalCallback);  }
}

function toggleswitch7() {
	if(switch7.checked) {
				  mcp.digitalWrite(7, 1, DigitalCallback);  }
	else {	
				  mcp.digitalWrite(7, 0, DigitalCallback);  }
}

function DigitalCallback(mcp, channel, value){
	var i = channel;
	if (i==0){
			if (value==0) {
					$('#switch0').prop('checked', false);	}
			else if (value==1) {
					$('#switch0').prop('checked', 'checked');	}
		}
	if (i==1){
			if (value==0) {
					$('#switch1').prop('checked', false);	}
			else if (value==1) {
					$('#switch1').prop('checked', 'checked');	}
		}
	if (i==2){
			if (value==0) {
					$('#switch2').prop('checked', false);	}
			else if (value==1) {
					$('#switch2').prop('checked', 'checked');	}
		}
	if (i==3){
			if (value==0) {
					$('#switch3').prop('checked', false);	}
			else if (value==1) {
					$('#switch3').prop('checked', 'checked');	}
		}			
	if (i==4){
			if (value==0) {
					$('#switch4').prop('checked', false);	}
			else if (value==1) {
					$('#switch4').prop('checked', 'checked');	}
		}
	if (i==5){
			if (value==0) {
					$('#switch5').prop('checked', false);	}
			else if (value==1) {
					$('#switch5').prop('checked', 'checked');	}
		}
	if (i==6){
			if (value==0) {
					$('#switch6').prop('checked', false);	}
			else if (value==1) {
					$('#switch6').prop('checked', 'checked');	}
		}
	if (i==7){
			if (value==0) {
					$('#switch7').prop('checked', false);	}
			else if (value==1) {
					$('#switch7').prop('checked', 'checked');	}
		}
}
