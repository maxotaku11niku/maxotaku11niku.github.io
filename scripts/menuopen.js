var menuOpen = false;
var menuButton = document.getElementById("menuButton");
var menuList = document.getElementById("menu");
var currentH = 0;
menuButton.onclick = menuOpenHandler;

function menuOpenHandler(event) {
	if(menuOpen) {
		menuButton.setAttribute("class", "closed");
		menuList.setAttribute("class", "closed");
		menuOpen = false;
		cancelAnimationFrame(menuOpenAni);
		menuCloseAni();
	}
	else {
		menuButton.setAttribute("class", "open");
		menuList.setAttribute("class", "open");
		menuOpen = true;
		menuOpenAni();
	}
}

function menuOpenAni() {
	currentH += 34.0;
	menuList.style = "height: " + currentH + "pt;";
	if(currentH >= 340.0) {
		return;
	}
	requestAnimationFrame(menuOpenAni);
}

function menuCloseAni() {
	currentH = 0.0;
	menuList.style = "height: " + currentH + "pt;";
}