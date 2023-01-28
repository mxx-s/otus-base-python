
  

  const hourLeft = document.querySelector(".time-line.hourLeft");
const hourRight = document.querySelector(".time-line.hourRight");
const minuteLeft = document.querySelector(".time-line.minuteLeft");
const minuteRight = document.querySelector(".time-line.minuteRight");
const secondLeft = document.querySelector(".time-line.secondLeft");
const secondRight = document.querySelector(".time-line.secondRight");

function updateLine(line, index) {
	const numbers = [...line.children];
	numbers.forEach((el) => el.classList.remove("active"));
	const number = line.children[index];
	line.style.translate = `0px -${number.offsetTop}px 0px`;
	number.classList.add("active");
}
function updateClock() {
	const time = new Date().toTimeString();
	updateLine(hourLeft, Number(time.charAt(0)));
	updateLine(hourRight, Number(time.charAt(1)));
	updateLine(minuteLeft, Number(time.charAt(3)));
	updateLine(minuteRight, Number(time.charAt(4)));
	updateLine(secondLeft, Number(time.charAt(6)));
	updateLine(secondRight, Number(time.charAt(7)));
}

const clock = document.querySelector(".clock");
let clockUpdate;

clockUpdate = setInterval(() => updateClock(), 1000);