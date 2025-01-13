input.onButtonPressed(Button.A, function () {
    basic.showNumber(randint(0, 99))
})
input.onButtonPressed(Button.B, function () {
    letter = randint(1, 5)
    if (letter == 1) {
        basic.showIcon(IconNames.No)
    } else if (letter == 2) {
        basic.showLeds(`
            # . . . .
            # . . . .
            # # # . .
            # . . . .
            # # # . .
            `)
    } else if (letter == 3) {
        basic.showLeds(`
            # . . . .
            # . . . .
            # # # . .
            # . # . .
            # # # . .
            `)
    } else if (letter == 4) {
        basic.showLeds(`
            # # # # #
            # . # . #
            # . # . #
            # . # . #
            # . # . #
            `)
    } else {
        basic.showLeds(`
            # . . . .
            # . . . .
            # # # . .
            # . # . .
            # . # . .
            `)
    }
})
input.onGesture(Gesture.Shake, function () {
    pass2 = ""
    for (let index = 0; index < 9; index++) {
        pass2 = "" + pass2 + String.fromCharCode(randint(33, 122))
    }
    basic.showString(pass2)
})
let pass2 = ""
let letter = 0
basic.showString("Press A or B")
basic.forever(function () {
	
})
