NEXT_MINOS = {0:"I", 1:"Z", 2:"J", 3:"O", 4:"S", 5:"T", 6:"L", 7:"LJ", 8:"O1", 9:"L1", 10:"J1", 11:"I1", 12:"I2", 13:"O2"}

WINDOW_POS = (1308, 273, 270, 528) # xpos, ypos, window_xsize, window_ysize
NEXT_POS = (1391, 233, 100, 30)
NEXT_IMGS = ["next_imgs/"+x[1]+"_binary.png" for x in NEXT_MINOS.items()]

CHIP_X = 27
CHIP_Y = 24

ALIGN = {
        "I":[3, 5],
        "Z":[3, 3],
        "J":[3, 3, 3, 4],
        "T":[3, 3, 3, 4],
        "O":[4],
        "S":[3, 3],
        "L":[3, 3, 3, 4],
        "LJ":[4, 3, 3, 4],
        "I2":[2, 4],
        "I1":[3, 4],
        "L1":[3, 4, 3, 4],
        "J1":[3, 4, 3, 4],
        "O1":[3, 3, 3, 4],
        "O2":[3, 3, 3, 4]
        }

TETRIMINOS = {
"I":[
    [[1, 1, 1, 1]],

    [[1],
     [1],
     [1],
     [1]]
     ]
     ,
"Z":[
    [[1, 1, 0],
     [0, 1, 1]],

    [[0, 1],
     [1, 1],
     [1, 0]]
     ]
     ,
"J":[
    [[1, 1, 1],
     [0, 0, 1]],

    [[0, 1],
     [0, 1],
     [1, 1]],

    [[1, 0, 0],
     [1, 1, 1]],

    [[1, 1],
     [1, 0],
     [1, 0]]

     ]
     ,
"T":[
    [[1, 1, 1],
     [0, 1, 0]],

    [[0, 1],
     [1, 1],
     [0, 1]],

    [[0, 1, 0],
     [1, 1, 1]],

    [[1, 0],
     [1, 1],
     [1, 0]]

     ]
     ,
"O":[
    [[1, 1],
     [1, 1]]
     ]
     ,
"S":[
    [[0, 1, 1],
     [1, 1, 0]],

    [[1, 0],
     [1, 1],
     [0, 1]]
     ]
     ,
"L":[
    [[1, 1, 1],
     [1, 0, 0]],

    [[1, 1],
     [0, 1],
     [0, 1]],

    [[0, 0, 1],
     [1, 1, 1]],

    [[1, 0],
     [1, 0],
     [1, 1]]
     ]
     ,
 "LJ":[
     [[1, 1, 1],
      [1, 0, 0],
      [1, 0, 0]],

     [[1, 1, 1],
      [0, 0, 1],
      [0, 0, 1]],

     [[0, 0, 1],
      [0, 0, 1],
      [1, 1, 1]],

     [[1, 0, 0],
      [1, 0, 0],
      [1, 1, 1]]
      ]
      ,
  "O1":[
     [[1, 1, 1],
      [0, 1, 1]],

     [[0, 1],
      [1, 1],
      [1, 1]],

     [[1, 1, 0],
      [1, 1, 1]]
      ,
     [[1, 1],
      [1, 1],
      [1, 0]],
      ],
  "O2":[
     [[1, 1, 1],
      [1, 1, 0]],

     [[1, 1],
      [1, 1],
      [0, 1]],

     [[0, 1, 1],
      [1, 1, 1]],

     [[1, 0],
      [1, 1],
      [1, 1]],
      ]
      ,
  "I1":[
     [[1, 1, 1]],

     [[1],
      [1],
      [1]]
      ]
      ,
  "I2":[
     [[1, 1, 1, 1, 1]],

     [[1],
      [1],
      [1],
      [1],
      [1]]
      ]
      ,

  "J1":[
     [[1, 1, 1, 1],
      [0, 0, 0, 1]],

     [[0, 1],
      [0, 1],
      [0, 1],
      [1, 1]],

     [[1, 0, 0, 0],
      [1, 1, 1, 1]],

     [[1, 1],
      [1, 0],
      [1, 0],
      [1, 0]],
      ]
      ,

  "L1":[
     [[1, 1, 1, 1],
      [1, 0, 0, 0]],

     [[1, 1],
      [0, 1],
      [0, 1],
      [0, 1]],

     [[0, 0, 0, 1],
      [1, 1, 1, 1]],

     [[1, 0],
      [1, 0],
      [1, 0],
      [1, 1]],
      ]
}
