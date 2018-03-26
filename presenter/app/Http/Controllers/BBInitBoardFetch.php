<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use \Config;

class BBInitBoardFetch extends Controller
{
    private function getUrl(){
        if(isset($_SERVER['HTTPS'])){
            $protocol = ($_SERVER['HTTPS'] && $_SERVER['HTTPS'] != "off") ? "https" : "http";
        }
        else{
            $protocol = 'http';
        }
        return $protocol . "://" . $_SERVER['HTTP_HOST'];
    }

    //
    public function index()
    {
        //
        $sessionID = Config::get('hackathon.game_session.id');
        $gameLogicURL = Config::get('hackathon.game_logic.presenter.init.url');
        $sFullURL = $gameLogicURL . "/" . $sessionID . "/token";
        $result = file_get_contents($sFullURL);

        return response()->json(json_decode($result), 200);

    }

    public function indexWithAIs($red, $blue)
    {
        //
        //TienTN: now we not use hardcoded setting any more
        //$sessionID = Config::get('hackathon.game_session.id');
        $sessionID = $red . '|' . $blue;
        $gameLogicURL = Config::get('hackathon.game_logic.presenter.init.url');
        $sFullURL = $gameLogicURL . "/" . $sessionID . "/token";
        $result = file_get_contents($sFullURL);

        return response()->json(json_decode($result), 200);

    }

}
