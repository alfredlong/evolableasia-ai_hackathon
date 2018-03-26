<?php
/**************************************
 TienTN: We don't need Model extension
 **************************************/
namespace App\Entities;

use App\Entities\BBTeamInfo;
use App\Entities\BBShipInfo;
use App\Entities\BBPosInfo;
use App\Entities\BBGameInfo;

use \Config;

//use PHP 5.4+ abstract
use \JsonSerializable;

class BBBoardInfo implements JsonSerializable 
{
    //
    private $objSession;
    private $objGameInfo;
    private $objGameRound;
    
    private $arrRedShips = [];
    private $arrBlueShips = [];
    
    private $arrRedHitPos = [];
    private $arrBlueHitPos = [];
    private $arrRedExplodePos = [];
    private $arrBlueExplodePos = [];
    private $arrRedWaterExplodePos = [];
    private $arrBlueWaterExplodePos = [];
    private $arrRedShipSinkPos = [];
    private $arrBlueShipSinkPos = [];
    
    private $infoRedTeam = null;
    private $infoBlueTeam = null;

    private $arrRedLayout = [
                        [0, 0, 0, 1, 2],
                        [0, 7, 1, 1, 2],
                        [17, 0, 2, 1, 2],
                        [19, 7, 3, 1, 2],
                        [2, 1, 0, 0, 2],
                        [10, 2, 0, 1, 4],
                        [1, 1, 1, 0, 2],
                        [3, 3, 2, 0, 2],
                        [15, 6, 3, 0, 2],
                        [12, 4, 4, 0, 4],
                        [5, 4, 5, 0, 2],
                    ];
    private $arrBlueLayout = [
                        [0, 0, 4, 0, 2],
                        [0, 6, 5, 0, 2],
                        [19, 0, 0, 0, 2],
                        [19, 6, 1, 0, 2],
                        [5, 4, 0, 0, 4],
                        [2, 2, 0, 0, 4],
                        [3, 3, 1, 1, 2],
                        [1, 1, 2, 1, 2],
                        [10, 10, 3, 1, 2],
                        [12, 4, 4, 1, 4],
                     ];
    
    function __construct($sid, $token) {
        $this->infoRedTeam = new BBTeamInfo();
        $this->infoRedTeam->fillData("Hoàng Sa Fleet", 
                            $this->randBetween(0, 100), 
                            intval($token), 
                            $this->randBetween(0, 100), 
                            $this->randBetween(0, 100), $this->randBetween(0, 100), $this->randBetween(0, 100));
        $this->infoBlueTeam = new BBTeamInfo();
        $this->infoBlueTeam->fillData("Hạm đội 7", 
                            $this->randBetween(0, 100), 
                            intval($token), 
                            $this->randBetween(0, 100), 
                            $this->randBetween(0, 100), $this->randBetween(0, 100), $this->randBetween(0, 100));

        $sessionID = $sid;
        
        $this->objSession = new BBSessionInfo($sessionID, "reqno_1", "dena", 0);
        $this->objGameInfo = new BBGameInfo("AI1vs_AI2", 20, 8, 0, 0, 0);

        $flgGameEnd = 0;
        //forced ending
        if (intval($token) > 19) {
            $flgGameEnd = 1;
        }
        $this->objGameRound = new BBGameRound($flgGameEnd, 0, 1, 0, 'Initializing ...', 'Wait');
        
        //init, for the json output
        $this->arrRedShipSinkPos = [];
        $this->arrBlueShipSinkPos = [];
        $this->arrRedWaterExplodePos = [];
        $this->arrBlueWaterExplodePos = [];
        $this->arrRedExplodePos = [];
        $this->arrBlueExplodePos = [];
        $this->arrRedHitPos = [];
        $this->arrBlueHitPos = [];

        $iTest1Type = 0;
        $iTest2Type = 0;
        $iTest3Type = 0;
        $iTest4Type = 0;
        /*
        //TienTN: rotate types, but now we are rendering just one time
        //so disabled by now
        $iRangeTypeFrom = $token - ((int)floor($token/6) * 6);
        $iTest1Type = $iRangeTypeFrom;
        $iTest2Type = ($iTest1Type + 1)<6?$iTest1Type + 1:0;
        $iTest3Type = ($iTest2Type + 1)<6?$iTest2Type + 1:0;
        $iTest4Type = ($iTest3Type + 1)<6?$iTest3Type + 1:0;
        */

        //type: 0 BB
        //dir: 0 vertical
        //x, y, type, direction, length
        foreach ($this->arrRedLayout as $layout) {
            $objShip = new BBShipInfo($layout[0], $layout[1], $layout[2], $layout[3], $layout[4]);
            $this->arrRedShips[] = $objShip;
        }

        foreach ($this->arrBlueLayout as $layout) {
            $objShip = new BBShipInfo($layout[0], $layout[1], $layout[2], $layout[3], $layout[4]);
            $this->arrBlueShips[] = $objShip;
        }
        
        $this->createRedHitPos(intval($token));
        $this->createBlueHitPos(intval($token));
        
        $this->createRedExplodePos(intval($token));
        $this->createBlueExplodePos(intval($token));
        
        $this->createRedWaterExplodePos(intval($token));
        $this->createBlueWaterExplodePos(intval($token));

        $this->createRedShipSinkPos(intval($token));
        $this->createBlueShipSinkPos(intval($token));

    }

    function isSomethingHit($arrData, $x, $y) {
        foreach ($arrData as $layout) {
            if ($layout[0] == $x && $layout[1] == $y) {
                return true;
            }
        }
        return false;
    }

    function isRedHit($x, $y) {
        return $this->isSomethingHit($this->arrRedLayout, $x, $y);
    }

    function isBlueHit($x, $y) {
        return $this->isSomethingHit($this->arrBlueLayout, $x, $y);
    }

    function createRedShipSinkPos($step) {
        $objPos = new BBPosInfo(0, 0);
        $this->arrRedShipSinkPos[] = $objPos;

    }

    function createBlueShipSinkPos($step) {
        $objPos = new BBPosInfo(0, 0);
        $this->arrBlueShipSinkPos[] = $objPos;
    }

    function createRedWaterExplodePos($step) {
        if ($step > 19) {
            $step = 19;
        }
        if ($step == 3) {
            //combo shot
            $objPos = new BBPosInfo(3, $this->randBetween(0,7));
            $this->arrRedWaterExplodePos[] = $objPos;
            $objPos = new BBPosInfo(5, $this->randBetween(0,7));
            $this->arrRedWaterExplodePos[] = $objPos;
            $objPos = new BBPosInfo(7, $this->randBetween(0,7));
            $this->arrRedWaterExplodePos[] = $objPos;

        }
        else {
            $objPos = new BBPosInfo($step, $this->randBetween(0,7));
            $this->arrRedWaterExplodePos[] = $objPos;
        }

    }

    function createBlueWaterExplodePos($step) {
        if ($step > 19) {
            $step = 19;
        }
        if ($step == 3) {
            //combo shot
            $objPos = new BBPosInfo(3, $this->randBetween(0,7));
            $this->arrBlueWaterExplodePos[] = $objPos;
            $objPos = new BBPosInfo(5, $this->randBetween(0,7));
            $this->arrBlueWaterExplodePos[] = $objPos;
            $objPos = new BBPosInfo(7, $this->randBetween(0,7));
            $this->arrBlueWaterExplodePos[] = $objPos;

        }
        else {
            $objPos = new BBPosInfo($step, $this->randBetween(0,7));
            $this->arrBlueWaterExplodePos[] = $objPos;
        }
    }

    function createRedExplodePos($step) {

        if ($step > 19) {
            $step = 19;
        }
        if ($step ==3) {
            $objPos = new BBPosInfo(4, $this->randBetween(0,7));
            $this->arrRedExplodePos[] = $objPos;
            $objPos = new BBPosInfo(6, $this->randBetween(0,7));
            $this->arrRedExplodePos[] = $objPos;
            $objPos = new BBPosInfo(8, $this->randBetween(0,7));
            $this->arrRedExplodePos[] = $objPos;
            $objPos = new BBPosInfo(9, $this->randBetween(0,7));
            $this->arrRedExplodePos[] = $objPos;
        }
        else {
            $objPos = new BBPosInfo($step, $this->randBetween(0,7));
            $this->arrRedExplodePos[] = $objPos;
        }

    }

    function createBlueExplodePos($step) {

        if ($step > 19) {
            $step = 19;
        }
        if ($step == 3) {
            $objPos = new BBPosInfo(4, $this->randBetween(0,7));
            $this->arrBlueExplodePos[] = $objPos;
            $objPos = new BBPosInfo(6, $this->randBetween(0,7));
            $this->arrBlueExplodePos[] = $objPos;
            $objPos = new BBPosInfo(8, $this->randBetween(0,7));
            $this->arrBlueExplodePos[] = $objPos;
            $objPos = new BBPosInfo(9, $this->randBetween(0,7));
            $this->arrBlueExplodePos[] = $objPos;
        }
        else {
            $objPos = new BBPosInfo($step, $this->randBetween(0,7));
            $this->arrBlueExplodePos[] = $objPos;
        }

    }

    function createRedHitPos($step) {
        if ($step > 19) {
            $step = 19;
        }
        $objPos = new BBPosInfo($this->randBetween(0, 19), $step);
        $this->arrRedHitPos[] = $objPos;
    }

    function createBlueHitPos($step) {
        if ($step > 19) {
            $step = 19;
        }
        $objPos = new BBPosInfo($this->randBetween(0, 19), $step);
        $this->arrBlueHitPos[] = $objPos;
    }
    
    function randBetween($iFrom, $iTo) {
        return rand($iFrom, $iTo);
    }

    function jsonSerialize() {
        return [
            'session_info' => $this->objSession,
            'game_info' => $this->objGameInfo,
            'game_round' => $this->objGameRound,
            'red_board' => [
                            'ships' => $this->arrRedShips,
                            'hitpos' => $this->arrRedHitPos,
                            'events' => [
                                        'explode' => $this->arrRedExplodePos,
                                        'waterhit' => $this->arrRedWaterExplodePos,
                                        'shipsink' => $this->arrRedShipSinkPos,
                                        ],
                           ],
            'blue_board' => [
                            'ships' => $this->arrBlueShips,
                            'hitpos' => $this->arrBlueHitPos,
                            'events' => [
                                        'explode' => $this->arrBlueExplodePos,
                                        'waterhit' => $this->arrBlueWaterExplodePos,
                                        'shipsink' => $this->arrBlueShipSinkPos,
                                        ],
                           ],
            'red_team' => $this->infoRedTeam,
            'blue_team' => $this->infoBlueTeam
        ];
    }
}
