<?php

namespace App\Entities;

use \JsonSerializable;

class BBGameRound implements JsonSerializable
{
    //
    private $flgGameEnd = 0;
    private $iTeamWin = 0;
    private $iRoundNumber = 0;
    private $iRoundTotal = 0;
    private $sHeaderMessage = 0;
    private $sFooterMessage = 0;
    
    function __construct($flg, $win, $number, $total, $hMsg, $fMsg) {
        $this->flgGameEnd = $flg;
        $this->iTeamWin = $win;
        $this->iRoundNumber = $number;
        $this->iRoundTotal = $total;
        $this->sHeaderMessage = $hMsg;
        $this->sFooterMessage = $fMsg;

    }
    
    public function jsonSerialize()
    {
        return [
                'round' => $this->iRoundNumber,
                'round_total' => $this->iRoundTotal,
                'game_end' => $this->flgGameEnd,
                'team_win' => $this->iTeamWin,
                'header_message' => $this->sHeaderMessage,
                'footer_message' => $this->sFooterMessage,
               ];
    }

}
