            mapboxgl.accessToken = 'pk.eyJ1IjoibWF1cm8wOCIsImEiOiJjbG5yb2t6a2gwdGI5Mnpud3llaWczYjRpIn0.Tws5fCUS6WHs_-1ECbnCjA';
              
            var map = new mapboxgl.Map({
                container: 'map',
                style: 'mapbox://styles/mapbox/streets-v11',
                zoom: 14,
                center: [-74.787977,10.988829]
              });

              
              map.addControl(new mapboxgl.NavigationControl());
              map.addControl(new MapboxDirections({ accessToken: mapboxgl.accessToken}),'top-left')

              map.on('load', () => {


                map.addSource('route', {
                    'type': 'geojson',
                    'data': {
                        "type": "Feature",
                        "properties": {},
                        "geometry": {
                            "coordinates": [
                                [
                                    -74.78800038350337,
                                    10.988096995991157
                                ],
                                [
                                    -74.78822423488677,
                                    10.987307794338477
                                ],
                                [
                                    -74.7871073849742,
                                    10.987000619472283
                                ],
                                [
                                    -74.78689316160737,
                                    10.98778273331034
                                ],
                                [
                                    -74.7871073849742,
                                    10.987005345241542
                                ],
                                [
                                    -74.78631027882493,
                                    10.986774034722345
                                ],
                                [
                                    -74.78609846246239,
                                    10.987563237802476
                                ],
                                [
                                    -74.78631153021837,
                                    10.986781891026638
                                ],
                                [
                                    -74.7868701224486,
                                    10.98483428284618
                                ],
                                [
                                    -74.78734203657388,
                                    10.983198660223323
                                ],
                                [
                                    -74.78774653439609,
                                    10.981581937627283
                                ],
                                [
                                    -74.78813177717201,
                                    10.980088114121102
                                ],
                                [
                                    -74.78891188011403,
                                    10.9773179057255
                                ],
                                [
                                    -74.78943319144113,
                                    10.97540439477197
                                ],
                                [
                                    -74.78976064205895,
                                    10.97439273567376
                                ],
                                [
                                    -74.79005919997516,
                                    10.973626897977212
                                ],
                                [
                                    -74.79050222139878,
                                    10.972388316762306
                                ],
                                [
                                    -74.79088745741994,
                                    10.97122536936908
                                ],
                                [
                                    -74.79130256453429,
                                    10.970125733867434
                                ],
                                [
                                    -74.7920537741537,
                                    10.96834820577071
                                ],
                                [
                                    -74.79251605737922,
                                    10.967156877467005
                                ],
                                [
                                    -74.79283387709575,
                                    10.966362655931178
                                ],
                                [
                                    -74.7933828384254,
                                    10.965190229764858
                                ]
                            ],
                            "type": "LineString"
                        },
            
                    }
                },
            
                    map.addSource('route2', {
                        'type': 'geojson',
                        'data': {
                            "type": "Feature",
                            "properties": {},
                            "geometry": {
                                "coordinates": [
                                    [
                                        -74.80882505054734,
                                        10.996202971357675
                                    ],
                                    [
                                        -74.80712714002024,
                                        10.999536425702047
                                    ],
                                    [
                                        -74.80380666047265,
                                        11.001883239804869
                                    ],
                                    [
                                        -74.79844106882787,
                                        11.005747699013767
                                    ],
                                    [
                                        -74.79800801962882,
                                        11.006098855626846
                                    ],
                                    [
                                        -74.79954252005298,
                                        11.007263214034708
                                    ],
                                    [
                                        -74.80106290235173,
                                        11.008388158227973
                                    ],
                                    [
                                        -74.79547871407293,
                                        11.016015831974343
                                    ],
                                    [
                                        -74.80106232239379,
                                        11.008388691649088
                                    ],
                                    [
                                        -74.79956869784135,
                                        11.0072825967395
                                    ],
                                    [
                                        -74.80504972699254,
                                        11.003251803983858
                                    ],
                                    [
                                        -74.80484902237481,
                                        11.003076444595962
                                    ],
                                    [
                                        -74.8038725923254,
                                        11.001841067431613
                                    ]
                                ],
                                "type": "LineString"
                            },
            
                        }
                    },
            
            
                        map.addSource('route3', {
                            'type': 'geojson',
                            'data': {
                                "type": "Feature",
                                "properties": {},
                                "geometry": {
                                    "coordinates": [
                                        [
                                            -74.77822431809112,
                                            10.981286273556194
                                        ],
                                        [
                                            -74.77808433493621,
                                            10.982161688469233
                                        ],
                                        [
                                            -74.77781992231064,
                                            10.98312362395609
                                        ],
                                        [
                                            -74.77758661705276,
                                            10.983820897984032
                                        ],
                                        [
                                            -74.7773792346014,
                                            10.983754733366197
                                        ],
                                        [
                                            -74.77717703671118,
                                            10.983688568733555
                                        ],
                                        [
                                            -74.77719259039543,
                                            10.983540970652982
                                        ],
                                        [
                                            -74.77756069424625,
                                            10.982828427156264
                                        ],
                                        [
                                            -74.77781473774952,
                                            10.982385631402224
                                        ],
                                        [
                                            -74.77794953634329,
                                            10.982019179241675
                                        ],
                                        [
                                            -74.77803248932399,
                                            10.981657816248955
                                        ],
                                        [
                                            -74.77808433493621,
                                            10.981235377261157
                                        ],
                                        [
                                            -74.77822431809112,
                                            10.98124555652069
                                        ]
                                    ],
                                    "type": "LineString"
                                },
            
            
                            }
                        },
            
                        ),
            
                        map.addSource('route4', {
                            'type': 'geojson',
                            'data': {
                                "type": "Feature",
                                "properties": {},
                                "geometry": {
                                    "coordinates": [
                                        [
                                            -74.80043793307173,
                                            11.026559978952022
                                        ],
                                        [
                                            -74.79843294094732,
                                            11.024861151794411
                                        ],
                                        [
                                            -74.79762382209192,
                                            11.023970595570418
                                        ],
                                        [
                                            -74.79629191464485,
                                            11.022953383888463
                                        ],
                                        [
                                            -74.79543364981033,
                                            11.022404580158081
                                        ],
                                        [
                                            -74.7951380648252,
                                            11.022177368122968
                                        ],
                                        [
                                            -74.79810042637618,
                                            11.019849891086324
                                        ],
                                        [
                                            -74.79514101520323,
                                            11.022174457915483
                                        ],
                                        [
                                            -74.79461750926666,
                                            11.02160817484264
                                        ],
                                        [
                                            -74.79409400587619,
                                            11.02114675640945
                                        ],
                                        [
                                            -74.78765934203945,
                                            11.01368275194875
                                        ],
                                        [
                                            -74.7874695753588,
                                            11.013444720228662
                                        ],
                                        [
                                            -74.78725870348407,
                                            11.013279129688542
                                        ],
                                        [
                                            -74.78703728801473,
                                            11.013165286137664
                                        ],
                                        [
                                            -74.78681587254621,
                                            11.013103189636752
                                        ],
                                        [
                                            -74.78641521598347,
                                            11.013072141381386
                                        ],
                                        [
                                            -74.78610945176474,
                                            11.012999695440328
                                        ],
                                        [
                                            -74.785803687546,
                                            11.012823755221575
                                        ],
                                        [
                                            -74.7856349900464,
                                            11.012689212631201
                                        ],
                                        [
                                            -74.78624651848388,
                                            11.011830208485762
                                        ],
                                        [
                                            -74.78912928927869,
                                            11.009360587724444
                                        ],
                                        [
                                            -74.79035234615363,
                                            11.008066891205118
                                        ],
                                        [
                                            -74.78913812809645,
                                            11.009351543113553
                                        ],
                                        [
                                            -74.78625038180896,
                                            11.011831817242651
                                        ],
                                        [
                                            -74.78563520994916,
                                            11.012685183969836
                                        ],
                                        [
                                            -74.78444005392568,
                                            11.01189159399776
                                        ],
                                        [
                                            -74.78411467376858,
                                            11.011612128389984
                                        ],
                                        [
                                            -74.7835655947538,
                                            11.011083139191982
                                        ],
                                        [
                                            -74.78232418213098,
                                            11.009751991027912
                                        ],
                                        [
                                            -74.77977024607141,
                                            11.007437846544676
                                        ],
                                        [
                                            -74.7778842338792,
                                            11.005528672686808
                                        ],
                                        [
                                            -74.7763125570525,
                                            11.004005181642754
                                        ],
                                        [
                                            -74.77548742671753,
                                            11.002925233852878
                                        ],
                                        [
                                            -74.77440689889906,
                                            11.001382444429865
                                        ],
                                        [
                                            -74.77385681200963,
                                            11.000591761720713
                                        ],
                                        [
                                            -74.77348353876373,
                                            10.999878216967545
                                        ],
                                        [
                                            -74.77316920339825,
                                            10.998894679475555
                                        ]
            
                                    ],
                                    "type": "LineString"
                                },
            
            
                            }
                        },
            
                        ),
            
                        map.addSource('route5', {
                            'type': 'geojson',
                            'data': {
                                "type": "Feature",
                                "properties": {},
                                "geometry": {
                                    "coordinates": [
                                        [
                                            -74.79193356617466,
                                            10.990840721435617
                                        ],
                                        [
                                            -74.79450905773597,
                                            10.991300403087976
                                        ],
                                        [
                                            -74.79553925436093,
                                            10.99166814789315
                                        ],
                                        [
                                            -74.80101802731856,
                                            10.993185090371085
                                        ],
                                        [
                                            -74.80298476632922,
                                            10.993966542541557
                                        ],
                                        [
                                            -74.80682459011176,
                                            10.99594314761383
                                        ],
                                        [
                                            -74.80705872570806,
                                            10.996448788643832
                                        ],
                                        [
                                            -74.8074801697818,
                                            10.99654072328346
                                        ],
                                        [
                                            -74.8094937359118,
                                            10.997414100929035
                                        ],
                                        [
                                            -74.81623684109069,
                                            11.001367251597571
                                        ],
                                        [
                                            -74.82068541742443,
                                            11.003159941984862
                                        ],
                                        [
                                            -74.8233077361051,
                                            11.002976076805751
                                        ]
            
            
                                    ],
                                    "type": "LineString"
                                },
            
            
                            }
                        },
            
                        ),
            
            
                        map.addSource('route6', {
                            'type': 'geojson',
                            'data': {
                                "type": "Feature",
                                "properties": {},
                                "geometry": {
                                    "coordinates": [
                                        [
                                            -74.83412921514203,
                                            11.007852631625624
                                          ],
                                          [
                                            -74.83474136214306,
                                            11.00673988114822
                                          ],
                                          [
                                            -74.83517213225483,
                                            11.006383800107685
                                          ],
                                          [
                                            -74.83567091870023,
                                            11.006183504333677
                                          ],
                                          [
                                            -74.83700857325837,
                                            11.005671636735457
                                          ],
                                          [
                                            -74.8377794250375,
                                            11.00495947164255
                                          ]
            
                                    ],
                                    "type": "LineString"
                                },
            
            
                            }
                        },
            
                        ),
            
            
                    ));
                map.addLayer({
                    'id': 'route',
                    'type': 'line',
                    'source': 'route',
                    'layout': {
                        'line-join': 'round',
                        'line-cap': 'round'
                    },
                    'paint': {
                        'line-color': '#37FF8B',
                        'line-width': 4
                    }
                });
            
                map.addLayer({
                    'id': 'route2',
                    'type': 'line',
                    'source': 'route2',
                    'layout': {
                        'line-join': 'round',
                        'line-cap': 'round'
                    },
                    'paint': {
                        'line-color': '#CC2936',
                        'line-width': 4
                    }
            
            
                });
                map.addLayer({
                    'id': 'route3',
                    'type': 'line',
                    'source': 'route3',
                    'layout': {
                        'line-join': 'round',
                        'line-cap': 'round'
                    },
                    'paint': {
                        'line-color': '#C455A8',
                        'line-width': 4
                    }
            
            
                });
            
                map.addLayer({
                    'id': 'route4',
                    'type': 'line',
                    'source': 'route4',
                    'layout': {
                        'line-join': 'round',
                        'line-cap': 'round'
                    },
                    'paint': {
                        'line-color': '#013452',
                        'line-width': 4
                    }
            
            
                });
            
                map.addLayer({
                    'id': 'route5',
                    'type': 'line',
                    'source': 'route5',
                    'layout': {
                        'line-join': 'round',
                        'line-cap': 'round'
                    },
                    'paint': {
                        'line-color': '#017657',
                        'line-width': 4
                    }
            
            
                });
            
                map.addLayer({
                    'id': 'route6',
                    'type': 'line',
                    'source': 'route6',
                    'layout': {
                        'line-join': 'round',
                        'line-cap': 'round'
                    },
                    'paint': {
                        'line-color': '#4A2545',
                        'line-width': 4
                    }
            
            
                });
            });


document.getElementById("signup").addEventListener("click", function() {
    window.location.href = "/register";
});

document.getElementById("signin").addEventListener("click", function() {
    window.location.href = "/login";
});

//pk.eyJ1IjoibWF1cm8wOCIsImEiOiJjbG5yb3IzMW8xN29mMmpsZ3czcjV6eHhuIn0.SdhF9vumkwe29Sgh82dAug


