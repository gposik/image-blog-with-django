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


// 



// const post = document.querySelector('.post-wrapper');

// const arrow = document.querySelector('#arrow');

// arrow.addEventListener('click', () => {
	
// 	let url = window.location.href;
// 	let splitted_url = url.split('/');
// 	console.log(splitted_url);
// 	let post_id = splitted_url.slice(-1)[0];
// 	console.log(post_id);
// 	arrow.href = post_id;	
// 	console.log(arrow.href);

// })