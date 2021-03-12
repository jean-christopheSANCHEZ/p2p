<?php
echo"calling python script set.py ...";


$ip = $_GET['set_ip'];
$port = $_GET['set_port'];
$key = $_GET['set_key'];
$value = $_GET['set_value'];
$command = "python3 /home/jc/Documents/cours/p2p/set.py " . $ip . " " . $port . " " . $key . " " . $value;
echo "with command : " . $command;
echo"<br>";
$out=null;
$status=null;
$out =shell_exec($command);
echo"<br>";
echo"<br>";
echo "output from the terminal : " . $out;
/*
if ($out == "Get result: None"){
	echo "can not set the value";
}else{
	echo "successfully set the value, output from the terminal : " . $out;
}*/

?>
