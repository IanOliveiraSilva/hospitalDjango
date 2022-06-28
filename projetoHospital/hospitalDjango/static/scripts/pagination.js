const newsMain = document.querySelector(".news-pag__main");

const listNews = document.querySelectorAll(".news-pag__news-image-wrapper");
const newsTitle = document.querySelectorAll(".news-pag__news-title");

var currentPage = 1;
var newsPerPage = 12;

function prevPage() {
  if (currentPage > 1) {
    currentPage--;
    changePage(currentPage);
  }
}

function nextPage() {
  if (currentPage < numPages()) {
    currentPage++;
    changePage(currentPage);
  }
}

function changePage(page) {
  var pagNext = document.querySelector("#pag-next");
  var pagPrev = document.querySelector("#pag-prev");
  var page_span = document.querySelector("#page");

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
  page_span.innerHTML = page;

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
}

function numPages() {
  console.log(Math.ceil(newsTitle.length / newsPerPage));
  return Math.ceil(newsTitle.length / newsPerPage);
}

window.onload = function () {
  changePage(1);
};
