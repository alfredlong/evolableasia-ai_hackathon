<?php
return [
    'AppName' => 'Hackathon duel platform', 
    'GameName' => 'Battleship',
    'app_info' => [
        'app_name' => 'Hackathon_Presenter',
        'author' => 'TienTN',
        'version' => '1.0'
    ],
    'game_session' => [
        'id' => 'dinhnv_phuongnv',
        'admin' => 'tientn@evolableasia.vn'
    ],
    'game_logic' => [
        'presenter' => [
            'ais' => [
                '4' => 'raijin',
                '5' => 'baby',
            ],
            'init' => [
                'url' => 'http://gameengine:5000/init'
            ],
            'round' => [
                'url' => 'http://gameengine:5000/round'
            ]
        ]
    ]
];
