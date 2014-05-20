
//*
coba= function (value){
			$.post("/update-lamp.php",
			  {jam:value},
			//*  
			function(){
				  window.location.href="http://localhost/home.html";				  }
			  );//*/
			  return;
}

//update = function (j0,j1,j2,j3,j4,j5,j6,j7,jf0,jf1,jf2,jf3,jf4,jf5,jf6,jf7,m0,m1,m2,m3,m4,m5,m6,m7,mf0,mf1,mf2,mf3,mf4,mf5,mf6,mf7){
update = function (lampu){			
			$.ajax(url:"/update-lamp.php",
			  type: "POST",
			  data: JSON.stringify(lampu),
			  contentType:"application/json;charset=UTF-8",
			  dataType:"json",
			//*  
			  complete: function(){
				  window.location.href="http://localhost/home.html";				  
				  }
			  );//*/
			  //return;
}





	
