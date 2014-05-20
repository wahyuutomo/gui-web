<?php

	
	$command = $_POST['command'];
	
	if ($command=='auto'){
		$koneksi=mysql_connect("localhost", "root", "1214174");
		if ($koneksi){mysql_select_db("monitoring");}
		$result = mysql_query("SELECT lampu.auto FROM monitoring.lampu");
		
		$i=0;
		$auto=array();
		while ($row = mysql_fetch_array($result))
		{	
			$auto[$i]=$row['auto'];
			//echo $auto[0]."\n";
			$i=$i+1;
		}
		echo json_encode($auto);
	}
	
	if ($command=='jamon'){
		$koneksi=mysql_connect("localhost", "root", "1214174");
		if ($koneksi){mysql_select_db("monitoring");}
		$result = mysql_query("SELECT lampu.jam_on FROM monitoring.lampu");
		
		$i=0;
		$jamon=array();
		while ($row = mysql_fetch_array($result))
		{	
			$jamon[$i]=$row['jam_on'];
			//echo $jamon[$i]."\n";
			$i=$i+1;
		}
		echo json_encode($jamon);
	}
	
	if ($command=='jamoff'){
		$koneksi=mysql_connect("localhost", "root", "1214174");
		if ($koneksi){mysql_select_db("monitoring");}
		$result = mysql_query("SELECT lampu.jam_off FROM monitoring.lampu");
		
		$i=0;
		$jamoff=array();
		while ($row = mysql_fetch_array($result))
		{	
			$jamoff[$i]=$row['jam_off'];
			//echo $jamon[$i]."\n";
			$i=$i+1;
		}
		echo json_encode($jamoff);
	}
	
	if ($command=='meniton'){
		$koneksi=mysql_connect("localhost", "root", "1214174");
		if ($koneksi){mysql_select_db("monitoring");}
		$result = mysql_query("SELECT lampu.menit_on FROM monitoring.lampu");
		
		$i=0;
		$meniton=array();
		while ($row = mysql_fetch_array($result))
		{	
			$meniton[$i]=$row['menit_on'];
			//echo $jamon[$i]."\n";
			$i=$i+1;
		}
		echo json_encode($meniton);
	}	
	
	if ($command=='menitoff'){
		$koneksi=mysql_connect("localhost", "root", "1214174");
		if ($koneksi){mysql_select_db("monitoring");}
		$result = mysql_query("SELECT lampu.menit_off FROM monitoring.lampu");
		
		$i=0;
		$meniton=array();
		while ($row = mysql_fetch_array($result))
		{	
			$menitoff[$i]=$row['menit_off'];
			//echo $jamon[$i]."\n";
			$i=$i+1;
		}
		echo json_encode($menitoff);
	}		
	mysqli_close($koneksi);
?>
