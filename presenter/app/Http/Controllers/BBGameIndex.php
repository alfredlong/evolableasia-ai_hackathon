<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use \Config;

class BBGameIndex extends Controller
{
    //
    private function getAIsFromFile() {

        $arrAIs = [];
        $sFileName = public_path() . "/bot_urls.txt";
        if (($handle = fopen($sFileName, "r")) !== FALSE) {

            while (($data = fgetcsv($handle, 1000, ",")) !== FALSE) {
                $id = urlencode($data[0]);
                $name = $data[2];
                $arrAIs["$id"] = "$name";
            }

            fclose($handle);
        }
        return $arrAIs;
    }

    public function index() {

        $gameAIs = $this->getAIsFromFile();

//        $gameAIs = $Config::get('hackathon.game_logic.presenter.ais');

        if ($gameAIs != null && count($gameAIs) > 0) {
            return $this->renderGameInitForm($gameAIs);
        }
        return "Config error, no AIs";
    }

    private function renderGameInitForm($gameAIs) {
        return view('bb_presenter_entry', ['ais' => $gameAIs]);
    }

}
