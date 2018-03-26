<!doctype html>
<html>
<head>
    <meta charset="utf-8" />
    <title>DeNA Travel lab - Hackathon platform</title>
    <link rel="shortcut icon" href="cube.ico" />
    <link rel="icon" type="image/png" href="cube.png" />
    <link href='http://fonts.googleapis.com/css?family=Roboto+Slab' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="css/app.css">
</head>
<body>
    <div class="container">
        <div class="center-block" id="test" style="border: 1 solid black; width: 1150px; background-color:black"></div>

        <script type="text/javascript">
            var sRedAIID = '{{$red_team}}';
            var sBlueAIID = '{{$blue_team}}';
            var flgDebugGrid = {{$debug_flg}};
            var flgHWAcceleration = {{$hw_acceleration}};
        </script>

            <script src="js/all.js"></script>

    </div>
</body>
</html>