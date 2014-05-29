
<?php 

//random
if (isset($_POST['btn-random']))
	{
        exec('screen -p 0 -S phplay -X kill');
	exec('screen -dmS phplay mpg321 -Z /home/pi/music/*');
	}

if (isset($_POST['btn-stoprandom']))
	{
	exec('screen -p 0 -S phplay -X kill');
	}

//Bengawan Solo.mp3
if (isset($_POST['play0']))
	{
        exec('screen -p 0 -S phplay -X kill');
	exec('screen -dmS phplay mpg321 /home/pi/music/BengawanSolo.mp3');
	}

if (isset($_POST['stop0']))
	{
	exec('screen -p 0 -S phplay -X kill');
	}

//Caping Gunung.mp3
if (isset($_POST['play1']))
	{
        exec('screen -p 0 -S phplay -X kill');
	exec('screen -dmS phplay mpg321 /home/pi/music/CapingGunung.mp3');
	}

if (isset($_POST['stop1']))
	{
	exec('screen -p 0 -S phplay -X kill');
	}

//Keroncong Kemayoran.mp3
if (isset($_POST['play2']))
	{
        exec('screen -p 0 -S phplay -X kill');
	exec('screen -dmS phplay mpg321 /home/pi/music/KeroncongKemayoran.mp3');
	}

if (isset($_POST['stop2']))
	{
	exec('screen -p 0 -S phplay -X kill');
	}

//Rangkaian Melati.mp3
if (isset($_POST['play3']))
	{
        exec('screen -p 0 -S phplay -X kill');
	exec('screen -dmS phplay mpg321 /home/pi/music/RangkaianMelati.mp3');
	}

if (isset($_POST['stop3']))
	{
	exec('screen -p 0 -S phplay -X kill');
	}

//Sapu Tangan.mp3
if (isset($_POST['play4']))
	{
        exec('screen -p 0 -S phplay -X kill');
	exec('screen -dmS phplay mpg321 /home/pi/music/SapuTangan.mp3');
	}

if (isset($_POST['stop4']))
	{
	exec('screen -p 0 -S phplay -X kill');
	}

//Mozart remix.mp3
if (isset($_POST['play5']))
	{
        exec('screen -p 0 -S phplay -X kill');
	exec('screen -dmS phplay mpg321 /home/pi/music/MozartRemix.mp3');
	}

if (isset($_POST['stop5']))
	{
	exec('screen -p 0 -S phplay -X kill');
	}

//Viva La Vida.mp3
if (isset($_POST['play6']))
	{
        exec('screen -p 0 -S phplay -X kill');
	exec('screen -dmS phplay mpg321 /home/pi/music/Viva.mp3');
	}

if (isset($_POST['stop6']))
	{
        exec('screen -p 0 -S phplay -X kill');
	}

//Kuntilanak.mp3
if (isset($_POST['play7']))
	{
	exec('screen -dmS phplay mpg321 /home/pi/music/lain/kuntilanak.mp3');
	}

if (isset($_POST['stop7']))
	{
	exec('screen -p 0 -S phplay -X kill');
	}


?>
