
const toggleBtnOpen = document.querySelector('#menu-icon-open');

const toggleBtnClose = document.querySelector('#menu-icon-close');


const divList = document.querySelector('.menu-content');


toggleBtnOpen.addEventListener('click', () => {
	if(divList.style.display === 'none') {
		divList.style.display = 'flex';
	} else {
		divList.style.display = 'none';
	}
});


toggleBtnClose.addEventListener("click", () => {
  if (divList.style.display === "none") {
    divList.style.display = "flex";
  } else {
    divList.style.display = "none";
  }
});
