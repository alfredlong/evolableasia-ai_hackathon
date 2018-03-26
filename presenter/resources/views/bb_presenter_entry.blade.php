<!doctype html>
<html>
<head>
    <meta charset="utf-8" />
    <title>DeNA Travel lab - Hackathon duel platform</title>
    <link rel="shortcut icon" href="cube.ico" />
    <link rel="icon" type="image/png" href="cube.png" />
    <link href='http://fonts.googleapis.com/css?family=Roboto+Slab' rel='stylesheet' type='text/css'>
    <link rel="stylesheet" href="css/app.css">
</head>
<body>
    <div class="container">
        <h1>DeNA Travel lab - Hackathon platform (<a href="/about">about</a>)</h1>
         <form action="/game_start">
            <div class="form-group">
                <label class="control-label " for="player1">Red team:</label>
                <select class="form-control" id="player1" name="red_team">
                    @foreach($ais as $key => $value)
                    <option value="{{ $key }}">{{ $value }}</option>
                    @endforeach
                </select>
            </div>
            <div class="form-group">
                <label class="control-label " for="player1">Blue team:</label>
                <select class="form-control" id="player2" name="blue_team">
                    @foreach($ais as $key => $value)
                    <option value="{{ $key }}">{{ $value }}</option>
                    @endforeach
                </select>
            </div>
            <div class="checkbox">
              <label>
                <input type="checkbox"  name="debug_grid" value="debug_grid">
                Debug Grid
              </label>
            </div>
            <div class="checkbox">
              <label>
                <input type="checkbox"  name="hardware" value="hardware">
                Hardware Acceleration
              </label>
            </div>
            <div class="form-group"> <!-- Submit button !-->
                <button class="btn btn-primary " name="submit" type="submit">Submit</button>
            </div>
        </form> 

    </div>
</body>
</html>