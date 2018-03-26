<?php

use Illuminate\Http\Request;

/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/user', function (Request $request) {
    return $request->user();
});

Route::get('boardfetch', 'BBBoardFetch@index');
Route::get('boardfetch/{sid}/{step}', 'BBBoardFetch@indexWithSessionId');
Route::get('boardinitfetch', 'BBInitBoardFetch@index');
Route::get('boardinitfetch/{red}/{blue}', 'BBInitBoardFetch@indexWithAIs');
Route::get('gamelogic/init/{sid}/{token}', 'BBInternalGameLogic@init');
Route::get('gamelogic/round/{sid}/{token}', 'BBInternalGameLogic@roundFetch');