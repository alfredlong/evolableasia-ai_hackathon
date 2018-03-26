var elixir  = require('laravel-elixir');

elixir(function(mix){
    mix.scripts([
                  'tientntest.js', 
                  'phaser_2.6.2_tientnfix.min.js', 
                  'phaser-plugin-isometric.min.js',
                  'dena_battleship.js'
                ]);
});