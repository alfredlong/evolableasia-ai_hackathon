<?php

namespace App\Entities;

use \JsonSerializable;

class BBPosInfo implements JsonSerializable
{
    //
    private $iX = 0;
    private $iY = 0;

    function __construct($x, $y) {
        $this->iX = $x;
        $this->iY = $y;
    }
    
    public function jsonSerialize()
    {
        return [
                'x' => $this->iX,
                'y' => $this->iY,
               ];
    }

}
