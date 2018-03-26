<?php

namespace App\Entities;

use \JsonSerializable;

class BBGameInfo implements JsonSerializable
{
    //
    private $sGameName = "";
    private $iWidth = 20;
    private $iHeight = 8;    
    private $timeStartAt = 0;
    private $timeEndAt = 0;
    private $flgSavedGame = 0;

    function __construct($gameName, $width, $height, $start, $end, $saved) {
        $this->sGameName = $gameName;
        $this->iWidth = $width;
        $this->iHeight = $height;    
        $this->timeStartAt = $start;
        $this->timeEndAt = $end;
        $this->flgSavedGame = $saved;
    }
    
    public function jsonSerialize()
    {
        return [
                'game_name' => $this->sGameName,
                'width' => $this->iWidth,
                'height' => $this->iHeight,
                'start_time' => $this->timeStartAt,
                'end_time' => $this->timeEndAt,
                'saved_game' => $this->flgSavedGame,
               ];
    }

}
