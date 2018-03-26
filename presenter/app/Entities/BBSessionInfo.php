<?php

namespace App\Entities;

use \JsonSerializable;

class BBSessionInfo implements JsonSerializable
{
    //
    private $sSessionID = "";
    private $sSessionToken = "";
    private $sLoggedInUsername = "";
    private $flgSessionExpired = 0;
    
    function __construct($sId, $sToken, $sUser, $flg) {
        $this->sSessionID = $sId;
        $this->sSessionToken = $sToken;
        $this->sLoggedInUsername = $sUser;
        $this->flgSessionExpired = $flg;
    }
    
    public function jsonSerialize()
    {
        return [
                'id' => $this->sSessionID,
                'token' => $this->sSessionToken,
                'username' => $this->sLoggedInUsername,
                'expired' => $this->flgSessionExpired,
               ];
    }

}
