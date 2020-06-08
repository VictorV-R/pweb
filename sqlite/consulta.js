function query(kind) {
  var xhttp;
  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function () {
    if (this.readyState == 4 && this.status == 200) {
      console.log("OJO:" + this.responseText);
    }
  };
  xhttp.open("GET", 'cgi-bin/consulta.py', true);
  xhttp.send();
}