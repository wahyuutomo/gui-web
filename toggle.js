// function init() defines function passed to webiopi().ready()
// NOTE* Change ("mcp") to the expander-name you designated in your config file
/*function init() {
		mcp = new GPIOPort("mcp");
        mcp2 = new GPIOPort("mcp2");
		mcp3 = new GPIOPort("mcp3");
		
		// refresh UI each seconds
		setInterval(updateUI, 3000);
}//*/

/*/ function called through setInterval
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
}//*/

toggleswitch0 =   function (mcp) {
		if(switch0.checked) {
                      mcp.digitalWrite(0, 1, DigitalCallback);  }
		else {	
                      mcp.digitalWrite(0, 0, DigitalCallback);  }
		}
		
toggleswitch1 = function (mcp) {		
		if(switch1.checked) {
                      mcp.digitalWrite(1, 1, DigitalCallback);  }
		else {	
                      mcp.digitalWrite(1, 0, DigitalCallback);  }
		}
toggleswitch2 = function (mcp) {	
		if(switch2.checked) {
                      mcp.digitalWrite(2, 1, DigitalCallback);  }
		else {	
                      mcp.digitalWrite(2, 0, DigitalCallback);  }
		}
toggleswitch3 = function (mcp) {
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
		
		
		 // called by switch onclickMCP2

toggleswitch20 = function (mcp2) {
		if(switch20.checked) {
                      mcp2.digitalWrite(0, 1, DigitalCallback2);  }
		else {	
                      mcp2.digitalWrite(0, 0, DigitalCallback2);  }
		}
toggleswitch21 = function (mcp2) {		
		if(switch21.checked) {
                      mcp2.digitalWrite(1, 1, DigitalCallback2);  }
		else {	
                      mcp2.digitalWrite(1, 0, DigitalCallback2);  }
		}
toggleswitch22 = function (mcp2) {	
		if(switch22.checked) {
                      mcp2.digitalWrite(2, 1, DigitalCallback2);  }
		else {	
                      mcp2.digitalWrite(2, 0, DigitalCallback2);  }
		}
toggleswitch23 = function (mcp2) {
		if(switch23.checked) {
                      mcp2.digitalWrite(3, 1, DigitalCallback2);  }
		else {	
                      mcp2.digitalWrite(3, 0, DigitalCallback2);  }
		}
        function toggleswitch24() {
		if(switch24.checked) {
                      mcp2.digitalWrite(4, 1, DigitalCallback2);  }
		else {	
                      mcp2.digitalWrite(4, 0, DigitalCallback2);  }
		}
        function toggleswitch25() {		
		if(switch25.checked) {
                      mcp2.digitalWrite(5, 1, DigitalCallback2);  }
		else {	
                      mcp2.digitalWrite(5, 0, DigitalCallback2);  }
		}
        function toggleswitch26() {	
		if(switch26.checked) {
                      mcp2.digitalWrite(6, 1, DigitalCallback2);  }
		else {	
                      mcp2.digitalWrite(6, 0, DigitalCallback2);  }
		}
        function toggleswitch27() {
		if(switch27.checked) {
                      mcp2.digitalWrite(7, 1, DigitalCallback2);  }
		else {	
                      mcp2.digitalWrite(7, 0, DigitalCallback2);  }
		}
		
		 // called by switch onclickMCP3

        function toggleswitch30() {
		if(switch30.checked) {
                      mcp3.digitalWrite(0, 1, DigitalCallback3);  }
		else {	
                      mcp3.digitalWrite(0, 0, DigitalCallback3);  }
		}
        function toggleswitch31() {		
		if(switch31.checked) {
                      mcp3.digitalWrite(1, 1, DigitalCallback3);  }
		else {	
                      mcp3.digitalWrite(1, 0, DigitalCallback3);  }
		}
        function toggleswitch32() {	
		if(switch32.checked) {
                      mcp3.digitalWrite(2, 1, DigitalCallback3);  }
		else {	
                      mcp3.digitalWrite(2, 0, DigitalCallback3);  }
		}
        function toggleswitch33() {
		if(switch33.checked) {
                      mcp3.digitalWrite(3, 1, DigitalCallback3);  }
		else {	
                      mcp3.digitalWrite(3, 0, DigitalCallback3);  }
		}
        function toggleswitch34() {
		if(switch34.checked) {
                      mcp3.digitalWrite(4, 1, DigitalCallback3);  }
		else {	
                      mcp3.digitalWrite(4, 0, DigitalCallback3);  }
		}
        function toggleswitch35() {		
		if(switch35.checked) {
                      mcp3.digitalWrite(5, 1, DigitalCallback3);  }
		else {	
                      mcp3.digitalWrite(5, 0, DigitalCallback3);  }
		}
        function toggleswitch36() {	
		if(switch36.checked) {
                      mcp3.digitalWrite(6, 1, DigitalCallback3);  }
		else {	
                      mcp3.digitalWrite(6, 0, DigitalCallback3);  }
		}
        function toggleswitch37() {
		if(switch37.checked) {
                      mcp3.digitalWrite(7, 1, DigitalCallback3);  }
		else {	
                      mcp3.digitalWrite(7, 0, DigitalCallback3);  }
		}

        // test returned value and set appropriate CSS class on the button
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
		
		
 // test returned value and set appropriate CSS class on the button MCP2
        function DigitalCallback2(mcp2, channel, value){
	 var i = channel;
		if (i==0){
                	if (value==0) {
                                   $('#switch20').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch20').prop('checked', 'checked');	}
        	}
		if (i==1){
                	if (value==0) {
                                   $('#switch21').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch21').prop('checked', 'checked');	}
        	}
		if (i==2){
                	if (value==0) {
                                   $('#switch22').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch22').prop('checked', 'checked');	}
        	}
		if (i==3){
                	if (value==0) {
                                   $('#switch23').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch23').prop('checked', 'checked');	}
        	}			
		if (i==4){
                	if (value==0) {
                                   $('#switch24').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch24').prop('checked', 'checked');	}
        	}
		if (i==5){
                	if (value==0) {
                                   $('#switch25').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch25').prop('checked', 'checked');	}
        	}
		if (i==6){
                	if (value==0) {
                                   $('#switch26').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch26').prop('checked', 'checked');	}
        	}
		if (i==7){
                	if (value==0) {
                                   $('#switch27').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch27').prop('checked', 'checked');	}
        	}
        }
		
 // test returned value and set appropriate CSS class on the button MCP2
        function DigitalCallback3(mcp3, channel, value){
	 var i = channel;
		if (i==0){
                	if (value==0) {
                                   $('#switch30').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch30').prop('checked', 'checked');	}
        	}
		if (i==1){
                	if (value==0) {
                                   $('#switch31').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch31').prop('checked', 'checked');	}
        	}
		if (i==2){
                	if (value==0) {
                                   $('#switch32').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch32').prop('checked', 'checked');	}
        	}
		if (i==3){
                	if (value==0) {
                                   $('#switch33').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch33').prop('checked', 'checked');	}
        	}			
		if (i==4){
                	if (value==0) {
                                   $('#switch34').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch34').prop('checked', 'checked');	}
        	}
		if (i==5){
                	if (value==0) {
                                   $('#switch35').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch35').prop('checked', 'checked');	}
        	}
		if (i==6){
                	if (value==0) {
                                   $('#switch36').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch36').prop('checked', 'checked');	}
        	}
		if (i==7){
                	if (value==0) {
                                   $('#switch37').prop('checked', false);	}
        		else if (value==1) {
               			$('#switch37').prop('checked', 'checked');	}
        	}
        }
		
