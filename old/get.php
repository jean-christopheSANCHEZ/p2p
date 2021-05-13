<?php
echo"calling python script get.py ...";

$ip = $_GET['get_ip'];
$port = $_GET['get_port'];
$key = $_GET['get_key'];
$command = "python3 /home/jc/Documents/cours/p2p/get.py " . $ip . " " . $port . " " . $key;
echo "with command : " . $command;
echo"<br>";
$out=null;
$out =shell_exec($command);
echo"<br>";
echo"<br>";
echo "output from the terminal : " . $out;
/*$msg = "Get result: None";
if ($out == $msg){
	echo "can not get the value corresponding the form key";
}else{
	echo "successfully get the value, output from the terminal : " . $out;
}*/

?>
