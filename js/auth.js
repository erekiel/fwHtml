$(function(){

function getAuth(){ 
    //alert(SHA256($("#pwd").val()));
    $.ajax({
            method: "POST",
                url: "fw_authentification.py",
                data: { 
                    pwd: SHA256($("#pwd").val()),
                    usr: $("#usr").val(),
                }
        })
        .done(
            function(reponse) {
                // alert(reponse);
                if($.trim(reponse) != ""){
                    setCookie("idSession", $.trim(reponse), 1);
                    setCookie("usr", $("#usr").val(), 1);
                    $("#resultat").html("Bienvenue " + $("#usr").val());
                    
                    // $("#resultat").html("idSession : " + reponse);
                    // $("#resultat").html($("#resultat").html() + "<p>cookie : " + document.cookie + "</p>");
                    
                    var p = getCookie("origine");
                    //alert("cookie origine : " + p);
                    
                    if(p){
                        deleteCookie("origine");
                        document.location = p;
                    }
                    
                }
                else{
                    $("#resultat").html("identification incorrecte...");
                }
        });
        
    return false;
}

function getAuth2(){ 
    $.ajax({
            method: "POST",
                url: "fw_authentification.py",
                data: { 
                    pwd: SHA256($("#pwd").val()),
                    usr: $("#usr").val(),
                }
        })
        .done(
            function(reponse) {
                reponse = JSON.parse(reponse);
                $("#resultat").html(reponse.commentaire);
                if(reponse.idSession != ""){
                    setCookie("idSession", $.trim(reponse.idSession), 1);
                    setCookie("usr", $("#usr").val(), 1);
                }
                
                if(reponse.redirige != ""){
                    document.location = reponse.redirige;
                } 
        });
        
    return false;
}

$("#btGoLogin").click(getAuth2);
$("#usr").focus();


});