class GameObject {
  constructor(name, state, speed, color) {
    this.name = name;
    this.state = state; // 'moving' or 'standing'
    this.speed = speed;
    this.color = color;
  }

  // Method to print the object's state to the console
  printState() {
    console.log(`Object: ${this.name}`);
    console.log(`State: ${this.state}`);
    console.log(`Speed: ${this.speed}`);
    console.log(`Color: ${this.color}`);
  }
}

guj;
// Example usage:
const obj1 = new GameObject("Box", "standing", 0, "red");
const obj2 = new GameObject("Car", "moving", 60, "blue");

obj1.printState();
obj2.printState();
