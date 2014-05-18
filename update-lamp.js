
jamon = function (j0,j1,j2,j3,j4,j5,j6,j7){
	$.post("/update-lamp.php", {jamon0:j0});
	$.post("/update-lamp.php", {jamon1:j1});
	$.post("/update-lamp.php", {jamon2:j2});
	$.post("/update-lamp.php", {jamon3:j3});
	$.post("/update-lamp.php", {jamon4:j4});
	$.post("/update-lamp.php", {jamon5:j5});
	$.post("/update-lamp.php", {jamon6:j6});
	$.post("/update-lamp.php", {jamon7:j7});
	return;
}

jamoff = function (jf0,jf1,jf2,jf3,jf4,jf5,jf6,jf7){
	$.post("/update-lamp.php", {jamoff0:jf0});
	$.post("/update-lamp.php", {jamoff1:jf1});
	$.post("/update-lamp.php", {jamoff2:jf2});
	$.post("/update-lamp.php", {jamoff3:jf3});
	$.post("/update-lamp.php", {jamoff4:jf4});
	$.post("/update-lamp.php", {jamoff5:jf5});
	$.post("/update-lamp.php", {jamoff6:jf6});
	$.post("/update-lamp.php", {jamoff7:jf7});
	return;
}

meniton = function (m0,m1,m2,m3,m4,m5,m6,m7){
	$.post("/update-lamp.php", {meniton0:m0});
	$.post("/update-lamp.php", {meniton1:m1});
	$.post("/update-lamp.php", {meniton2:m2});
	$.post("/update-lamp.php", {meniton3:m3});
	$.post("/update-lamp.php", {meniton4:m4});
	$.post("/update-lamp.php", {meniton5:m5});
	$.post("/update-lamp.php", {meniton6:m6});
	$.post("/update-lamp.php", {meniton7:m7});
	return;
}

menitoff = function (mf0,mf1,mf2,mf3,mf4,mf5,mf6,mf7){
	$.post("/update-lamp.php", {menitoff0:mf0});
	$.post("/update-lamp.php", {menitoff1:mf1});
	$.post("/update-lamp.php", {menitoff2:mf2});
	$.post("/update-lamp.php", {menitoff3:mf3});
	$.post("/update-lamp.php", {menitoff4:mf4});
	$.post("/update-lamp.php", {menitoff5:mf5});
	$.post("/update-lamp.php", {menitoff6:mf6});
	$.post("/update-lamp.php", {menitoff7:mf7});
	return;
}


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

update = function (j0,j1,j2,j3,j4,j5,j6,j7,jf0,jf1,jf2,jf3,jf4,jf5,jf6,jf7,m0,m1,m2,m3,m4,m5,m6,m7,mf0,mf1,mf2,mf3,mf4,mf5,mf6,mf7){
			$.post("/update-lamp.php",
			  {
				jamon0:j0,
				jamon1:j1,
				jamon2:j2,
				jamon3:j3,
				jamon4:j4,
				jamon5:j5,
				jamon6:j6,
				jamon7:j7,
				jamoff0:j0,
				jamoff1:j1,
				jamoff2:j2,
				jamoff3:j3,
				jamoff4:j4,
				jamoff5:j5,
				jamoff6:j6,
				jamoff7:j7,
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
				menitoff7:mf7
			  },
			//*  
			function(){
				  window.location.href="http://localhost/home.html";				  
				  }
			  );//*/
			  //return;
}
