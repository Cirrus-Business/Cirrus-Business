<!DOCTYPE html>
<html>
<head>
    <title>Form 1 Test</title>
    <?php
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
</head>
<body>
    <h1>Enter your shift details</h1>
    <form id="shiftForm" name="shiftForm" action="result.php" method="post">
	    <label for="employee">Select your Name: </label>
        <select id="employee" name="employee">
            <?php
            echo ("<option value=null>Select your name...</option>");
            foreach ($employees as $item){
                echo ("<option value=$item[0]>".$item[1]."</option>");
            }
            ?>
        </select>
        <br/>
        <script>
            var date;

            function setStartDate() {
                date = new Date();
                document.getElementById("startDate").value =  date.getDate() + "-" + date.getMonth() + "-" +  date.getFullYear();
            }
            function setStartTime() {
                date = new Date();
                document.getElementById("startTime").value =  date.getHours() + ":" + date.getMinutes() + ":" +  date.getSeconds();
            }
            function setEndTime() {
                date = new Date();
                document.getElementById("endTime").value =  date.getFullYear() + "-" + date.getMonth() + "-" + date.getDate() + "T" + date.getHours() + ":" + date.getMinutes();
            }
        </script>
        <label for="startDate">Enter the time you started work:</label>
        <input type="text" id="startDate" name="startDate" placeholder="DD-MM-YYYY">
        <input type="button" id="autoStartDate" name="autoStartDate" onclick="setStartDate();" value="Click to use current date">
        <br/>
        <label for="startTime">Enter the time you started work:</label>
        <input type="text" id="startTime" name="startTime" placeholder="hh:mm:ss">
        <input type="button" id="autoStartTime" name="autoStartTime" onclick="setStartTime();" value="Click to use current time">
        <br/>
        <label for="endTime">Enter the time you end work:</label>
        <input type="datetime-local" id="endTime" name="endTime">
        <input type="button" id="autoEndTime" name="autoEndTime" onclick="return setEndTime();" value="Click to use current time">
        <br/>
        <span id="timeBetween"></span>
        <br/>
        <button type="submit">Submit</button> - <button type="reset">Reset</button>
    </form>
</body>
</html>