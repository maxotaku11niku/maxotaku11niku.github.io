var commonFooter = document.getElementById("commonFooter");
var commonFooterYearNamePara = commonFooter.getElementsByTagName("p")[0];
dateNow = new Date(Date.now());
commonFooterYearNamePara.innerHTML = dateNow.getFullYear() + " Maxim Hoxha";