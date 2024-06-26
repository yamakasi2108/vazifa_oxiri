<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Datetime Difference Calculation</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            padding: 20px;
        }
        form {
            display: flex;
            flex-direction: column;
            max-width: 400px;
            margin: auto;
        }
        input[type="datetime-local"],
        input[type="time"] {
            margin-bottom: 10px;
            padding: 5px;
            font-size: 16px;
        }
        button {
            padding: 10px;
            background-color: #4CAF50;
            color: white;
            border: none;
            cursor: pointer;
        }
        button:hover {
            background-color: #45a049;
        }
        .result {
            max-width: 400px;
            margin: auto;
            margin-top: 20px;
            padding: 10px;
            background-color: #f2f2f2;
            border: 1px solid #ddd;
        }
        .result p {
            margin: 0;
            font-size: 16px;
        }
    </style>
</head>
<body>

<h2>Sanalar va vaqtlar orasidagi farqni hisoblash</h2>
<form action="index_11.php" method="post">
    Date <input type="datetime-local" name="date"> <br>
    Time gone <input type="time" name="time"> <br>

    Date_2 <input type="datetime-local" name="date_2"> <br>
    Time gone_2 <input type="time" name="time_2"> <br>

    Date_3 <input type="datetime-local" name="date_3"> <br>
    Time gone_3 <input type="time" name="time_3"> <br>

    Date_4 <input type="datetime-local" name="date_4"> <br>
    Time gone_4 <input type="time" name="time_4"> <br>

    Date_5 <input type="datetime-local" name="date_5"> <br>
    Time gone_5 <input type="time" name="time_5"> <br>

    <button type="submit">Hisobla</button>
</form>

<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    function calculateTimeDifference($dateTimeStart, $dateTimeEnd) {
        $interval = $dateTimeStart->diff($dateTimeEnd);
        return ($interval->h * 3600) + ($interval->i * 60) + $interval->s;
    }

    function secondsToTime($seconds) {
        $hours = floor($seconds / 3600);
        $minutes = floor(($seconds % 3600) / 60);
        $seconds = $seconds % 60;

        return sprintf("%02d:%02d:%02d", $hours, $minutes, $seconds);
    }

    $totalSeconds = 0;

    for ($i = 1; $i <= 5; $i++) {
        $date = $_POST["date" . ($i == 1 ? "" : "_" . $i)];
        $time = $_POST["time" . ($i == 1 ? "" : "_" . $i)];

        if (!empty($date) && !empty($time)) {
            $dateTime = new DateTime($date);
            $dateTimeGone = clone $dateTime;
            $secondsGone = strtotime($time) - strtotime('TODAY');
            $dateTimeGone->modify("+$secondsGone seconds");

            $totalSeconds += calculateTimeDifference($dateTime, $dateTimeGone);
        }
    }

    $formattedTime = secondsToTime($totalSeconds);
    echo "<div class='result'><p>Umumiy farq: $formattedTime</p></div>";
}
?>

</body>
</html>
