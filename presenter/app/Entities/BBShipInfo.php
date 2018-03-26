<?php

namespace App\Entities;

use \JsonSerializable;

class BBShipInfo implements JsonSerializable 
{
    //
    private $iShipType = 0;
    private $iShipX = 0;
    private $iShipY = 0;
    private $iShipDirection = 0;
    private $iShipLength = 0;
    
    function __construct($x, $y, $type, $direction, $length) {
        $this->iShipX = $x;
        $this->iShipY = $y;
        $this->iShipType = $type;
        $this->iShipDirection = $direction;
        $this->iShipLength = $length;
    }
    
    public function jsonSerialize()
    {
        return [
                'type' => $this->iShipType,
                'x' => $this->iShipX,
                'y' => $this->iShipY,
                'direction' => $this->iShipDirection,
                'length' => $this->iShipLength
               ];
    }

}
