function code() {

    let canvas = document.getElementById('canvas');
    let context = canvas.getContext('2d');
    let windowWidthAdjuster = document.getElementById('windowWidth').value;
    let windowHeightAdjuster = document.getElementById('windowHeight').value;
    let windowWidth = window.innerWidth - windowWidthAdjuster;
    let windowHeight = window.innerHeight - windowHeightAdjuster;
    let circleRadiusAdjuster = document.getElementById('circleRadius').value;
    let startXPosAdjuster = document.getElementById('startXPos').value;
    let startYPosAdjuster = document.getElementById('startYPos').value;
    canvas.width = windowWidth;
    canvas.height = windowHeight;

    let colors = ['red', 'green', 'pink', 'purple', 'orange', 'blue', 'yellow', 'white', 'grey', 'maroon', 'turquoise', '#FF6F61'];


    class Circle{
        constructor(xpos, ypos, radius, color, lineWidth, speed) {
            this.xpos = xpos;
            this.ypos = ypos;
            this.radius = radius;
            this.color = color;
            this.lineWidth = lineWidth;
            this.speed = speed;

            this.dx = 1 * this.speed;
            this.dy = 1 * this.speed;
        }

        draw(context) {
            context.beginPath();
            context.arc(this.xpos, this.ypos, this.radius, 0, Math.PI * 2, false);
            context.strokeStyle = this.color;
            context.lineWidth = this.lineWidth;
            context.stroke()
        }

        update() {
            this.color = colors[(Math.floor(Math.random() * colors.length))];
            this.xpos += this.dx;
            this.ypos += this.dy;

            if ((this.xpos + this.radius) > windowWidth) {
                this.dx = -this.dx;
            }
            if ((this.ypos + this.radius) > windowHeight) {
                this.dy = -this.dy;
            }
            if ((this.xpos - this.radius) < 0) {
                this.dx = -this.dx;
            }
            if ((this.ypos - this.radius) < 0) {
                this.dy = -this.dy;
            }
        }
    }

    let newCircle = new Circle(100, 100, 50, 'red', 1, 10);


    function update() {
        requestAnimationFrame(update);
        newCircle.draw(context);
        newCircle.update();
    }

    update();

}

code();