<?php
//	header('Content-Type: application/json');
	//$jam_on = $_POST['jam'];
	//*
//*
    $jamon0 = $_POST['jamon0'];
    $jamon1 = $_POST['jamon1'];
    $jamon2 = $_POST['jamon2'];
    $jamon3 = $_POST['jamon3'];
    $jamon4 = $_POST['jamon4'];
    $jamon5 = $_POST['jamon5'];
    $jamon6 = $_POST['jamon6'];
    $jamon7 = $_POST['jamon7'];
    $jamoff0 = $_POST['jamoff0'];
    $jamoff1 = $_POST['jamoff1'];
    $jamoff2 = $_POST['jamoff2'];
    $jamoff3 = $_POST['jamoff3'];
    $jamoff4 = $_POST['jamoff4'];
    $jamoff5 = $_POST['jamoff5'];
    $jamoff6 = $_POST['jamoff6'];
    $jamoff7 = $_POST['jamoff7'];
    $meniton0 = $_POST['meniton0'];
    $meniton1 = $_POST['meniton1'];
    $meniton2 = $_POST['meniton2'];
    $meniton3 = $_POST['meniton3'];
    $meniton4 = $_POST['meniton4'];
    $meniton5 = $_POST['meniton5'];
    $meniton6 = $_POST['meniton6'];
    $meniton7 = $_POST['meniton7'];
    $menitoff0 = $_POST['menitoff0'];
	$menitoff1 = $_POST['menitoff1'];
    $menitoff2 = $_POST['menitoff2'];
	$menitoff3 = $_POST['menitoff3'];
	$menitoff4 = $_POST['menitoff4'];
	$menitoff5 = $_POST['menitoff5'];
	$menitoff6 = $_POST['menitoff6'];
	$menitoff7 = $_POST['menitoff7'];
	//*/
	
	$auto0 = $_POST['auto0'];
	$auto1 = $_POST['auto1'];
	$auto2 = $_POST['auto2'];
	$auto3 = $_POST['auto3'];
	$auto4 = $_POST['auto4'];
	$auto5 = $_POST['auto5'];
	$auto6 = $_POST['auto6'];
	$auto7 = $_POST['auto7'];
	
	//*/
    
    $koneksi=mysql_connect("localhost", "root", "1214174");
    if ($koneksi){mysql_select_db("monitoring");}
  //  $sql=mysql_query("update lampu set jam_on='$jam_on', jam_off='$jam_off',menit_on='$menit_on', menit_off='$menit_off' WHERE id = 0");         
 //*
    $sql=mysql_query("update lampu set auto='$auto0', jam_on='$jamon0',menit_on='$meniton0',jam_off='$jamoff0',menit_off='$menitoff0' where id=0");
    $sql=mysql_query("update lampu set auto='$auto1', jam_on='$jamon1',menit_on='$meniton1',jam_off='$jamoff1',menit_off='$menitoff1' where id=1");
    $sql=mysql_query("update lampu set auto='$auto2', jam_on='$jamon2',menit_on='$meniton2',jam_off='$jamoff2',menit_off='$menitoff2' where id=2");
    $sql=mysql_query("update lampu set auto='$auto3', jam_on='$jamon3',menit_on='$meniton3',jam_off='$jamoff3',menit_off='$menitoff3' where id=3");
    $sql=mysql_query("update lampu set auto='$auto4', jam_on='$jamon4',menit_on='$meniton4',jam_off='$jamoff4',menit_off='$menitoff4' where id=4");
    $sql=mysql_query("update lampu set auto='$auto5', jam_on='$jamon5',menit_on='$meniton5',jam_off='$jamoff5',menit_off='$menitoff5' where id=5");
    $sql=mysql_query("update lampu set auto='$auto6', jam_on='$jamon6',menit_on='$meniton6',jam_off='$jamoff6',menit_off='$menitoff6' where id=6");
    $sql=mysql_query("update lampu set auto='$auto7', jam_on='$jamon7',menit_on='$meniton7',jam_off='$jamoff7',menit_off='$menitoff7' where id=7");
//*/    
	//mysqli_close($sql);
?>
