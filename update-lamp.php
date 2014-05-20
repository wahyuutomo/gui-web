<?php
	header('Content-Type: application/json');
	//$jam_on = $_POST['jam'];
	//*
    $jamon0 = $_POST['lampu[0].jamon'];
    $jamon1 = $_POST['lampu[1].jamon'];
    $jamon2 = $_POST['lampu[2].jamon'];
    $jamon3 = $_POST['lampu[3].jamon'];
    $jamon4 = $_POST['lampu[4].jamon'];
    $jamon5 = $_POST['lampu[5].jamon'];
    $jamon6 = $_POST['lampu[6].jamon'];
    $jamon7 = $_POST['lampu[7].jamon'];
    
    $jamoff0 = $_POST['lampu[0].jamoff'];
    $jamoff1 = $_POST['lampu[1].jamoff'];
    $jamoff2 = $_POST['lampu[2].jamoff'];
    $jamoff3 = $_POST['lampu[3].jamoff'];
    $jamoff4 = $_POST['lampu[4].jamoff'];
    $jamoff5 = $_POST['lampu[5].jamoff'];
    $jamoff6 = $_POST['lampu[6].jamoff'];
    $jamoff7 = $_POST['lampu[7].jamoff'];
    
    $meniton0 = $_POST['lampu[0].meniton'];
    $meniton1 = $_POST['lampu[1].meniton'];
    $meniton2 = $_POST['lampu[2].meniton'];
    $meniton3 = $_POST['lampu[3].meniton'];
    $meniton4 = $_POST['lampu[4].meniton'];
    $meniton5 = $_POST['lampu[5].meniton'];
    $meniton6 = $_POST['lampu[6].meniton'];
    $meniton7 = $_POST['lampu[7].meniton'];
    
    $menitoff0 = $_POST['lampu[0].menitoff'];
	$menitoff1 = $_POST['lampu[1].menitoff'];
    $menitoff2 = $_POST['lampu[2].menitoff'];
	$menitoff3 = $_POST['lampu[3].menitoff'];
	$menitoff4 = $_POST['lampu[4].menitoff'];
	$menitoff5 = $_POST['lampu[5].menitoff'];
	$menitoff6 = $_POST['lampu[6].menitoff'];
	$menitoff7 = $_POST['lampu[7].menitoff'];
	
	$auto0 = $_POST['lampu[0].auto'];
	$auto1 = $_POST['lampu[1].auto'];
	$auto2 = $_POST['lampu[2].auto'];
	$auto3 = $_POST['lampu[3].auto'];
	$auto4 = $_POST['lampu[4].auto'];
	$auto5 = $_POST['lampu[5].auto'];
	$auto6 = $_POST['lampu[6].auto'];
	$auto7 = $_POST['lampu[7].auto'];
	
	//*/
    
    $koneksi=mysql_connect("localhost", "root", "1214174");
    if ($koneksi){mysql_select_db("monitoring");}
  //  $sql=mysql_query("update lampu set jam_on='$jam_on', jam_off='$jam_off',menit_on='$menit_on', menit_off='$menit_off' WHERE id = 0");         
 /*
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
