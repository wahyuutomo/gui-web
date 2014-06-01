
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

update = function (j0,j1,j2,j3,j4,j5,j6,j7,jf0,jf1,jf2,jf3,jf4,jf5,jf6,jf7,m0,m1,m2,m3,m4,m5,m6,m7,mf0,mf1,mf2,mf3,mf4,mf5,mf6,mf7,a0,a1,a2,a3,a4,a5,a6,a7){
			
			$.post("http://192.168.1.16/htdocs/update-lamp.php",
			  {
				jamon0:j0,
				jamon1:j1,
				jamon2:j2,
				jamon3:j3,
				jamon4:j4,
				jamon5:j5,
				jamon6:j6,
				jamon7:j7,
				jamoff0:jf0,
				jamoff1:jf1,
				jamoff2:jf2,
				jamoff3:jf3,
				jamoff4:jf4,
				jamoff5:jf5,
				jamoff6:jf6,
				jamoff7:jf7,
				meniton0:m0,
				meniton1:m1,
				meniton2:m2,
				meniton3:m3,
				meniton4:m4,
				meniton5:m5,
				meniton6:m6,
				meniton7:m7,
				menitoff0:mf0,
				menitoff1:mf1,
				menitoff2:mf2,
				menitoff3:mf3,
				menitoff4:mf4,
				menitoff5:mf5,
				menitoff6:mf6,
				menitoff7:mf7,
				auto0:a0,
				auto1:a1,
				auto2:a2,
				auto3:a3,
				auto4:a4,
				auto5:a5,
				auto6:a6,
				auto7:a7
			  },
			//*  
			function(){
				  window.location.href="http://192.168.1.16:8000/home.html";				  
				  }
			  );//*/
			  //return;
}





	
