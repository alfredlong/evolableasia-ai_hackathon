<?php

namespace App\Entities;

use \JsonSerializable;

class BBTeamInfo implements JsonSerializable 
{
    //
    private $iScore = 0;
    private $iComboScore = 0;
    private $iMovesCount = 0;
    private $avgResponseTime = 0;
    private $slowestResponseTime = 0;
    private $lastResponseTime = 0;
    private $sTeamName = '';
    
    public function fillData($name, $score, $combo_score, $move_count, $avg_response, $slowest_response, $last_response) {
        $this->sTeamName = $name;
        $this->iScore = $score;
        $this->iComboScore = $combo_score;
        $this->iMovesCount = $move_count;
        $this->avgResponseTime = $avg_response;
        $this->slowestResponseTime = $slowest_response;
        $this->lastResponseTime = $last_response;
    }
    
    public function jsonSerialize()
    {
        //only work with public ... return get_object_vars($this);
        return [
                'team_name' => $this->sTeamName,
                'score' => $this->iScore,
                'combo_score' => $this->iComboScore,
                'moves' => $this->iMovesCount,
                'avg_response' => $this->avgResponseTime,
                'slowest_response' => $this->slowestResponseTime,
                'last_response' => $this->lastResponseTime
                ];
    }
    
}
