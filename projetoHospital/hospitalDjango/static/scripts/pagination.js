const newsMain = document.querySelector(".news-pag__main");

const listNews = document.querySelectorAll(".news-pag__news-image-wrapper");
const newsTitle = document.querySelectorAll(".news-pag__news-title");
var page_span = document.querySelector("#num-page-wrapper");

var pagNext = document.querySelector("#pag-next");
var pagPrev = document.querySelector("#pag-prev");

var currentPage = 1;
var newsPerPage = 12;

for (let i = 0; i < numPages(); i++) {
  var url = window.location.href;
  url = url.split("#");
  page_span.innerHTML += `<a href="${url[0]}#/page/${
    i + 1
  }" class="num-page" value="${1 + i}">${1 + i}</a>`;
}

const numPage = document.querySelectorAll(".num-page");
numPage[currentPage-1].className += " active";

function resetActive() {
  for (let j = 0; j < numPage.length; j++) {
    numPage[j].className = "num-page";
  }
}

for (let i = 0; i < numPage.length; i++) {
  numPage[i].onclick = function () {
    resetActive();
    changePage(i + 1);
    numPage[i].className += " active";
    currentPage = i + 1;
  };
}

function prevPage() {
  if (currentPage > 1) {
    resetActive();
    currentPage--;
    numPage[currentPage - 1].className += " active";
    changePage(currentPage);
  }
}

function nextPage() {
  if (currentPage < numPages()) {
    resetActive();
    currentPage++;
    numPage[currentPage - 1].className += " active";
    changePage(currentPage);
  }
}

function changePage(page) {
  // Validate page
  if (page < 1) page = 1;
  if (page > numPages()) page = numPages();

  for (j = 0; j < newsTitle.length; j++) {
    listNews[j].style.display = "none";
  }

  for (
    var i = (page - 1) * newsPerPage;
    i < page * newsPerPage && i < listNews.length;
    i++
  ) {
    if (page === 1) {
      newsMain.style.display = "flex";
      listNews[i].style.display = "flex";
    } else {
      newsMain.style.display = "none";
      listNews[i].style.display = "flex";
    }
  }

  if (page == 1) {
    pagPrev.style.visibility = "hidden";
  } else {
    pagPrev.style.visibility = "visible";
  }

  if (page == numPages()) {
    pagNext.style.visibility = "hidden";
  } else {
    pagNext.style.visibility = "visible";
  }

  var url = window.location.href;
  if (url.includes("#")) {
    url = url.split("#");
    location.replace = `${url[0]}#/page/${page}`;
    console.log(page);
  } else {
    console.log("b");
    document.location = document.location.hash + `#/page/${page}`;
  }
}

function numPages() {
  return Math.ceil(newsTitle.length / newsPerPage);
}

window.onload = function () {
  changePage(1);
};
