<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class BBGamePresenter extends Controller
{
    //
    public function index() {
        if (isset($_GET['red_team']) && isset($_GET['blue_team'])) {
            if (isset($_GET['debug_grid'])) {
                $debugGrid = 1;
            }
            else {
                $debugGrid = 0;
            }
            if (isset($_GET['hardware'])) {
                $hwAcceleration = 1;
            }
            else {
                $hwAcceleration = 0;
            }
            $debugCode = 0;
            if (isset($_GET['internalFlag'])) {
                $debugCode = 1;
            }
            return $this->renderGameScreen($_GET['red_team'], $_GET['blue_team'], $debugGrid, $hwAcceleration, $debugCode);
        }
        else {
            return redirect()->action('BBGameIndex@index');
        }
    }

    private function renderGameScreen($redTeam, $blueTeam, $debugFlg, $hwAcceleration, $debugCode) {
        return view('bb_presenter_stage', 
            [
                'red_team' => $redTeam, 
                'blue_team' => $blueTeam, 
                'debug_flg' => $debugFlg,
                'hw_acceleration' => $hwAcceleration,
                'debug_code' => $debugCode
            ]);
    }

}
