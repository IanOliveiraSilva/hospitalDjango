window.onscroll = function () {
    scrollFunction();
  };
  
  function scrollFunction() {
    const $lines = document.querySelectorAll(".header__menu--line");
    
    if (document.body.scrollTop > 90 || document.documentElement.scrollTop > 90) {
      const fontSizeTitle = 40 / 16;
      const fontSizeAlt = 15 / 16;
  
      document.querySelector(".header__title--logo").style.width = "40px";
  
      document.querySelector(
        ".header__title--title"
      ).style.fontSize = `${fontSizeTitle}rem`;
  
      document.querySelector(
        ".header__menu--title"
      ).style.fontSize = `${fontSizeAlt}rem`;
  
      document.querySelector(".header__menu").style.width = "40px";
      document.querySelector(".header__menu").style.margin = "0";
  
      for (let $i = 0; $i < $lines.length; $i++) {
        $lines[$i].style.height = "2px";
      }
    } else {
      const fontSizeTitle = 56 / 16;
      const fontSizeAlt = 20 / 16;
  
      document.querySelector(".header__title--logo").style.width = "70px";
  
      document.querySelector(
        ".header__title--title"
      ).style.fontSize = `${fontSizeTitle}rem`;
  
      document.querySelector(
        ".header__menu--title"
      ).style.fontSize = `${fontSizeAlt}rem`;
  
      document.querySelector(".header__menu").style.width = "50px";
      document.querySelector(".header__menu").style.margin = "2vh 0 0 0";
  
      for (let $i = 0; $i < $lines.length; $i++) {
        $lines[$i].style.height = "4px";
      }
    }
  }
  