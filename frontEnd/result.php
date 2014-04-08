<?php
/**
 * Created by PhpStorm.
 * User: Elizabeth
 * Date: 8/04/14
 * Time: 8:35 PM
 */

    $file = file_get_contents("dbFile.json", 'r');
    $dbFile = json_decode($file, true);
    $employees = array();
    foreach ($dbFile as $a => $b){
        $tempArray = array();
        foreach ($b as $c => $d){

            array_push($tempArray, $d);
        }
        array_push($employees, $tempArray);
    }
?>
<!DOCTYPE html>
<html>
<head>
    <title>Form 1 Test</title>
</head>
<body>
    <h1>Your Details have been gotten</h1>
    <?php
        $id = $_REQUEST["employee"]-1;
        $name = $employees[$id][1];
        $startDate = $_REQUEST["startDate"];
        $startTime = $_REQUEST["startTime"];
        $endTime = $_REQUEST["endTime"];

        echo ("<h2>Pure Values</h2>");
        echo("name: ".$name."<br/>start date: ".$startDate."<br/>start time: ".$startTime."<br/>end time: ".$endTime);

        echo ("<br/> <h2>Values in json format</h2><p>Now just need to work out how to make a file and send it :p</p>");
        $array = array("ID" => $id, "employeeName" =>$name, "startDate" => $startDate, "startTime" => $startTime, "endTime" => $endTime);
        echo (json_encode($array));

    ?>
</body>
</html>